#include<iostream>
using namespace std;
#define llu long long int
llu t,a,b;
string s;
void getint()
{
	a=0,b=0;
	int i=0;
	while(s[i]!='/')
	{
		a=a*10+s[i]-'0';
		i++;
		//cout<<i<<endl;
	}
	i++;
	while(i<s.size())
	{
		b=b*10+s[i]-'0';
		i++;
		//cout<<i<<endl;
	}
}
llu gcd (llu a,llu b)
{
	if(b==0)return a;
	else return gcd(b,a%b);
}
int main()
{
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>s;
	//	cout<<"yes"<<endl;
		getint();
	//	cout<<a<<" "<<b<<endl;
		int c=0,ans=100,ch=0;
		while(c<=40)
		{
			llu k=gcd(a,b);
			a/=k;
			b/=k;
			if(a>b){a-=b;ans=min(ans,c);}
			else if(b>a)a*=2;
			else {ans=min(ans,c);ch=1;break;}
			c++;
		}
		if(!ch)cout<<"Case #"<<i<<": impossible"<<endl;
		else cout<<"Case #"<<i<<": "<<ans<<endl;

	}

}