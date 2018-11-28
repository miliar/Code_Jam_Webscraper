#include<bits/stdc++.h>
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define scan(a) scanf("%d",&a)
#define scanl(a) scanf("%lld",&a)
#define print(a) printf("%d",a)
#define printl(a) printf("%lld",a)
#define MAX 10
using namespace std;

typedef pair<int,int>pii;
typedef long long LL;

bool cmp(const pii &left,const pii &right)
{
	return left.second<right.second;
}
int gcd(int a,int b)
{
	if(b==0)
	{
		return a;
	}
	else
		return gcd(b,a%b);
}
int main()
{
   	freopen("ind.in","r",stdin);
   	freopen("outd.out","w",stdout);
	int t,cc=1;
	scan(t);
	while(t--)
	{
		int x,r,c;
		scan(x);scan(r);scan(c);
		if(x==1)
			cout<<"Case #"<<cc++<<": GABRIEL"<<endl;
		else if(x==2)
		{
			if((r==1 && c==1) || (r==1 && c==3) || (r==3 && c==3) || (r==3 && c==1))
				cout<<"Case #"<<cc++<<": RICHARD"<<endl;
			else
				cout<<"Case #"<<cc++<<": GABRIEL"<<endl;
		}
		else if(x==3)
		{
			if((r==2 && c==3) || (r==3 && c==2) || (r==3 && c==3) || (r==3 && c==4) || (r==4 && c==3))
				cout<<"Case #"<<cc++<<": GABRIEL"<<endl;
			else
				cout<<"Case #"<<cc++<<": RICHARD"<<endl;
		}
		else
		{
			if((r==3 && c==4) || (r==4 && c==3) || (r==4 && c==4))
				cout<<"Case #"<<cc++<<": GABRIEL"<<endl;
			else
				cout<<"Case #"<<cc++<<": RICHARD"<<endl;
		}
	}
	return 0;
}




