#include <fstream>
#include <string>

using namespace std;

ifstream cin("B-large.in");
ofstream cout("pancakes.out");

long long T,rs;
int i,a,k2,k1;
string s;

int main()
{
	cin>>T;
	for(int j=1; j<=T; ++j)
	{
		rs=0;
		k2=0;
		k1=0;
		cin>>s;
		a=s.length();
		if(s[0]=='+')
		{
			i=0;
		   while(i<a)
		   {
		   	    k1=0;
		   	    k2=0;
		         while(s[i]=='+' && i<a)
				 {
		             k1++;
		             i++;
		         }
		         if(i<a && s[i]=='-' && k1)rs++;
		         
				 while(s[i]=='-' && i<a)
				 {
		             i++;
		             k2++;
		         }
		         if(k2)rs++;
		   }
		
	    }
	    else
	    {
	       
	       i=0;
		   while(i<a)
		   {
		   	    k1=0;
		   	    k2=0;
		         while(s[i]=='-' && i<a)
				 {
		             i++;
		             k2++;
		         }
		         if(k2)rs++;
		         
		         while(s[i]=='+' && i<a)
				 {
		             k1++;
		             i++;
		         }
		         if(i<a && s[i]=='-' && k1)rs++;
		         
		   }
		  
		   //if(s[a-1]=='-') rs++;
		}
		
		cout<<"case #"<<j<<": "<<rs<<endl;
	}
return 0;
}
