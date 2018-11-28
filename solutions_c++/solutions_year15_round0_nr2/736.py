#include <iostream>
#include <fstream>
#include <iomanip>
#include <math.h>
#include <limits.h>
#include <algorithm>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <string>
#include <string.h>
#include <sstream>
#include <ctime>
 
using namespace std;
 
typedef long long ll;
typedef unsigned long long ull;


int res,cases,d,sp,maxi,p[1010];
int main()
{
	std::ios::sync_with_stdio(false);
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	cin>>cases;
	for(int kase=1;kase<=cases;kase++)
	{
		cin>>d;
		maxi=0;
		for(int i=1;i<=d;i++)
		{
			cin>>p[i];
			if(p[i]>maxi)
			{
				maxi=p[i];
			}
		}
		res=maxi;
		for(int i=1;i<=maxi;i++)
		{
			sp=0;
			for(int j=1;j<=d;j++)
			{
				if(p[j]>i)
				{
					sp+=(p[j]-i)/i;
					if((p[j]-i)%i!=0)sp++;
				}
			}
			if(sp+i<=res)
			{
				res=sp+i;
			}
		}
		cout<<"Case #"<<kase<<": "<<res<<"\n";
	}
	return 0;
}