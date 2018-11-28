#include<iostream>
#include<vector>
#include<stdio.h>
#include<string>

using namespace std;

int main()
{     
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out","w",stdout);
    
    int T;
    cin>>T;
    for(int cas=1;cas<=T;cas++)
    {
        string s;
        cin>>s;
        
        int ans;
        ans=0;
        
        int len=s.size();
        for(int i=0;i<len-1;i++)
            if(s[i]!=s[i+1])
                ans++;
        
        if(s[len-1]=='-')
            ans++;
            
        printf("Case #%d: %d\n",cas,ans);      
          
    }//
    
  //system("pause");
}
