#include <cstdio>
#include <queue>
using namespace std;

class SENATOR{
public:
    int p;
    char c;
    SENATOR(int p, char c){
        this->p = p;
        this->c = c;
    }
};

struct cmp{
    bool operator()(const SENATOR &A, const SENATOR &B){
        if(A.p == B.p)
            return !(A.c < B.c);
        return !(A.p > B.p);
    }
};

priority_queue<SENATOR, vector<SENATOR>, cmp> pq;

int main(){
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    int totalCase;
    scanf("%d", &totalCase);
    for(int T = 1; T <= totalCase; ++T){
        int N, all = 0;
        scanf("%d", &N);
        for(int i = 0; i < N; ++i){
            int x;
            scanf("%d", &x);
            pq.push(SENATOR(x, i+'A'));
            all+=x;
        }
        printf("Case #%d:", T);
        while(!pq.empty()){
            printf(" ");
            SENATOR tmp = pq.top();
            pq.pop();
            printf("%c", tmp.c);
            if(tmp.p > 1)
                pq.push(SENATOR(tmp.p-1, tmp.c));
            all--;
            if(!pq.empty() && pq.top().p > all/2){
                tmp = pq.top();
                pq.pop();
                printf("%c", tmp.c);
                if(tmp.p > 1)
                    pq.push(SENATOR(tmp.p-1, tmp.c));
                all--;
            }
        }
        printf("\n");
    }
    return 0;
}
/*
4
2
2 2
3
3 2 2
3
1 1 2
3
2 3 1
*/
