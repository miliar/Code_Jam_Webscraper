#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cstdlib>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("b.out","w",stdout);
    int T;
    while (cin>>T)
    {
        for (int ca=1;ca<=T;ca++)
        {
            char x[200];
            cin>>x;
            int len=strlen(x);
            int i,cnt;
            cnt=0;
            for (i=1;i<len;i++)
            {
                if (x[i]!=x[i-1]) cnt++;
            }
            if (x[len-1]=='-') cnt++;
        printf("Case #%d: %d\n",ca,cnt);
        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
