#include<stdio.h>
#include<iostream>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<iomanip>
#include<fstream>
using namespace std;
#define getchar_unlocked getchar
#define ll long long int
inline long long int in()
{
   long long int n=0;
   long long int ch=getchar_unlocked();
   long long int sign=1;
   while( ch < '0' || ch > '9' )
   {
   	if(ch=='-')sign=-1; ch=getchar_unlocked();
	   }
 
   while(  ch >= '0' && ch <= '9' )
           n = (n<<3)+(n<<1) + ch-'0', ch=getchar_unlocked();
   return n*sign;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("Problem_b_large_output.txt","w",stdout);
	ll n;
	cin>>n;
	for(int t=1;t<=n;t++)
	{	
		double c,f,x,nor=2.0,extra,old,news;
		cin>>c>>f>>x;
		old=x/nor;
		extra=c/nor;
		nor+=f;
		news=extra+(x/nor);
		//cout<<"old:"<<old<<"new:"<<news<<"\n";
		//ll ct=0;
		while(old>news)
		{
		//	if(ct==5)
		//	break;
			old=news;
			news=0;
			extra+=c/nor;
			nor+=f;
			news+=extra+(x/nor);
		//	cout<<"old:"<<old<<"new:"<<news<<"\n";
		//	ct++;
		}
		cout<<"Case #"<<t<<": "<<fixed<<setprecision(7)<<old<<"\n";
	}

}
