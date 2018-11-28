//OUM HARI OUM, OUM TATSAT
// OUM NAMA VAGABATE BASUDEBAY
// OUM NAMA MA SWARASATI OUM NAMA

#include<cmath>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<fstream>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<sstream>
#include<stack>
#include<stdlib.h>
#include<iostream>
#include<algorithm>

#define cl(vctr) vctr.clear()
#define ms(v, ar) memset(ar, v, sizeof(ar))

const double pi=(double)(2.0 * acos( 0.0 ));
const int inf=1 << 30;
const double eps=1E-9;
const double e = exp(1.0);
const int sz=100000 + 5;
const int mod=1000000000 + 7;

using namespace std;
typedef long long int ll;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("Aout.in","w",stdout);
    int t,T,i,l;
    scanf("%d",&t);T=t;
    while(t--)
    {
        string s;
        cin>>s;
        cout<<"Case #"<<T-t<<": ";
        string s1="",s2="",res="";
        l=s.length();
        for(i=0;i<l;i++)
        {
            s1=res;
            s1+=s[i];
            s2="";
            s2+=s[i];
            s2=s2+res;
            if(s1>s2)
                res=s1;
            else
                res=s2;
        }
        cout<<res<<endl;
    }

    return 0;
}
