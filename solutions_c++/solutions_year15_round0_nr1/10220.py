#include <iostream>
#include <cstdio>
#include <cstring>
#include <fstream>
using namespace std;
int main()
{
    int t,smax,i,cnt,sum,n;
    string s;
    ifstream ef;
    ofstream of;
    ef.open("A-small-attempt3.in");
    of.open("output.txt");
    ef>>t;
    n=t;
    while(t--)
    {
        cnt=sum=0;
        ef>>smax>>s;
        for(i=0;i<=smax;i++)
        {
            if((s[i]-'0')>0)
            {
                if(cnt<i)
                {
                    sum+=i-cnt;
                    cnt+=sum;
                }
                cnt+=(s[i]-'0');
            }
        }
        of<<"Case #"<<n-t<<": "<<sum<<"\n";
    }
    of.close();
    ef.close();
    return 0;
}
