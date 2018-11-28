#include <bits/stdc++.h>
#define ll long long
#define mp make_pair
#define pb push_back
#define try1(a) cout<<a<<endl;
#define try2(a,b) cout<<a<<" "<<b<<" "<<endl;
#define try3(a,b,c) cout<<a<<" "<<b<<" "<<c<<endl;
#define try4(a,b,c,d) cout<<a<<" "<<b<<" "<<c<<" "<<d<<endl;
 
 
 
using namespace std;
 
int main() {

freopen("inp3.txt","r",stdin);

freopen("out3.txt","w",stdout);
ll t;
cin>>t;
ll k1=0;
while(t--)
{
k1++;

ll x,r,c;
cin>>x>>r>>c;

if(x==1)
{
   
   cout<<"Case #"<<k1<<": "<<"GABRIEL"<<endl;


}
else if(x==2)
{
   if((r*c%2)==0)
       cout<<"Case #"<<k1<<": "<<"GABRIEL"<<endl;
     
     else
     	   cout<<"Case #"<<k1<<": "<<"RICHARD"<<endl;

     
}
else if(x==3)
{
	if((r*c)%3!=0 || (r*c)==3)
		   cout<<"Case #"<<k1<<": "<<"RICHARD"<<endl;
		else
		{
            cout<<"Case #"<<k1<<": "<<"GABRIEL"<<endl;


		}


}
else if(x==4)
{

	if((r*c)>=12)
		   cout<<"Case #"<<k1<<": "<<"GABRIEL"<<endl;
else
	   cout<<"Case #"<<k1<<": "<<"RICHARD"<<endl;



}



}




return 0;
}