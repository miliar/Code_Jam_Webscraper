#include<bits/stdc++.h>

using namespace std;
char s[1500];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("b.txt","w",stdout);
    int m,c=0,k,t,n,i,j;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        c=0;
        m=0;
        cin>>n;
        cin>>s;
        for(j=0;j<n+1;j++)
        {
            if(c>=j)
            {
                c+=s[j]-48;
            }
            else
            {
                m+=1;
                c+=1;
                c+=s[j]-48;
            }
            //cout<<c<<" ";
        }
        printf("Case #%d: %d\n",i+1,m);
    }
    return 0;
}
