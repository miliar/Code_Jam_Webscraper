#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define  get(a) scanf("%lld", &a)
#define  out(a) printf("%lld", a)
ll i,j,k,x,y,z;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("16Al.out","w",stdout);
ll t;
cin>>t;
for(i=1;i<=t;i++)
{ ll cnt=0; map<ll,bool> M;
	cin>>x;
	if(x==0)
	{
		cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		continue;
	}
	j=1;
	while(cnt<10)
	{
		k=j*x;
		while(k)
		{
			if(M[k%10]==0)
			{
				M[k%10]=1;
				cnt++;
			}
		k/=10;	
		}
		j++;
	}
cout<<"Case #"<<i<<": "<<(j-1)*x<<endl;
}

   return 0;

}


