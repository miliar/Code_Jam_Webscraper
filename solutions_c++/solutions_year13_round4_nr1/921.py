#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

int
main(void)
{
    int T;
    int i, j, k, len;
    long long N, M, ret, num;
    long long vo[1000];
    long long ve[1000];
    long long vp[1000];
    long long sum[1000];
    string s;

    cin >> T;

    for(i=1;i<=T;i++) {
        ret = 0;
        cin >> N >> M;
        for(j=0;j<M;j++) {
            cin >> vo[j] >> ve[j] >> vp[j];
            //            printf("%d %d %d\n", vo[j], ve[j], vp[j]);
            //            cout << vo[j] << ve[j] << vp[j] << endl;
            ret += vp[j]*(N+N-ve[j]+vo[j]+1)*(ve[j]-vo[j])/2;
            //            printf("ret=%d\n", ret);
            //            cout << "ret=" << ret << endl;
        }

        memset(sum, 0, sizeof(sum));

        for(j=0;j<M;j++) {
            for(k=vo[j];k<ve[j];k++) {
                sum[k] += vp[j];
            }
        }
        // for(j=1;j<N;j++) {
        //     printf("%d ", sum[j]);
        // }
        // printf("\n");

        for(len=N-1;len>0;len--) {
            // printf("len %d\n", len);
            for(k=1;k<N;k++) {
                num = 1000000;
                // printf("k %d\n", k);
                for(j=k;j<(k+len);j++) {
                    // printf("j %d\n", j);
                    num = min(sum[j],num);
                }
                // cout << "num=" << num << endl;
                ret -= ((N+N-len+1)*len/2)*num;
                for(j=k;j<(k+len);j++) {
                    sum[j] -= num;
                }
                // cout << "ret=" << ret << endl;
                // for(j=1;j<N;j++) {
                //     printf("%d ", sum[j]);
                // }
                // printf("\n");
            }
        }

        cout << "Case #" << i << ": " << ret << endl;
    }
    
    return 0;
}
