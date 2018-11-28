#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <ctime>
using namespace std;
typedef long long LL;
#define S(n) scanf("%d",&n);
#define LS(n) scanf("%lld",&n);
#define P(n) printf("%d\n",n);
#define LP(n) printf("%lld\n",n);
#define MOD 10000007

int main() 
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t,a,b,n,i,l;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		cin>>n;
		string a,b;
		cin>>a;
		cin>>b;
		//cout<<a<<"  "<<b<<endl;
		int l1=a.size();
		int l2=b.size();
		int cnt=0,j=0;
		i=0;
		bool flag=true;
		while(i<l1&&j<l2&&flag)
		{
			if(a[i] != b[j])
			{
				if(i>0 && a[i-1]==a[i])
				{
					while(i<l1 && a[i-1] == a[i])
					{
						i++;
						cnt++;
					}
				}
				else if(b[j-1] == b[j])
				{
					while(j<l2 && b[j-1] == b[j])
					{
						j++;
						cnt++;
					}
				}

				if(a[i]!=b[j])
					flag=false;
			}
			i++;j++;
			if(i==l1&&flag)
			{
				while(j<l2 && a[i-1]==b[j])
				{
					j++;
					cnt++;
				}
				if(j!=l2)
					flag=false;
			}
			else if(j==l2&&flag)
			{
				while(i<l1 && a[i]==b[j-1])
				{
					i++;
					cnt++;
				}
				if(i!=l1)
					flag=false;
			} 
		}
		if(flag)
			printf("Case #%d: %d\n",k,cnt);
		else
			printf("Case #%d: Fegla Won\n",k);
	}
	fclose (stdout);
	fclose (stdin);
	return 0;
}
