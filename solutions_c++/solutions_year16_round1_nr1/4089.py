#include <iostream>
#include<malloc.h>
using namespace std;




int main() {
	int T=0;
  int fin=0;
	string s= "";

	int pos=0;
	cin>>T;
	for(int i= 1;i<=T;i++)
	{
	    cin>>s;
	    char *f = (char *)malloc(s.length()*sizeof(char));
	    pos=0;
	    for(int j=0;j<s.length();j++)
	    {
	        if(pos ==0)
	        {
	              f[0] =  s[j];  
	              pos++;
	        }
	        else
	        {
	            if(s[j] >= f[0])
	            {
	                fin = pos;
	                while(fin!=0)
	                {
	                    f[fin] = f[fin -1];
	                    fin--;
	                }
	                f[0] = s[j];
	                pos++;
	            }
	            else
	            {
	                f[pos] = s[j];  
	                pos++; 
	            }
	          //  cout<<f<<" ";
	        }
	    
	    }
	    f[pos]='\0';
	      cout<<"Case #"<<i<<": "<<f<<endl;

	}
	return 0;
}
