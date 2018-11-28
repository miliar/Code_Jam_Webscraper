#include <iostream>
#include<cstring>
#include<cstdio>
using namespace std;

bool ok(string s)
{
    int ls=s.length();
    for(int i=0;i<ls;i++)
        if(s[i]=='-')   return false;
    return true;
}

string s;
int T,ls;

int main()
{
    freopen("w.txt","w",stdout);

    cin>>T;
    for(int TT=1;TT<=T;TT++)
    {
        cin>>s;
        ls=s.length();
        int times=0;
        while(!ok(s))
        {
            int t=0;
            while((s[t]==s[t+1])&&(t<=ls-2)) t++;
            for(int i=0;i<=t;i++)
                if(s[i]=='-')   s[i]='+';   else s[i]='-';
            times++;
        }
        cout<<"Case #"<<TT<<": "<<times<<endl;
    }

    return 0;
}
