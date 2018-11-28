#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out2.o","w",stdout);
    int i,j,k,l,m,n,t;
    scanf("%d",&t);
    string s;
    getchar();
    for(int p=1;p<=t;p++)
    {
        getline(cin,s);
        l=s.size();
        int c=0;
        for(i=0;i<l-1;i++)
        {
            if(s[i]!=s[i+1])
                c++;
        }
        if(s[l-1]=='-')
            c++;
        printf("Case #%d: %d\n",p,c);
    }
}
