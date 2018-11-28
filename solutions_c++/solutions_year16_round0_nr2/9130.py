#include<bits/stdc++.h>
#define pi 2*acos(0.0)
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)
#define MAX 10000000
using namespace std;

int main ()
{
    ofstream fout ("B-large.out");
    ifstream fin ("B-large.in");
    int testcase,cs=1; fin>>testcase;
    while(testcase--)
    {
        string str; fin>>str;
        int i=0,j,k,l,m,n,temp,ans=0,result,slen;
        slen=str.length();
        while(i<(slen-1))
        {
            if(str[i]!=str[i+1])
            {
                ans++;i++;
            }
            else
            {
                i++;
            }
        }
        if(str[slen-1]=='+')
            fout<<"Case #"<<cs++<<": "<<ans<<endl;
        else
            fout<<"Case #"<<cs++<<": "<<ans+1<<endl;
    }
    return 0;
}
