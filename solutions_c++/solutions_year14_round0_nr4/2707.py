#include<fstream>
#include<algorithm>
using namespace std;
ifstream fin ("temp.in");
ofstream fout ("temp.out");
double nanmi[1000];
double ken[1000];
int main ()
{
    int t;
    fin>>t;
    int i,j;
    for (i=1;i<=t;i++)
    {
        int n;
        fin>>n;
        for (j=0;j<n;j++) fin>>nanmi[j];
        for (j=0;j<n;j++) fin>>ken[j];
        sort (nanmi,nanmi+n);
        sort (ken,ken+n);
        int p=n-1,q;
        int a=0;
        for (q=n-1;q>=0;q--)
        {
            while (ken[q]<nanmi[p]&&p>=0) p--;
            if (p>=0) a++;
            p--;
        }
        a=n-a;
        int b=0;
        q=n-1;
        for (p=n-1;p>=0;p--)
        {
            while (ken[q]>nanmi[p]&&q>=0) q--;
            if (q>=0) b++;
            q--;
        }
        fout<<"Case #"<<i<<": "<<b<<" "<<a<<endl;
    }
    return 0;
}
