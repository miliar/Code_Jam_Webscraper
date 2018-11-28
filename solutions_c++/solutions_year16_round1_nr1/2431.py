#include <iostream>
#include<string>
using namespace std;

int main() {
	int t,j,len=0;
	string s="\0",i;
	char c;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
	    s="\0";
	    cin>>i;
	    len=i.length();
	    for(j=0;j<len;j++)
	    {
	    c=i[j];
	    if(s=="\0")
	        s=s+c;
	   else
	   {
	       if(c>=s[0])
	       s=c+s;
	       else
	       s=s+c;
	   }
	    }
	    s[j]='\0';
	    cout<<"Case #"<<k<<": "<<s<<endl;
	}
	return 0;
}