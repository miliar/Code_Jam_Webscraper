#include <stdio.h>
#include <string.h>
#include <vector>
#include <map>
#include <algorithm>
#include <string>

using namespace std;

int rr,pp,ss,indx;
int ans[11000];
const char* out = "RPS";

string dfs(int n, int c)
{
    if (n==0)
    {
        if (c==0)
            rr++;
        else if (c==1)
            pp++;
        else
            ss++;
        ans[indx++]=c;

        static char tmp[10];
        tmp[0]=out[c];
        tmp[1]=0;
        return tmp;
    }
    int c1=c,c2=(c+2)%3;
    string s1=dfs(n-1, c1);
    string s2=dfs(n-1, c2);
    if (s1<s2)
        return s1+s2;
    return s2+s1;
}

int main()
{
    int t;
    scanf("%d",&t);
    for (int ii=1;ii<=t;ii++)
    {
        int n,r,p,s;
        scanf("%d%d%d%d",&n,&r,&p,&s);
        string str;
        for (int i=0;i<3;i++)
        {
            rr=pp=ss=indx=0;
            string s1 = dfs(n, i);
            if (rr==r&&pp==p)
            {
                if (str=="" || s1<str)
                    str=s1;
            }
        }

        printf("Case #%d: ", ii);
        if (str=="")
        {
            puts("IMPOSSIBLE");
        }
        else
        {
            puts(str.c_str());
        }
    }
}
