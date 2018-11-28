#include <iostream>
#include <cstdio>
using namespace std;
bool check(char s)
{
    if (s=='a'||s=='e'||s=='i'||s=='o'||s=='u') return true;
    return false;
}
int main()
{
        freopen("/home/garfield/下载/A-small-attempt0 (1).in","r",stdin);
    freopen("/home/garfield/下载/ans0.txt","w",stdout);
    string s;
    int n;
    int pp;
    cin>>pp;
    for (int tt=1;tt<=pp;tt++)
    {
        cin>>s>>n;
        int ans=0;
        int len=s.size();
        int i;
        int j=0;
        int last=0;
        for (i=0;i<len;i++)
        {
            if (check(s[i])) j=0;
            else j++;
            if (j>=n)
            {
                ans+=(i-j+1-last+1)*(len-i);
                last=i-j+2;
                j=j-1;
            }
        }
        printf("Case #%d: ",tt);
        cout<<ans<<endl;
    }
}
