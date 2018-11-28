#include <iostream>
#include <cstdio>
using namespace std;

int f(int n)
{
    int visited[100], i, j, k;
    for (i=0; i<100; i++) visited[i]=false;

    for (i=n, j=0; j<500; j++, i+=n)
    {
        for (k=i; k>0; k/=10) {visited[k%10]=true;}

        int sum=0;
        for (k=0; k<10; k++) sum+=visited[k];
        if (sum==10) return i;
    }
}
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int i, j, k, t, cs=0, n;

    cin>>t;
    while (t--)
    {
        cin>>n;

        printf("Case #%d: ", ++cs);
        if (n==0) printf("INSOMNIA\n");
        else
        {
            cout<<f(n)<<endl;
        }
    }

}
