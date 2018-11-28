#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;
#define mp make_pair
#define pb push_back
#define ft first
#define sd second

#define mod 1000000007
#define inf 2000000001

int main()
{
    freopen("B-large.in","r",stdin);
    int qq,tt;
    scanf("%d",&tt);
    int ans[tt];
    for (qq=1;qq<=tt;qq++)
    {
        int i,j,k,n,f;
        char s[109];
        scanf("%s",&s);
        n=strlen(s);
        f=0; k=0;
        while(f==0)
        {
            if (s[0]=='-')
            {
                for (i=0;s[i]=='-';i++)
                    s[i]='+';
                k++;
            }
            else
            {
                for (i=0;s[i]=='+';i++)
                    s[i]='-';
                if (i==n)
                {
                    f=1;
                    break;
                }
                else
                {
                    for (;s[i]=='-';i++)
                        s[i]='+';
                    k++;
                }
            }
        }
        ans[qq-1]=k;
    }
    fclose(stdin);
    freopen("out.txt","w",stdout);
    for (qq=0;qq<tt;qq++)
    {
        printf("Case #%d: %d\n",qq+1,ans[qq]);
        fflush(stdout);
    }
    fclose(stdout);
}
