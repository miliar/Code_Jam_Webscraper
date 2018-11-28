#include<fstream>
#include<algorithm>
using namespace std;
ifstream fin ("A-large.in");
ofstream fout ("temp.out");
int main ()
{
    int t;
    fin>>t;
    int i;
    int save [10010];
    for (i=1;i<=t;i++)
    {
        int n,x;
        fin>>n>>x;
        for (int j=0;j<n;j++)
            fin>>save[j];
        sort (save,save+n);
        int p=0,q=n-1;
        int ans=0;
        while (p<=q)
        {
            if (save[p]+save[q]>x) {ans++;q--;}
            else {ans++;p++;q--;}
        }
        fout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
