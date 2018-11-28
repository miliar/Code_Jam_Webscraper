#include<bits/stdc++.h>
using namespace std;

int main()
{
    string str,s=" ";
    int t;
    cin>>t;
    for(int k=1;k<=t;k++)    
    	{
    		cin>>str;
    int len=str.length();
    s[0]=str[0];
    for(int i=1;i<len;i++)
    {
        if(str[i]<s[0])
           s=s+str[i];
        else if(str[i]>=s[0])
            s=str[i]+s;
    }
    cout<<"Case #"<<k<<": "<<s<<endl;
    s={'\0'};
}
	return 0;
}