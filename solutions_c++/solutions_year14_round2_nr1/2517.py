#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <stdlib.h>

#define INF 1000000015

using namespace std;

string str1[101], str2[101];
int str3[101][101];
int N, numb;
int compare(int i,int j)
{
	int t=0;
	for (int k=0; k<=numb; ++k)
	{
		t+=abs(str3[i][k]-str3[j][k]);
//		cout<<abs(str3[i][k]-str3[j][k])<< " ";
	}
//	cout<<endl;
	return t;
}

int main()
{	
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T, t, i, j, s, min;
	char buff[9];
	bool checker;
	scanf("%d", &T);
	for(t=0; t<T; ++t)
	{
		scanf("%d", &N);
		for (i=0; i<N; ++i)
		{

			cin>>str1[i];
			str2[i]=str1[i][0];
			int k=1;
			int pos=0;
			for (j=1; j < (str1[i]).length(); ++j)
			{
				if (str1[i][j]!=str1[i][j-1])
				{
					str2[i]+=str1[i][j];
					str3[i][pos]=k;
					k=1;
					++pos;
				} else
					++k;
			}
			
				str3[i][pos]=k;
				numb=pos;
		}
		checker=false;
		for (i=1; i<N; ++i)
			if (str2[i].compare(str2[0]))
				checker=true;
		printf("Case #%d: ",t+1);
		if (checker)
		{
			printf("Fegla Won\n");
		}
		else
		{
			min=INF;
			for (i=0; i<N; ++i)
			{
				s=0;
				for (j=0; j<N; ++j)
					if (i!=j)
					{
						s+=compare(i, j);
					}
				if (s<min)
					min=s;
//				cout<<str1[i]<<endl<<str2[i]<<endl<<min<<endl<<s<<endl<<endl;
			}
			
			printf("%d\n", min);
		}

	}	

	return 0;
}