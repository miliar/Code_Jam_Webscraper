#include <bits/stdc++.h>
#define ll long long int
using namespace std;

int main() {
	// your code goes here
	char s[1001];
	ll i,t,t1;
	t1=0;
	cin>>t;
	while(t--)
	{
	    t1++;
	    //max=-1;
	    cout<<"Case #"<<t1<<": ";
	    cin>>s;
	    //s1="";
	    string s1;
	    s1="";
	    s1=s[0]+s1;
	    for(i=1;i<strlen(s);i++)
	    {
	       if(s[i]<s1[0])
	       s1=s1+s[i];//cout<<"1";}
	       else
	       s1=s[i]+s1;//cout<<"2";}
	    }
	    cout<<s1<<"\n";
	}
	return 0;
}
