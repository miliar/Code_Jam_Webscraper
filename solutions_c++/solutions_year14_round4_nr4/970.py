#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

#ifdef DEBUG
#define D(x...) fprintf(stderr,x)
#else
#define D(x...)
#endif

const int MAX_CHAR = 105;
const int MAX_M = 10;

int T;
int tree[MAX_CHAR][26];

int N, M;
char str[MAX_M][MAX_CHAR];

int best = 0;
int numBest = -1;

int perm[10];

int makeTrie(vector<int> &ind) {
    for(int i=0;i<MAX_CHAR;i++) {
        for(int j=0;j<26;j++) {
            tree[i][j] = -1;
        }
    }

    int S = 1;

    for(int i=0;i<ind.size();i++) {
        int w = ind[i];
        int L = strlen(str[w]);

        int cur = 0;
        for(int j=0;j<L;j++) {
            int let = str[w][j] - 'A';
            if(tree[cur][let] == -1) {
                tree[cur][let] = S;
                S++;
            }
            cur = tree[cur][let];
        }
    }

    return S;
}

void gen(int ply) {
    if(ply == M) {
        int tot = 0;
        for(int i=0;i<N;i++) {
            vector<int> ind;
            for(int j=0;j<M;j++) {
                if(perm[j] == i) {
                    ind.push_back(j);
                }
            }

            if(!ind.empty()) {
                tot += makeTrie(ind);
            }
        }

        for(int i=0;i<M;i++) {
            D("%d ",perm[i]);
        }
        D(" = %d\n",tot);

        if(tot > best) {
            best = tot;
            numBest = 1;
        } else if(tot == best) {
            numBest++;
        }
    } else {
        for(int i=0;i<N;i++) {
            perm[ply] = i;
            gen(ply+1);
        }
    }
}

int main() {
    int T;
    scanf("%d",&T);

    for(int z=1;z<=T;z++) {
        scanf("%d %d",&M,&N);

        for(int i=0;i<M;i++) {
            scanf(" %s ",str[i]);
        }

        best = 0;
        numBest = -1;

        gen(0);

        printf("Case #%d: %d %d\n",z,best,numBest);
    }

    return 0;
}
