#include <iostream>
#include <cstdio>
#include <string>
using namespace std;
const int maxn=1001;
int a[maxn];
int q(int r,int t)
{
    return r/t+((r%t)!=0)-1;
}
void work()
{
    int n,i,j,k;
    cin >> n;
    for (i=1;i<=n;i++)
        cin >> a[i];
    int sum=0,ans=9999;
    for (k=1;k<=1000;k++)
    {
        sum=0;
        for (i=1;i<=n;i++)
        {
            sum+=q(a[i],k);
        }
        if (sum+k<ans) ans=sum+k;
    }
    cout << ans << endl;
}
int main()
{
    int T;
    cin >> T;
    for (int cas=1;cas<=T;cas++)
    {
        cout<<"Case #"<<cas<<": ";
        work();
    }
}
