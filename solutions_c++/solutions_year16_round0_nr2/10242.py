#include<iostream>
#include<string>
#include<fstream>
using namespace std;

int main()
{
 	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
    long long int t,line=1;
    string s;
    cin>>t;
    while(t>0)
    {
        cin>>s;
        char c;
        int foo=0,count1,count2;
        /* for(int i=0;i<s.length();i++)
             {
                if(s[i]=='+'){count1++;}
             }
             if(count1==s.length()){cout<<foo; return 0;}
              count2=0;
        for(int i=0;i<s.length();i++)
            {
              if(s[i]=='-'){count2++;}
            }
             if(count2==s.length()){foo++; cout<<foo;return 0;}
*/
        if(s[s.length()-1]=='-'){c='+';}
        else if(s[s.length()-1]=='+'){c='-';}

        for(int j=s.length()-1;j>=0;j--)
         {
             if(s[j]==c)
             {
                 for(int i=0;i<=j;i++)
                 {
                     if(s[i]=='-'){s[i]='+';}
                     else if(s[i]=='+'){s[i]
                     ='-';}
                 }
                 foo++;
             }
         }
          count1=0;
      for(int i=0;i<s.length();i++)
             {
                if(s[i]=='+'){count1++;}
             }
             if(count1==s.length()){cout<<"Case "<<"#"<<line<<": "<<foo<<"\n";line++;}
          count2=0;
         for(int i=0;i<s.length();i++)
            {
              if(s[i]=='-'){count2++;}
            }
        if(count2==s.length()){foo++;cout<<"Case "<<"#"<<line<<": "<<foo<<"\n";line++;}

        t--;
    }

    return 0;
}
