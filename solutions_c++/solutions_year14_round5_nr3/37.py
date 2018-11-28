#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <utility>
#define MAXN 1005
#define MAXID 2005
#define MYINF 1000000000

using namespace std;

struct node
{
	char type;
	int id;
};

struct seg
{
	int l, r, what;
	char look, ok;
};

int main ()
{
	int T, iT;
	scanf("%d",&T);
	for (iT = 0; iT < T; iT++)
	{
		int N;
		scanf("%d",&N);
		static struct node data[MAXN];
		int i;
		for (i = 0; i < N; i++)
		{
			scanf("\n%c %d",&(data[i].type),&(data[i].id));
		}
		static struct seg s[MAXN];
		int sc = 0;
		static int b[MAXID];
		memset(b,0,sizeof(b));
		for (i = 0; i < N; i++)
		{
			if (data[i].id != 0)
			{
				if (data[i].type == 'E')
				{
					if (b[data[i].id] > 0)
					{
						s[sc].l = b[data[i].id] - 1;
						s[sc].r = i;
						s[sc].what = data[i].id;
						s[sc].look = 'L';
						s[sc].ok = 0;
						sc++;
					}
					b[data[i].id] = i+1;
				}
				else
				{
					if (b[data[i].id] < 0)
					{
						s[sc].l = (-b[data[i].id]) - 1;
						s[sc].r = i;
						s[sc].what = data[i].id;
						s[sc].look = 'E';
						s[sc].ok = 0;
						sc++;
					}
					b[data[i].id] = -(i+1);
				}
			}
		}
		for (i = 0; i < N; i++)
		{
			if (data[i].id == 0)
			{
				int minr = MYINF;
				int minpos = -1;
				int j;
				for (j = 0; j < sc; j++)
				{
					if ((s[j].look == data[i].type) && (s[j].r >= i) && (s[j].l <= i) && (!s[j].ok))
					{
						if (s[j].r < minr)
						{
							minr = s[j].r;
							minpos = j;
						}
					}
				}
				if (minpos != -1)
				{
					data[i].id = s[minpos].what;
					s[minpos].ok = 1;
				}
			}
		}
		char ok = 1;
		for (i = 0; i < sc; i++)
		{
			if (!s[i].ok)
			{
				ok = 0;
				break;
			}
		}
		printf("Case #%d: ",iT+1);
		if (!ok) printf("CRIME TIME\n");
		else
		{
			static char fr[MAXN][MAXID];
			memset(fr,1,sizeof(fr));
			for (i = N-1; i >= 0; i--)
			{
				if (data[i].id != 0)
				{
					int j;
					for (j = i; j >= 0; j--) fr[j][data[i].id] = 0;
				}
			}

			memset(b,0,sizeof(b));
			for (i = 0; i < N; i++)
			{
				if (data[i].id != 0)
				{
					if (data[i].type == 'E')
					{
						b[data[i].id] = i+1;
					}
					else
					{
						if (b[data[i].id] == 0)
						{
							int j = i-1;
							while (j >= 0)
							{
								if ((data[j].id == 0) && (data[j].type == 'E')) break;
								j--;
							}
							if (j >= 0) data[j].id = data[i].id;
						}
						b[data[i].id] = -(i+1);
					}
				}
			}

			memset(b,0,sizeof(b));
			for (i = 0; i < N; i++)
			{
				if (data[i].id != 0)
				{
					if (data[i].type == 'E')
					{
						b[data[i].id] = i+1;
					}
					else
					{
						b[data[i].id] = -(i+1);
					}
				}
				else
				{
					if (data[i].type == 'L')
					{
						//Try removing free person
						int j;
						for (j = 1; j < MAXID; j++)
						{
							if ((b[j] > 0) && (fr[i][j]))
							{
								b[j] = -(i+1);
								break;
							}
						}
					}
				}
			}

			memset(b,0,sizeof(b));
			for (i = 0; i < N; i++)
			{
				if (data[i].id != 0)
				{
					if (data[i].type == 'E')
					{
						b[data[i].id] = i+1;
					}
					else
					{
						if (b[data[i].id] > 0)
						{
							int l, r;
							l = b[data[i].id] - 1;
							r = i;
							int prevL = -1;
							int j;
							for (j = l; j <= r; j++)
							{
								if (data[j].id == 0)
								{
									if (data[j].type == 'E')
									{
										if (prevL != -1)
										{
											data[prevL].id = data[i].id;
											data[j].id = data[i].id;
											prevL = -1;
										}
									}
									else
									{
										if (prevL == -1)
										{
											prevL = j;
										}
									}
								}
							}
						}
						b[data[i].id] = -(i+1);
					}
				}
			}

			memset(b,0,sizeof(b));
			int res = 0;
			for (i = 0; i < N; i++)
			{
				if (data[i].id != 0)
				{
					if (data[i].type == 'E')
					{
						res++;
						b[data[i].id] = i+1;
					}
					else
					{
						if (b[data[i].id] > 0) res--;
						b[data[i].id] = -(i+1);
					}
				}
				else
				{
					if (data[i].type == 'L')
					{
						//Try removing free person
						int j;
						for (j = 1; j < MAXID; j++)
						{
							if ((b[j] > 0) && (fr[i][j]))
							{
								res--;
								b[j] = -(i+1);
								break;
							}
						}
					}
					else
					{
						int j;
						for (j = 1; j < MAXID; j++)
						{
							if ((b[j] <= 0) && (fr[i][j]))
							{
								res++;
								b[j] = i+1;
								break;
							}
						}
					}
				}
			}

			printf("%d\n",res);
		}
	}
	return 0;
}
