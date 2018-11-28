#include<iostream>
#include<vector>
#include<stdio.h>
#include<algorithm>
#include<set>
#include<math.h>
#include<string.h>
#include<map>
#define all(c) c.begin(), c.end()
#define tr(container, it) for(typeof(container.begin())it=container.begin();it!=container.end();it++)
#define sz(a) int((a).size()) 
#define pb push_back
#define present(c,x) ((c).find(x)!=(c).end()) 
#define cpresent(c,x) (find(all(c),x)!=(c).end())
using namespace std;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef set<int> si;
typedef map<int,int> mi;
typedef long long int lli;

int main()
{
	int t,n,m,i,j,k,flag=0,cnt=0;
	scanf("%d",&t);
	for(j=1;j<=t;j++)
	{
		mi m;
		scanf("%d",&n);
		int N=n;
		int c=0;
		if(n==0)
		{
			cout<<"Case #"<<j<<": INSOMNIA\n";
			continue;
		}
		i=1;
		while(true)
		{
			int temp=n;
			while(temp!=0)
			{
				int d=temp%10;
				temp=temp/10;
				m[d]=1;
			}
			i++;
			n=N*i;
			int sum=0;
			tr(m,it)
			{
				//cout<<it->first<<":"<<it->second<<endl;
				sum=it->second+sum;
			}
			if(sum==10)
				break;
			//cout<<c<<endl;
		}
		//tr(m,it)
			//cout<<it->first<<": "<<it->second<<endl;
		printf("Case #%d: %d\n",j,(n-N));
	}
}

