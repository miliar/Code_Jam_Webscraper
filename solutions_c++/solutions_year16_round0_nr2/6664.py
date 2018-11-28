#include<bits/stdc++.h>
using namespace std;
string s;
int main()
{
//    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int i,j,k,T,t,cot;
    string s,ss;
    cin >> T;
    for(t=1;t<=T;t++)
    {
        cot=0;
        cin >> s;
        for(i=(int)s.size()-1;i>=0;i--)
        {
            if(s[i]=='-')
            {
                k=i;
                break;
            }
        }
        if(i<0)
        {
            printf("Case #%d: 0\n",t);
            continue;
        }
        j=1;
        for(i=1;i<=k;i++)
        {
            if(s[i]!=s[i-1])
            {
                j++;
            }
        }
        printf("Case #%d: %d\n",t,j);
    }
}
