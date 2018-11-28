#include<cstdio>
#include<iostream>
#include<queue>

using namespace std;

int t, casei, n;
int p[30];

int main() {
    casei = 0;
    scanf("%d", &t);
    while(t--) {
        priority_queue<pair<int, int> > pq;
        scanf("%d", &n);
        int n_tmp = 0;
        for(int i = 0; i < n; i++) {
            scanf("%d", &p[i]);
            n_tmp += p[i];
            pq.push(make_pair(p[i], i));
        }
        printf("Case #%d: ", ++casei);
        while(!pq.empty()) {
            pair<int, int> party_max_1 = pq.top();
            pq.pop();

            pair<int, int> party_max_2;
            bool has_party_max_2 = false;
            if(!pq.empty()) {
                party_max_2 = pq.top();
                pq.pop();
                has_party_max_2 = true;
            }

            if(has_party_max_2) {
                if(party_max_1.first == party_max_2.first) {
                    printf("%c", party_max_1.second + 65);
                    --party_max_1.first;
                    --n_tmp;
                    if(n_tmp != 2) {
                        printf("%c", party_max_2.second + 65);
                        --party_max_2.first;
                        --n_tmp;
                    }
                }
                else {
                    printf("%c%c", party_max_1.second + 65, party_max_1.second + 65);
                    party_max_1.first -= 2;
                    n_tmp -= 2;
                }
            }
            else {
                printf("%c", party_max_1.second + 65);
                --party_max_1.first;
                --n_tmp;
            }

            if(party_max_1.first > 0)
                pq.push(party_max_1);
            if(party_max_2.first > 0)
                pq.push(party_max_2);

            printf(" ");
        }
        printf("\n");
    }
    return 0;
}
