#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("revenge-large.out","w",stdout);
    int t;
    cin>>t;
    for(int i = 1; i<= t; i++)
    {
        string s;
        cin>>s;
        int countof=0;
        int ans;
        for(int j = 0; j<= s.length()-1; j++)
        {
           if(s[j]=='+')
                countof++;
        }
        
        if(countof==s.length())
            ans=0;
            
        else 
        {  int pos;
            for(int j = s.length()-1; j>= 0; j--)
            {
                if(s[j]=='-')
                {pos = j; break;}
            }
            
            
            int count = 1;
            for(int j =0; j<= pos-1; j++)
            {
                if(s[j]!=s[j+1])
                count++;
            }
            ans = count;
        }
        
        
    cout<<"Case "<<"#"<<i<<": "<<ans<<endl; 
    }
    
    return 0;
}
