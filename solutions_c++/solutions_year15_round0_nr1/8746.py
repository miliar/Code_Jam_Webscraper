#include<iostream>
#include<fstream>

using namespace std ;
int main()
{   fstream f;
  fstream c;
       
   f.open("myfile.txt");
    c.open("urfile.txt");
   
	int t;
	f>>t;
	 for(int p=1;p<=t;p++)
	{
		int n;
		f>>n;
		int sum=0,ans=0;
		char ch[n+2];
		f>>ch;
		  sum=ch[0]-48;
		  for(int i=1;i<=n;i++)
		  {
		  	if(sum<i)
		  	{
		  	 ans++;
		  		sum= sum+ ch[i]-48+1;
			  }
			  else
			  {
			  	sum= sum+ ch[i]-48;
			  }
		  }
		  
		  c<<"Case #"<<p<<": "<<ans<<endl;
		  	
		
	}
}
