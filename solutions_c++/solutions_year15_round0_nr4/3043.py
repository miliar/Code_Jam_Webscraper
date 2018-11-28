#include <bits/stdc++.h>
using namespace std;
#define FOR(i,n) for (int i = 0; i < (int)(n); ++i)
#define mod 1000000007
#define bigger(a,b) (a>b?a:b)
#define smaller(a,b) (a<b?a:b)
#define mem(A,g) memset(A,g,sizeof(A))
#define positive(a) (bigger(a,-a))
int main() {
ios_base::sync_with_stdio(false); cin.tie(0);
int t;
cin>>t;
int y = t;
while(t--)
{
int x,r,c;
cin>>x>>r>>c;
long long count = r*c;
if(x==1)
{
	cout<<"Case #"<<y-t<<":"<<" "<<"GABRIEL"<<"\n";

}
else if(x==2)
{
	if(count%2==0)
	{
			cout<<"Case #"<<y-t<<":"<<" "<<"GABRIEL"<<"\n";
	}
	else
	{
			cout<<"Case #"<<y-t<<":"<<" "<<"RICHARD"<<"\n";
	}
}
else if(x==3)
{
	if(count%3==0 && ((r>=3&& c>=2)||((c>=3)&&(r>=2))))
	{
				cout<<"Case #"<<y-t<<":"<<" "<<"GABRIEL"<<"\n";

	}
	else
	{
			cout<<"Case #"<<y-t<<":"<<" "<<"RICHARD"<<"\n";
	}
}
else
{
	if(count%4==0 && ((r>=4&& c>=3)||((c>=4)&&(r>=3))))
	{
					cout<<"Case #"<<y-t<<":"<<" "<<"GABRIEL"<<"\n";
	}
	else
{
	cout<<"Case #"<<y-t<<":"<<" "<<"RICHARD"<<"\n";
}
}
}
return 0;
}
