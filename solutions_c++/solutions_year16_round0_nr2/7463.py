#include <bits/stdc++.h>
#include <iostream>
#include <string>

using namespace std;

int main()
{
    FILE *f=fopen("C:\\Users\\Vishal\\Desktop\\output.txt","w");
    int t;
    cin>>t;
    int tcp=0;
    while(t--)
    {
        int l,ans=0,i,pos=-1;
        string s;
        cin>>s;
        l=s.length();
        tcp++;
        for(i=l-1;i>=0;i--)
        {
           // cout<<s[i]<<endl;
            if(s[i]=='-')
            {
                pos=i;
                break;
            }
        }
        //cout<<pos<<endl;
        if(pos==-1)
        {
            fprintf(f,"Case #%d: %d\n",tcp,0);
        }

        else
        {
            //cout<<"here"<<endl;
        for(i=0;i<=pos;)
        {
           if(s[i]=='-')
           {
               while(s[i]=='-')
                    i++;
            ans++;
           }
           else if(s[i]=='+')
           {
               while(s[i]=='+')
                    i++;
            ans++;
           }
        }
        fprintf(f,"Case #%d: %d\n",tcp,ans);
        }
    }
    return 0;
}
