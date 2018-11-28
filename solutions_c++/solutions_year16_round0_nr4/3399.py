#include<bits/stdc++.h>
#define scan(n) scanf("%d",&n)
#define scanll(n) scanf("%lld",&n)
#define For(i,a,b) for(i=a;i<b;i++)
#define fill(a,b) memset(a,b,sizeof(a))
#define swap(a,b) a=a+b;b=a-b;a=a-b;
#define ll long long int
#define pb push_back
#define MAX 1000000007
#define f_in(st) freopen(st,"r",stdin);
#define f_out(st) freopen(st,"w",stdout);
using namespace std;
int main()
{
//	f_in("D-small-attempt1.in");
//	f_out("D-small-attempt1out.txt");
	int test,t;
	scan(test);
	for(t=1;t<=test;t++)
	{
		int i,k,c,s;
		scan(k);
		scan(c);
		scan(s);
		if(c==1)
		{
			if(s<k)
				cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
			else
			{
				cout<<"Case #"<<t<<": ";
				for(i=1;i<=k;i++)
				{
					cout<<i<<" ";	
				}	
				cout<<endl;
			}	
		}
		else
		{
			if(s<k-1)
				cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
			else{
			
			cout<<"Case #"<<t<<": ";
			if(k==1)
			cout<<"1";
			for(i=2;i<=k;i++)
			{
				cout<<i<<" ";
			}
			cout<<endl;
			}
		}		
	}
 	return 0;
}


