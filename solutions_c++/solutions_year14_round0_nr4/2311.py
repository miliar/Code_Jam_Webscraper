#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <iostream>

using namespace std;

int main()
{
    int t;
    int logs;
    freopen("D-large.in.txt","r",stdin);
    freopen("outpopox.txt","w",stdout);

    scanf("%d", &t);
    for(int i = 1;i <= t;i++) {
        scanf("%d", &logs);

        double naomi[logs];
        double ken[logs];

        for(int j = 0;j < logs;j++) {
            scanf("%lf", &naomi[j]);
        }

        for(int j = 0;j < logs;j++) {
            scanf("%lf", &ken[j]);
        }

        sort(naomi, naomi+logs);
        sort(ken, ken+logs);

        int count_deceit = 0;
        int count_optimal = 0;

        int lower_limit = 0;
        int idxn = logs-1;
        int idxk = logs-1;

        while(idxn >= lower_limit && idxk >= 0) {
            if(naomi[idxn] > ken[idxk]) {
                count_deceit++;
                idxn--;
                idxk--;
            } else {
                lower_limit++;
                idxk--;
            }
        }

        int last = 0;

        for(int j = 0;j < logs;j++) {
            double nval = naomi[j];
            int flag = 0;

            for(int idx = last;idx < logs;idx++) {
                if(ken[idx] > nval) {
                    flag = 1;
                    last = idx+1;
                    break;
                }
            }

            if(flag == 0) {
                count_optimal = logs - j;
                break;
            }
        }

        printf("Case #%d: %d %d\n", i, count_deceit, count_optimal);
    }
    return 0;
}
