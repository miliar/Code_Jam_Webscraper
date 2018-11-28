#include<iostream>
#include<cstdio>
#include<sstream>
#include<string>
#include<cstdlib>
using namespace std;

int main()
{
	int t,n,m,matrix[100][100],k=0,j,i,max_row[100],max_col[100];
	string str;
	getline(cin,str);
	t = atoi(str.c_str());
	stringstream ss;
	bool flag;
	while(t--)
	{
		k++;
		getline(cin,str);
		ss << str;
		ss >> n >> m;
		ss.clear();
		for(i=0;i<n;i++)
		{
			getline(cin,str);
			ss << str;
			for(j=0;j<m;j++)
			{
				ss >> matrix[i][j] ;
			}
			ss.clear();
		}
		for(i=0;i<n;i++)
		{
			max_row[i] = 0;
			for(j=0;j<m;j++)
				max_row[i] = (max_row[i] > matrix[i][j]) ? max_row[i] : matrix[i][j] ;
		}
		for(j=0;j<m;j++)
		{
			max_col[j] = 0;
			for(i=0;i<n;i++)
				max_col[j] = (max_col[j] > matrix[i][j]) ? max_col[j] : matrix[i][j] ;
		}
		flag = true;
		for(i=0;i<n;i++)
			for(j=0;j<m;j++)
				if((matrix[i][j] < max_row[i]) && (matrix[i][j] < max_col[j]))
					flag = false;
		if(flag)
			printf("Case #%d: YES\n",k);
		else
			printf("Case #%d: NO\n",k); 
	}
	return 0;
}
