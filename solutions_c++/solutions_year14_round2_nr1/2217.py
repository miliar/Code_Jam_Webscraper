#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdio>

using namespace std;
#define N 110



int ct[N][N];
int siz;
int tot[N];
char record[N];
char tmp[N];


int main()
{
//    freopen("D:\\GCJ\\R1B\\A-small-attempt0.in","r",stdin);
//    freopen("D:\\GCJ\\R1B\\A-small-attempt0.txt","w",stdout);
    int T,n;
    cin >> T;
    for (int cas = 0; cas < T; cas++){
        fill(tot,tot+N,0);
//        fill(ct[0][0],ct+N*N,0);
        cin >> n;
        cin >> tmp;
        int len = strlen(tmp);
        bool ok = true;
        record[0] = tmp[0];
        ct[0][0] = 1;
        siz = 0;
        for (int j=1;j<len;j++){
            if (tmp[j]!=tmp[j-1]){
                tot[siz] = ct[0][siz];
                siz++;
                ct[0][siz] = 1;
                record[siz] = tmp[j];
            } else {
                ct[0][siz]++;
            }
        }
        if (ct[0][siz]!=0) {
            tot[siz] = ct[0][siz];
            siz++;
        }

        for (int i=1;i<n;i++){
            cin >> tmp;
            len = strlen(tmp);
            if (ok){
                if (tmp[0]!=record[0]) {
                    ok = false;
                    continue;
                } else
                    ct[i][0] = 1;
                int ssiz = 0;
                for (int j=1;j<len;j++){
                    if (tmp[j]!=record[ssiz]){
                        tot[ssiz] += ct[i][ssiz];
                        ssiz++;
                        if (tmp[j]!=record[ssiz]) {
                            ok = false;
                            break;
                        }
                        ct[i][ssiz] = 1;
                    } else {
                        ct[i][ssiz]++;
                    }
                }
                if (ct[i][ssiz]!=0) {
                    tot[ssiz] += ct[i][ssiz];
                    ssiz++;
                }
                if (ssiz!=siz) ok = false;
            }
        }
        cout << "Case #"<<cas+1<<": ";
        if (!ok)
            cout << "Fegla Won" << endl;
        else {
            int ans = 0;
            for (int i=0; i< siz; i++){
                int avg=tot[i]/n;
                int avg2 = avg+1;
                int sum =0, sum2 = 0;
                for (int j=0;j<n;j++){
                    sum += abs(ct[j][i]-avg);
                    sum2 += abs(ct[j][i]-avg2);
                }
                ans += min(sum,sum2);
            }
            cout << ans << endl;
        }
    }
    return 0;
}
