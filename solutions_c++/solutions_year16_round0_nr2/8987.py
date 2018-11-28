/*
Rasedur Rahman Roxy
Facebook: www.facebook.com/MdRoxy
E-mail: roxy.xmw@gmail.com
Condeforces: mdroxy

Problem link:
*/

#include<iostream>
#include<fstream>
#include<cstdio>
#include<cstring>
#include<cctype>
#include<cmath>
#include<vector>
#include<map>
#include<algorithm>
#include<set>

#define ll long long
#define read freopen("in.txt","r",stdin)
#define write freopen("out.txt","w",stdout)
#define loop(x,y,z) for(int i=x;i<y;i+=z)
#define cloop(x,y,z) for(int i=x;i>=y;i-=z)
#define PI acos(-1.0)
#define pf printf
#define MAX 100009

using namespace std;

int main()
{
    //read;
    //write;
    string s;
    int tst;
    cin>>tst;
    for(int t=1;t<=tst;t++)
    {
        cin>>s;
        int l=s.size(),c=0,lst,f=1;
        while(f)
        {
            f=0;
            bool x=1;
            for(int i=l-1;i>=0;i--)
                if(s[i]=='-')
                {
                    c++;
                    lst=i;
                    x=0;
                    break;
                }
            if(x) break;
            for(int i=lst;i>=0;i--)
                if(s[i]=='-') s[i]='+';
                else
                {
                    f=1;
                    s[i]='-';
                }
        }
        pf("Case #%d: %d\n",t,c);
        s.clear();
    }
    return 0;
}

