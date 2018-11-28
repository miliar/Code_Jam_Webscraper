#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
using namespace std;
const int N=1005;
char a[N];
int main()
{
    int t,i,kk,l,j,pos;
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    scanf("%d",&t);
    vector<char>g;
    kk=t;

    while(t--)
    {
        pos=0;
        scanf("%s",a);
        l=strlen(a);
        g.insert(g.begin(),a[0]);
        pos++;
        for(i=1; i<l; i++)
        {
            if(a[i]>=g[0]) g.insert(g.begin(),a[i]);
            else g.insert(g.begin()+pos,a[i]);
            pos++;
        }
        printf("Case #%d: ",kk-t);
        for(i=0; i<l; i++)
        {
            printf("%c",g[i]);
        }
        printf("\n");
    }
    return 0;
}
