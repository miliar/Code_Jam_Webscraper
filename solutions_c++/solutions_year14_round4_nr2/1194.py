#include <cstdio>
#include <algorithm>
using namespace std;

const int MAX_N = 1005;

int N;
int vals[MAX_N];
int numLeft[MAX_N];
int numRight[MAX_N];

int myabs(int a) {
    if(a < 0) {
        return -a;
    }
    return a;
}

int main() {
    int T;
    scanf("%d",&T);

    for(int z=1;z<=T;z++) {
        scanf("%d",&N);

        for(int i=0;i<N;i++) {
            scanf("%d",&vals[i]);
        }

        int largest = 0;
        for(int i=1;i<N;i++) {
            if(vals[i] > vals[largest]) {
                largest = i;
            }
        }
        
        int tot = 0;

        for(int i=0;i<N;i++) {
            numLeft[i] = 0;
            numRight[i] = 0;

            for(int j=0;j<i;j++) {
                if(vals[j] > vals[i]) {
                    numLeft[i]++;
                }
            }

            for(int j=i+1;j<N;j++) {
                if(vals[j] > vals[i]) {
                    numRight[i]++;
                }
            }

            if(i < largest) {
                tot += numLeft[i];
            } else if(i > largest) {
                tot += numRight[i];
            }
        }

        int best = tot;

        int pos1 = tot;
        for(int i=0;i<largest;i++) {
            if(numLeft[i] >= numRight[i]) {
                pos1 -= numLeft[i];
                pos1 += numRight[i];
            }
        }

        best = min(best, pos1);

        int pos2 = tot;
        for(int i=largest+1;i<N;i++) {
            if(numRight[i] >= numLeft[i]) {
                pos2 -= numRight[i];
                pos2 += numLeft[i];
            }
        }

        best = min(best, pos2);

        printf("Case #%d: %d\n",z,best);
    }

    return 0;
}
