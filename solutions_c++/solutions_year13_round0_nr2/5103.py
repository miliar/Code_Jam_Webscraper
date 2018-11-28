#include <fstream>
#include <algorithm>
using namespace std;

ifstream cin("B-large.in");
ofstream cout("output.txt");

long t,m,n,a[200][200],mxv[200][200],mxh[200][200];

int main()
{
    cin>>t;
    for (long i=0;i<t;i++){
    cin>>n>>m;
    for (long j=0;j<n;j++)
    for (long k=0;k<m;k++)
    cin>>a[j][k];
    cout<<"Case #"<<i+1<<": ";

    for (long j=0;j<n;j++)
    for (long k=0;k<m;k++)
        mxh[i][j]=max(mxh[i][j],a[j][k]);

    for (long j=0;j<m;j++)
    for (long k=0;k<n;k++)
        mxv[i][j]=max(mxv[i][j],a[k][j]);

    bool alr=1;
    for (long j=0;j<n;j++)
    for (long k=0;k<m;k++)
    if (a[j][k]!=mxh[i][j] && a[j][k]!=mxv[i][k])
            alr=0;

    alr ? cout<<"YES":cout<<"NO";
    cout<<endl;

    }

    return 0;
}
