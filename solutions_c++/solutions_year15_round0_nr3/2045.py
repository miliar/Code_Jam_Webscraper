# include <iostream>
# include <vector>
# include <cstring>
#include <stdio.h>
#include <set>
#include <algorithm>
using namespace std;
char a[10001][10001];
bool pos[10001][10001];
void mul(char x, char y,int s,int e)
{
    if (x=='1' && y=='i')
        a[s][e]='i',pos[s][e]=pos[s][e-1];
    if (x=='1' && y=='j')
        a[s][e]='j',pos[s][e]=pos[s][e-1];
    if (x=='1' && y=='k')
        a[s][e]='k',pos[s][e]=pos[s][e-1];
    if (x=='1' && y=='1')
        a[s][e]='1',pos[s][e]=pos[s][e-1];
    if (x=='i' && y=='i')
        a[s][e]='1',pos[s][e]=1-pos[s][e-1];
    if (x=='i' && y=='j')
        a[s][e]='k',pos[s][e]=pos[s][e-1];
    if (x=='i' && y=='k')
        a[s][e]='j',pos[s][e]=1-pos[s][e-1];
    if (x=='i' && y=='1')
        a[s][e]='i',pos[s][e]=pos[s][e-1];
    if (x=='j' && y=='i')
        a[s][e]='k',pos[s][e]=1-pos[s][e-1];
    if (x=='j' && y=='j')
        a[s][e]='1',pos[s][e]=1-pos[s][e-1];
    if (x=='j' && y=='k')
        a[s][e]='i',pos[s][e]=pos[s][e-1];
    if (x=='j' && y=='1')
        a[s][e]='j',pos[s][e]=pos[s][e-1];
    if (x=='k' && y=='i')
        a[s][e]='j',pos[s][e]=pos[s][e-1];
    if (x=='k' && y=='j')
        a[s][e]='i',pos[s][e]=1-pos[s][e-1];
    if (x=='k' && y=='k')
        a[s][e]='1',pos[s][e]=1-pos[s][e-1];
    if (x=='k' && y=='1')
        a[s][e]='k',pos[s][e]=pos[s][e-1];
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    for (int tst=1;tst<=t;tst++)
    {
        memset(pos,1,sizeof(pos));
        memset(a,0,sizeof(a));
        int n,k;
        cin>>n>>k;
        string s;
        cin>>s;
        string o=s;
        for (int j=0;j<k-1;j++)
            s+=o;
        int len=n*k;
        for (int i=0;i<len;i++)
        {
            a[i][i]=s[i];
            for (int j=i+1;j<len;j++)
            {
                mul(a[i][j-1],s[j],i,j);
            }
        }
        cout<<"Case #"<<tst<<": ";
        for (int i=0;i<len;i++)
        {
            if (a[0][i]!='i' || pos[0][i]==0)
                continue;
            for (int j=i+1;j<len-1;j++)
            {
                if (a[0][i]=='i' && pos[0][i] && a[i+1][j]=='j' && pos[i+1][j] && a[j+1][len-1]=='k' && pos[j+1][len-1])
                {
                    cout<<"YES"<<endl;
                    goto NEXT;
                }
            }
        }
        cout<<"NO"<<endl;
        NEXT:{}
    }
}
