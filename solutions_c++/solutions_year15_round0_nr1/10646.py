#include<iostream>
using namespace std;
int main()
{
    int T,i,s,N,e,l;
    char str[1003];
    cin>>T;
    for(e=1;e<=T;e++)
    {
        cin>>N;
        cin>>str;
      //  l=strlen(str);
      s=0;

      l=0;
        for(i=0;i<=N;i++)
        {
            if(s<i)
                {
                    l+=i-s;
                   s+=(i-s);
                }
            s+=(str[i]-'0');


        }
      cout<<"Case #"<<e<<": "<<l<<'\n';
    }

}

