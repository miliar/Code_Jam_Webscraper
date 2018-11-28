#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
     
int main() {
    int T;
    cin>>T;
    for(int i=0;i<T;i++)
    {
    	char s[101];
    	cin>>s;
    	int l=strlen(s);
    	int c=0;
    	for(int j=0;j<l-1;j++)
    	{
    		if(s[j]=='+' && s[j+1]=='-')
    		{
    			c++;
    		}
    		else if(s[j]=='-' && s[j+1]=='+')
    		{	
    			c+=1;
    		}
    	}
    	if(s[l-1]=='-')
    		c++;
    	cout<<"Case #"<<i+1<<": "<<c<<"\n";
    }
    return 0;
}