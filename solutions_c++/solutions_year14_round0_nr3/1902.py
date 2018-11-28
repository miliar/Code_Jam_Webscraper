#include<iostream>
#include<cstring>
#include<cstdlib>
#include<cmath>

using namespace std;

int r, c, m;
int che;

bool check()
{
	if (r == 1 || c == 1)
	{
		che = 1;
		if (r*c - m >= 1)
			return true;
	}
	else if (r == 2 || c == 2)
	{
		che = 2;
		if ((r*c - m == 1) || ((r*c - m >= 4) && (!((r*c - m) % 2))))
			return true;
	}
	else
	{
		che = 3;
		if (r*c - m == 1)
			return true;
		else if ((r*c - m >=4) && ((!((r*c - m) % 2)) || (r*c - m >= 9)))
			return true;
	}
	return false;
}

void output()
{
	int rest;
	int row, col;
	int tmp, tmp2;
	bool first = true;
	putchar('c');

	if (che == 1)           //che==1
	{
		rest = r*c - m - 1;
		if (r == 1)
		{
			for (col = 1; col < c; col++)
			{
				if (rest)
				{
					rest--;
					putchar('.');
				}
				else
					putchar('*');
			}
			putchar('\n');
		}
		else
		{
			putchar('\n');
			for (row = 1; row < r; row++)
			{
				if (rest)
				{
					rest--;
					puts(".");
				}
				else
					puts("*");
			}
		}
	}
	else if (che == 2)      //che==2
	{
		if ((r*c - m) == 1)
			for (first = true, row = 0; row < r; row++)
			{
				for (col = 0; col < c; col++)
				{
					if (first)
					{
						first = false;
						continue;
					}
					putchar('*');
				}
				putchar('\n');
			}
		else
		{
			rest = (r*c - m) / 2;
			if (r == 2)
			{
				for (first = true, row = 0; row < r; row++)
				{
					for (col = 0; col < c; col++)
					{
						if (first)
						{
							first = false;
							continue;
						}
						if (col < rest)
							putchar('.');
						else
							putchar('*');
					}
					putchar('\n');
				}
			}
			else if (c == 2)
			{
				puts(".");
				for (row = 1; row < r; row++)
				{
					if (row < rest)
						puts("..");
					else
						puts("**");
				}
			}
		}
	}
	else if (che == 3)    //che==3
	{
		if ((c == 3) && (m == 2))
		{
			tmp = (3 * r - 6) / 3;
			puts("..");
			for (row = 1; row < tmp; row++)
				puts("...");
			puts("..*");
			puts("..*");
		}
		else
		{
			if (!((r*c - m) % 2))
			{
				if ((r*c - m) / 2 <= c)
				{
					rest = (r*c - m) / 2;
					for (row = 0; row < r; row++)
					{
						for (col = 0; col < c; col++)
						{
							if (first)
							{
								first = false;
								continue;
							}
							if ((row < 2) && (col < rest))
								putchar('.');
							else
								putchar('*');
						}
						putchar('\n');
					}
				}
				else
				{
					for (row = 0; row < 2; row++)
					{
						for (col = 0; col < c; col++)
						{
							if (first)
							{
								first = false;
								continue;
							}
							putchar('.');
						}
						putchar('\n');
					}
					rest = r*c - m - 2 * c;
					while (rest / (2 * c))
					{
						for (tmp = 0; tmp < 2; tmp++, row++)
						{
							for (col = 0; col < c; col++)
								putchar('.');
							putchar('\n');
						}
						rest -= 2 * c;
					}
					if (rest == (c + 1))
					{
						for (col = 0; col < c - 1; col++)
							putchar('.');
						puts("*");
						cout << "..";
						row++;
						for (col = 2; col < c; col++)
							putchar('*');
						putchar('\n');
						row++;
						for (; row < r; row++)
						{
							for (col = 0; col < c; col++)
								putchar('*');
							putchar('\n');
						}
					}
					else
					{
						for (; row < r; row++)
						{
							for (col = 0; col < c; col++)
							{
								if (rest)
								{
									rest--;
									putchar('.');
								}
								else
									putchar('*');
							}
							putchar('\n');
						}
					}
				}
			}
			else
			{
				if ((r*c - m) == 1)
					for (first = true, row = 0; row < r; row++)
					{
						for (col = 0; col < c; col++)
						{
							if (first)
							{
								first = false;
								continue;
							}
							putchar('*');
						}
						putchar('\n');
					}
				else
				{
					rest = r*c - m;
					if (rest <= 2 * c + 1)
					{
						tmp = (rest - 3) / 2;
						for (first = true, row = 0; row < 2; row++)
						{
							for (col = 0; col < c; col++)
							{
								if (first)
								{
									first = false;
									continue;
								}
								if (col < tmp)
									putchar('.');
								else
									putchar('*');
							}
							putchar('\n');
						}
						cout << "...";
						for (col = 3; col < c; col++)
							putchar('*');
						putchar('\n');
						row++;
						for (; row < r; row++)
						{
							for (col = 0; col < c; col++)
								putchar('*');
							putchar('\n');
						}
					}
					else
					{
						for (first = true, row = 0; row < 2; row++)
						{
							for (col = 0; col < c; col++)
							{
								if (first)
								{
									first = false;
									continue;
								}
								putchar('.');
							}
							putchar('\n');
						}
						rest = r*c - m - 2 * c;
						while (((rest / (2 * r)) - 1) > 0)
						{
							for (tmp = 0; tmp < 2; tmp++, row++)
							{
								for (col = 0; col < c; col++)
									putchar('.');
								putchar('\n');
							}
							rest -= 2 * c;
						}
						if (rest < col)
						{
							for (col = 0; col < c; col++)
							{
								if (rest)
								{
									putchar('.');
									rest--;
								}
								else
									putchar('*');
							}
							putchar('\n');
							row++;
							for (; row < r; row++)
							{
								for (col = 0; col < c; col++)
									putchar('*');
								putchar('\n');
							}
						}
						else
						{
							if (rest == c + 1)
							{
								for (col = 0; col < c - 1; col++)
									putchar('.');
								puts("*");
								row++;
								cout << "..";
								for (col = 2; col < c; col++)
									putchar('*');
								putchar('\n');
								row++;
								for (; row < r; row++)
								{
									for (col = 0; col < c; col++)
										putchar('*');
									putchar('\n');
								}
							}
							else if (rest == 2 * c + 1)
							{
								tmp = (rest - 3) / 2;
								for (tmp2 = 0; tmp2 < 2; row++, tmp2++)
								{
									for (col = 0; col < c; col++)
									{
										if (col < tmp)
											putchar('.');
										else
											putchar('*');
									}
									putchar('\n');
								}
								cout << "...";
								for (col = 3; col < c; col++)
									putchar('*');
								putchar('\n');
								row++;
								for (; row < r; row++)
								{
									for (col = 0; col < c; col++)
										putchar('*');
									putchar('\n');
								}
							}
							else
							{
								for (; row < r; row++)
								{
									for (col = 0; col < c; col++)
									{
										if (rest)
										{
											rest--;
											putchar('.');
										}
										else
											putchar('*');
									}
									putchar('\n');
								}
							}
						}
					}
				}
			}
		}
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int count, counttmp;
	cin >> count;
	for (counttmp = 0; counttmp < count; counttmp++)
	{
		cin >> r;
		cin >> c;
		cin >> m;
		printf("Case #%d:\n", counttmp + 1);
		if (check())
			output();
		else
			puts("Impossible");
	}
	return 0;
}