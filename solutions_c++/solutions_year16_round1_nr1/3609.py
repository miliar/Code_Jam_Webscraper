#include <bits/stdc++.h>
using namespace std;
char s[1005];
long long int b[1005];
int main() {
 
    long long int t,k,count;
    cin>>t;
    count=0;
    while(t--)
    { count++;
        list <char> LI;
    list <char>::iterator it;
        cin>>s;
        for(int i=0;i<strlen(s);i++)
        {
            b[i]=s[i]-48;
        }
        LI.push_back(s[0]);
        k=b[0];
        for(int i=1;i<strlen(s);i++)
        {if(b[i]<k)
        LI.push_back(s[i]);
 
 
 
        else
        {
        LI.push_front(s[i]);
        k=b[i];
        }
        }
            cout<<"Case #"<<count<<": ";
 
         for(it = LI.begin();it!=LI.end();it++)
    {
        cout<<*it;
    }cout<<endl;
 
    }
	// your code goes here
	return 0;
}