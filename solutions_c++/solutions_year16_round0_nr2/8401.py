//Utkarsh Jha
#include<iostream>
#include<string>
#include<fstream>

using namespace std;

int main()
{
     FILE *fin = freopen("B-large.in", "r", stdin);
	FILE *fout = freopen("B-large.out", "w", stdout);
    long long int t,index=1;
    string s;
    cin>>t;
    while(t--)
    {
        cin>>s;
        char cs;
        long long int ans=0,foo1,foo2,x;
        x=s.length();
        if(s[x-1]=='-'){cs='+';}
        else if(s[x-1]=='+'){cs='-';}

        for(int j=s.length()-1;j>=0;j--)
         {
             if(s[j]==cs)
             {
                 for(int i=0;i<=j;i++)
                 {
                     if(s[i]=='-'){s[i]='+';}
                     else if(s[i]=='+'){s[i]
                     ='-';}
                 }
                 ans++;
             }
         }
      foo1=0;
      for(int i=0;i<s.length();i++)
             {
                if(s[i]=='+'){foo1++;}
             }
             if(foo1==s.length()){cout<<"Case "<<"#"<<index<<": "<<ans<<"\n";index++;}
          foo2=0;
         for(int i=0;i<s.length();i++)
            {
              if(s[i]=='-'){foo2++;}
            }
        if(foo2==s.length()){ans++;cout<<"Case "<<"#"<<index<<": "<<ans<<"\n";index++;}

    }

    return 0;
}
