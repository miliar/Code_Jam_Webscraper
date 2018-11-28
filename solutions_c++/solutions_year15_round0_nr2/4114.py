#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <climits>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <utility>
#include <cstring>
#include <list>
#include <stack>
#include <cmath>
#include <fstream>

using namespace std;

int a[10000];

int main()
{
    ofstream myfile ;
    myfile.open("s007.txt") ;
	int t,k=1;
	scanf("%d",&t);
	while(t--)
	{
		int ma=0,n;
		scanf("%d",&n);
		for(int i=1;i<=n;i++)
		{
			scanf("%d",&a[i]);
			ma=max(ma,a[i]);
		}
		int sum=ma;
		for(int i=1;i<=ma;i++)
		{
			int temp=0,smax=0;
			for(int j=1;j<=n;j++)
			{
				if(a[j]>i)
				{
					temp += (a[j] / i)+((a[j]%i==0)?0:1)-1;
					smax=max(smax,i);
				}
				else smax=max(smax,a[j]);
			}
			temp+=smax;
			if(temp<sum)sum=temp;
		}
		myfile <<"Case"<<" "<<"#"<<k<<":"<<" "<< sum << endl;

		k++ ;
	}
	return 0;
}
