#include<iostream>
#include<string>
#include<vector>
#include<cstring>
#include<algorithm>
#include <iomanip>
#include<cmath>
#include<map>
#include <sstream>
using namespace std;

#define PB push_back
#define F0(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define FORE(i,x) for( auto i=(x).begin();i != (x).end();++i)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,w) memset((x),w,sizeof (x))
#define X first
#define Y second
//////////////////////////////////////////////////

void display()
{

}

long double A,B;
long double r;
string sr,s,rv;
long long c;
void getvs(int v)
{
  
  switch(v)
  {
  
   case 0:
     rv= "0";
	 break;
   case 1:
     rv= "1";
	 break;
	 case 2:
     rv= "2";
	 break;
	 case 3:
     rv= "3";
	 break;
	 case 4:
     rv= "4";
	 break;
	 case 5:
     rv= "5";
	 break;
	 case 6:
     rv= "6";
	 break;
	 case 7:
     rv= "7";
	 break;
	 case 8:
     rv= "8";
	 break;
	 case 9:
     rv= "9";
	 break;
   }
   //return rv;
}

int checkp(long double v)
{
  s="";
  int j=0;
  s.clear();
   sr.clear();
  while( !(v<1))
  {
    getvs((int)v%10);
    s+= rv;
	
	v=v/10;
  }
   j=0;
  
  //s.shrink_to_fit();
  
  for(int i=s.length()-1;i>=0;i--)
   sr.push_back(s[i]);
   
  //cout<<s<<" == "<<sr<<" - "<<s.length()<<endl;
  if(sr==s)
   return 1;
   else
   return 0;
   
   
}
int main()
{
  int T;
  cin>>T;
  FOR(i,1,T)
  {
    c=0;
    cin>>A>>B;
	//cout<<A<<B;
	for(long double a=A;a<=B;a++)
	{
	  //cout<<endl<<a<<endl;
	   if(checkp(a))
	   {
	     //long double r;
		 long long r;
	     r=(long long)sqrt(a);
		 if( (long double)r*r == a)
		 {
		  if(checkp(r))
		  c++;
		 }
	  }
	}
	 cout<<"Case #"<<i<<": "<<c<<endl;
	}
    

return 0;
}