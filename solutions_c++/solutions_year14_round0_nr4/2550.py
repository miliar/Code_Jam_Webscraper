#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
    int i,j,k,t;
    double a[1001],b[1001];
    int n,ans;
    int cc = 0;
    ifstream fin("war.in");
    ofstream fout("war.out");

    fin>>t;
    while (cc<t){
        cc++;

        fin>>n;
        for (i=1;i<=n;i++) fin>>a[i];
        for (i=1;i<=n;i++) fin>>b[i];
        for (i=1;i<=n;i++)
            for (j=i+1;j<=n;j++){
                if (a[j]<a[i]){
                    double tmp = a[i];
                    a[i] = a[j];
                    a[j] = tmp;
                }
                if (b[j]<b[i]){
                    double tmp = b[i];
                    b[i] = b[j];
                    b[j] = tmp;
                }
            }

        ans = 0;
        i = 1; j = 1;
        while ((i<=n)&&(j<=n)){
            if (a[i]>b[j]){
                ans = ans + 1;
                i++;
                j++;
            }
            else i++;
        }
        fout<<"Case #"<<cc<<": "<<ans;

        ans = 0;
        i = 1; j = 1;
        while ((i<=n)&&(j<=n)){
            if (a[i]<b[j]){
                ans = ans + 1;
                i++;
                j++;
            }
            else j++;
        }
        ans = n - ans;
        fout<<" "<<ans<<endl;
    }
    return 0;
}
