#include<iostream>
#include<string.h>
using namespace std;
int main()
{
	string s_in[100],s_out[100];
	char temp;
	int t;
	cin>>t;
	for(int j=0;j<t;j++)
   {

	 cin>>s_in[j];
	 s_out[j]=s_in[j];
 	
	for(int i=1;i<s_in[j].size();i++)
     {
		if(int(s_out[j][0])>int(s_in[j][i]))
		 { 
		 	s_out[j][i]=s_in[j][i];	
		 }
		else
		  { temp=s_in[j][i];		
		  	s_out[j]=temp+s_out[j];			 		 
		  }
	 }
	 
    }
    for(int j=0;j<t;j++)
	 { cout<<"Case #"<<j+1<<": ";	 
	   for(int i=0;i<s_in[j].size();i++)
	    cout<<s_out[j][i];
	   cout<<"\n"; 
     }
   
}   
