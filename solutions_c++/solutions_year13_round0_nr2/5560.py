#include <stdio.h>

int main()
{
	int ar[110][110];
	int t,n,m;
	int cut_row,cut_col,min;
	bool good_row,good_col;
	bool check_empty;
	bool empty_col[110],empty_row[110];

	scanf("%d",&t);

	for (int i=0;i<t;i++)
	{
		scanf("%d %d",&m,&n);
		for (int j=0;j<m;j++) empty_row[j]=false;
		for (int j=0;j<n;j++) empty_col[j]=false;

		for (int j=0;j<m;j++)
		{
			for (int k=0;k<n;k++)
			{
				scanf("%d",&ar[j][k]);
			}
		}
		while(true)
		{
			good_row=good_col=false;
			cut_row=cut_col=-1;
			check_empty=true;

			for (int j=0;j<m;j++)
			{
				for (int k=0;k<n;k++)
				{
					if (ar[j][k]!=-1)
					{
						check_empty=false;
						break;
					}
				}
				if (check_empty==false) break;
			}

			if (check_empty==true)
			{
				printf("Case #%d: YES\n",i+1);
				break;
			}
			else
			{
				min = 10000;
				for (int j=0;j<m;j++)
				{
					for (int k=0;k<n;k++)
					{
						if (min>ar[j][k] && ar[j][k]!=-1) min=ar[j][k];
					}
				}

				//check row
				for (int j=0;j<m;j++)
				{
					if (empty_row[j]==true) continue;
					good_row=true;
					for (int k=0;k<n;k++)
					{
						if (ar[j][k]>min)
						{
							good_row=false;
							break;
						}
					}
					if (good_row==true)
					{
						empty_row[j]=true;
						cut_row=j;
						break;
					}
				}

				if (good_row==true)
				{
					for (int k=0;k<n;k++)
					{
						ar[cut_row][k] = -1;
					}
					continue;
				}

				//check column
				for (int k=0;k<n;k++)
				{
					if (empty_col[k]==true) continue;
					good_col = true;
					for (int j=0;j<m;j++)
					{
						if (ar[j][k]>min)
						{
							good_col=false;
							break;
						}
					}
					if (good_col==true)
					{
						empty_col[k]=true;
						cut_col = k;
						break;
					}
				}

				if (good_col==true)
				{
					for (int j=0;j<m;j++)
					{
						ar[j][cut_col]=-1;
					}
					continue;
				}


				if (good_row==false && good_col==false)
				{
					printf("Case #%d: NO\n",i+1);
					break;
				}
			}
		}
	
	}

	return 0;
}