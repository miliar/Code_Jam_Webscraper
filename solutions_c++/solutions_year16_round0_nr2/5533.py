#include<bits/stdc++.h>
#define ll   long long

#define md 1000000007

using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
   #ifndef ONLINE_JUDGE
            freopen("input.txt","r",stdin);
            freopen("output.txt","w",stdout);    
    #endif
      int test;
      cin>>test;
     for(int tst=1;tst<=test;tst++){
     	cout<<"Case #"<<tst<<": ";
     	string s;
        cin>>s;
        int ct=0;
        char sign=s[0];
        for(int i=0;i<s.length();i++){
            if(s[i]!=sign)
                ct++;
            sign=s[i];
        }
        if(sign=='-')
            ct++;
        cout<<ct<<endl;
     	
     }
    return 0;
    
    
    
}
