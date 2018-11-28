#include<iostream>
#include<map>
#include<vector>
#include<string>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<fstream>
#include<iomanip>
#include<set>
#include<cstdio>
using namespace std;
//pandey


long long int gcd ( long long int a,long long int b )
{
  long long int c;
  while ( a != 0 ) {
     c = a; a = b%a;  b = c;
  }
  return b;
}
int main()
{
	//ios_base::sync_with_stdio(false);
	freopen("A-large.in","r",stdin);
	freopen("A-large-ans.txt","w",stdout);
	
	int t;
	cin>>t;
	
	int count=1;
	
	while(t-->0)
	{
		string s;
		cin>>s;
		unsigned  f =s.find("/");
		string a=s.substr(0,f);
		string b=s.substr(f+1);
		
		
		long long int p=0,q=0;
		for(int i=0;i<a.length()-1;i++)
		{
			p=(p+((int)a[i]-48))*10;
			
			
		}
		p=p+(int)a[a.length()-1]-48;
		
		for(int i=0;i<b.length()-1;i++)
		{
			q=(q+((int)b[i]-48))*10;
			
			
		}
		q=q+(int)b[b.length()-1]-48;
		
		long long int common=gcd(p,q);
		
		p=p/common;
		q=q/common;
		//cout<<p<<"  "<<q;
		
		
		long long int calc=0;
		
		int imp=0;
		int tot=1;
		
		
		
		//if(q%2!=0)
		//imp=1;
		
		
		if((q%p==0)&&!( !((q/p) == 0) && !((q/p) & ((q/p) - 1)))) 
		imp=1;
		if((q%p!=0)&&!( !((q) == 0) && !((q) & ((q) - 1))))
		imp=1;
		/*while(2*p<(q))
		{
			p=p*2;
			 common=gcd(p,q);
		
		p=p/common;
		q=q/common;
		//cout<<p<<"    "<<q<<endl;
		if(q%2!=0)
		{
		imp=1;
		break;
		}
		
		calc++;
		}
		*/
	/*	while(q>=p)
		{
			q=q/2;
			calc++;
			if(q!=p&&q%2!=0)
			imp=1;
		}
		
	*/
	
	int cnt=0;
	long long int sp;
	if(q%p==0)
	{  sp=q/p;
	   while(sp!=1)
	   {
	   	 sp=sp/2;
	   	 calc++;
	   }
 
	}
    else
    {
    while(q>=p)
	   {
	   	 q=q/2;
	   	 calc++;
	   }	
    }
	
		
	/*	if(2*p>=q)
		{
			while(p>=0)
			{
				p=2*p-q;
				
			//common=gcd(p,q);
		
		//p=p/common;
		//q=q/common;
				tot++;
			}
			
			
		}
	*/	
		if(imp==0&&calc<=40)
		cout<<"Case #"<<count<<": "<<calc;
		else
		cout<<"Case #"<<count<<": "<<"impossible";
		
		cout<<endl;
		count++;
	}
 
 
 
 
}



