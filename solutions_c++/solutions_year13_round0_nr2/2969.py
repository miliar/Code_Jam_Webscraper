#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,m,n;
	cin>>t;
	int a[101][101];
	for(int c = 1; c <= t; ++c)
	{
		cin>>m>>n;
		for(int i = 0; i < m; ++i)
		    for(int j = 0; j < n; ++j)
		        cin>>a[i][j];
        bool bi = 0,bj = 0;
		for(int i = 0; i < m && !bj; ++i)
		    for(int j = 0; j < n && !bj; ++j)
		    {
				int ii,jj;
				bi = 0,bj = 0;
				for(jj = 0; jj < n; ++jj)
				{
						if(a[i][jj] > a[i][j])
						{
							bi = 1;
							break;
						}
				}
				if(bi)
				{
					for(ii = 0; ii < m; ++ii)
					{
							if(a[ii][j] > a[i][j])
							{
								bj = 1;
								cout<<"Case #"<<c<<": NO"<<endl;
								break;
							}
					}
				}
			}
		if(!bj)
		    cout<<"Case #"<<c<<": YES"<<endl;
	}
	//system("pause");
	return 0;
}
