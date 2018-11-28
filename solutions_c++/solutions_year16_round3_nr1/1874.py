#include <cstdio>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;

int main()
{
    int tc;
    scanf("%d",&tc);
    for(int TC =1 ;TC<=tc;TC++){
        printf("Case #%d:",TC);

        int n,p;
        int sum = 0;
        priority_queue<pair<int,int>> pq;
        scanf("%d",&n);
        for(int i=0;i<n;i++) {
            scanf("%d",&p);
            sum += p;
            pq.push(make_pair(p,i));
        }

        while(!pq.empty()) {
            if(pq.size()==2) {
                auto fir = pq.top();
                pq.pop();
                auto sec = pq.top();
                pq.pop();
                if(fir.first == sec.first) {
                    fir.first--;
                    sec.first--;
                    if(fir.first>0) {
                        pq.push(fir);
                        pq.push(sec);
                    }
                    printf(" %c%c",fir.second+'A',sec.second+'A');
                    continue;
                } else {
                    pq.push(fir);
                    pq.push(sec);
                }
            }

            auto now = pq.top();
            pq.pop();
            now.first--;
            sum--;
            if(now.first>0) pq.push(now);
            printf(" %c",now.second+'A');

        }
        printf("\n");
    }
    return 0;
}
