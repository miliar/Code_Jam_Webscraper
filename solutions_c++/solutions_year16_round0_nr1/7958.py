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
    freopen("A-large.in","r",stdin);
    int qq,tt;
    scanf("%d",&tt);
    int ans[tt];
    for (qq=1;qq<=tt;qq++)
    {
        int i,j,k,n;
        scanf("%d",&n);
        if (n==0)
            ans[qq-1]=-1;
        else
        {
            int a[10]={0};
            i=1;
            while(1)
            {
                k=(n*i);
                while(k>0)
                {
                    a[k%10]=1;
                    k/=10;
                }
                int f=1;
                for (j=0;j<10;j++)
                {
                    if (a[j]==0)
                    {
                        f=0;
                        break;
                    }
                }
                if (f==1)
                {
                    ans[qq-1]=(n*i);
                    break;
                }
                i++;
            }
        }
    }
    fclose(stdin);
    freopen("out.txt","w",stdout);
    for (qq=0;qq<tt;qq++)
    {
        if (ans[qq]==-1)
            printf("Case #%d: INSOMNIA\n",qq+1);
        else
            printf("Case #%d: %d\n",qq+1,ans[qq]);
        fflush(stdout);
    }
    fclose(stdout);
}
