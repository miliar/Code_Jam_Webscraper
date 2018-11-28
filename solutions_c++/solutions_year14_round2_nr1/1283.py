#include <cstdio>
#include <iostream>
#include <cstring>
#include <cstdlib>
using namespace std;
#define INF 1000000007
char pat[110], inp[110][110];
int cnt[110][110], ar[110];
int main() {
    freopen("repn.in","r",stdin);
    freopen("rep2.out","w",stdout);
    int n, tc, l, t = 1, patlen, cur_cost, minm, sum;
    scanf("%d",&tc);
    while (tc--) {
        memset(cnt, 0, sizeof(cnt));
        memset(ar, 0,sizeof(ar));
        scanf("%d",&n);
        for (int i=0; i<n; i++) {
            scanf("%s",inp[i]);
        }
        bool pssbl = true;
        for (int i=0; i<n; i++) {
            l = strlen(inp[i]);
            char temp[110];
            int k = 0, c = 0;
            for (int j=0; j<l; j++) {
                c += 1;
                if (j == 0 || inp[i][j-1] != inp[i][j]) {
                    temp[k++] = inp[i][j];
                }
                if (j == l-1 || inp[i][j+1] != inp[i][j]) {
                    cnt[i][k-1] = c;
                    c = 0;
                }
            }
            temp[k] = '\0';
            /*cout<<"temp : "<<temp<<endl;
            for (int r=0; r<k; r++) {
                cout<<cnt[i][r]<<" ";
            }   cout<<endl;*/
            if (i == 0) {
                //cout<<"temp : "<<temp<<endl;
                strcpy(pat, temp);
                patlen = strlen(pat);
                //cout<<"temp : "<<temp<<"  pat : "<<pat<<endl;
            } else if (strcmp(temp, pat) != 0) {
                //cout<<"not possible\n";
                pssbl = false;
                break;
            }
        }
        if (!pssbl) {
            printf("Case #%d: Fegla Won\n",t);
            t++;
            continue;
        }
        for (int i=0; i<n; i++) {
            for (int j=0; j<patlen; j++) {
                ar[j] = max(ar[j], cnt[i][j]);
            }
        }
        int sum = 0;
        for (int i=0; i<patlen; i++) {
            minm = INF;
            for (int g=1; g<=ar[i]; g++) {
                cur_cost = 0;
                for (int j=0; j<n; j++) {
                    cur_cost += abs(cnt[j][i] - g);
                }
                minm = min(minm, cur_cost);
            }
            sum += minm;
        }
        printf("Case #%d: %d\n",t,sum);
        t++;
    }
    return 0;
}
