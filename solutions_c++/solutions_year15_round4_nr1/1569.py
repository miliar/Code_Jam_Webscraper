#include<cstdio>
#include<cstring>
#include<queue>
using namespace std;
char x[101][101];
int jizz[101][101];
int set[101][101];
int R,C,T;
int main()
{
		FILE *in =//stdin;
			fopen("in.txt","r");
		FILE *out =//stdout;
			fopen("out.txt","w");
		fscanf(in,"%d",&T);
		int t=0;
		while(T--)
		{
				t++;
				fscanf(in,"%d%d",&R,&C);
				for(int i=0;i<R;i++) fscanf(in,"%s",x[i]);
				for(int i=0;i<R;i++)
					for(int j=0;j<C;j++)
					{
						jizz[i][j] = 0;//1 can't up 2 can't down 3 can't ledt 4 can't right
						set[i][j] = 0;
					}
				int ans=0;
				bool ok=true;
				for(int i=0;i<C;i++)
				{
						for(int j=0;j<R;j++)
						{
								if(x[j][i] =='^')
								{
										if(set[j][i] == 0)ans++;
										jizz[j][i]++;
										set[j][i] = 1;
										x[j][i] = 'v';
										break;
								}
								else if(x[j][i]!='.')
								{
									jizz[j][i] ++;
									break;
								}
						}
						for(int j=R-1;j>=0;j--)
						{
								if(x[j][i] =='v')
								{
										if(set[j][i] == 0) ans++;
										set[j][i] = 1;
										jizz[j][i]++;
										x[j][i] = '<';
										break;
								}
								else if(x[j][i]!='.')
								{
									jizz[j][i]++;
									break;
								}
						}
				}
				for(int i=0;i<R;i++)
				{
						for(int j=0;j<C;j++)
						{
								if(x[i][j] =='<')
								{
										if(set[i][j] == 0)ans++;
										set[i][j] = 1;
										jizz[i][j]++;
										x[i][j] = '>';
										break;
								}
								else if(x[i][j]!='.')
								{
									jizz[i][j]++;
									break;
								}
						}
						for(int j=C-1;j>=0;j--)
						{
								if(x[i][j] =='>')
								{
										if(set[i][j] == 0)ans++;
										jizz[i][j]++;
										set[i][j] = 1;
										if(jizz[i][j] == 4) ok=false;
										break;
								}
								else if(x[i][j]!='.')
								{
									jizz[i][j]++;
									break;
								}
						}
				}
				if(!ok) fprintf(out,"Case #%d: IMPOSSIBLE\n",t);
				else fprintf(out,"Case #%d: %d\n",t,ans);
				/*if(x[0][0] =='^' || x[0][0] == '<') 
				if(x[0][C-1] == '^' || x[0][C-1] == '>') ans++;
				if(x[R-1][0] == 'v' || x[R-1][0] == '<') ans++;
				if(x[R-1][C-1] == 'v' || x[R-1][C-1] == '>') ans++;
				for(int i=1;i<C-1;i++) if(x[0][i] == '^') ans++;
				for(int i=1;i<C-1;i++) if(x[R-1][i] == 'v') ans++;
				for(int i=1;i<R-1;i++) if(x[i][0] == '<') ans++;
				for(int i=1;i<R-1;i++) if(x[i][C-1] == '>') ans++;*/
		}
}
