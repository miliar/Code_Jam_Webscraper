#include<iostream>
#include<string>
#include<fstream>
using namespace std;

int main()
{
 	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
    long long t,line=1;
    string s;
    cin>>t;
    while(t--)
    {
        cin>>s;
        char x;
        long long a=0,c1=0,c2;
        
        if(s[s.length()-1]=='-'){x='+';}
        
        else if(s[s.length()-1]=='+')
		{x='-';}

        for(int j=s.length()-1;j>=0;j--)
         {
             if(s[j]==x)
             {
                 a++;
				 for(int i=0;i<=j;i++)
                 {
                     if(s[i]=='-')
					 	{s[i]='+';}
                     else if(s[i]=='+')
					 	{s[i]='-';}
                 }
                 
             }
         }
          c1=0;
      for(int i=0;i<s.length();i++)
             {
                if(s[i]=='+'){c1++;}
             }
             if(c1==s.length()){cout<<"Case "<<"#"<<line<<": "<<a<<"\n";line++;}
          c2=0;
         for(int i=0;i<s.length();i++)
            {
              if(s[i]=='-'){c2++;}
            }
        if(c2==s.length())
		{
			a++;
			cout<<"Case "<<"#"<<line<<": "<<a<<"\n";line++;
		}

        
    }

    return 0;
}
