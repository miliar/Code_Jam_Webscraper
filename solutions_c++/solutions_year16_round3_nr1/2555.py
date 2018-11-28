#include <bits/stdc++.h>

using namespace std;

class Party {
public:
    char name;
    int qty;
    bool operator <(const Party &p) const {
        return this->qty > p.qty;
    }
    Party(char name, int qty) : name(name), qty(qty){}
    Party() : qty(0){}
};

/*void printv(vector<Party> v) {
    for (int i = 0; i < v.size(); ++i) {
        printf("%c %d ", v[i].name, v[i].qty);
    }
    printf("\n");
}*/

int main() {
    freopen("senate.in", "r", stdin);
    freopen("senate.out", "w", stdout);
    int T;
    scanf("%d", &T);

    for (int z = 0; z < T; ++z) {
        int N, sum = 0, name = 'A';
        scanf("%d", &N);
        printf("Case #%d: ", z+1);
        vector<Party> room(N+2);
        for(int i = 0; i < N; i++) {
            int t;
            scanf("%d", &t);
            room[i] = Party(name, t);
            sum += t;
            name++;
        }
        while(sum > 0) {
            sort(room.begin(), room.end());
            //printv(room);
            Party &a = room[0], &b = room[1];
            if(sum-2 != 0 && ((sum-2)/2.0 < room[2].qty || (sum-2.0)/2.0 < a.qty-1)) {
                a.qty--;
                sum--;
                printf("%c", a.name);
            }
            else {
                a.qty--;
                sum--;
                printf("%c", a.name);
                if(b.qty > 0) {
                    b.qty--;
                    sum--;
                    printf("%c", b.name);
                }
            }
            printf(" ");
        }
        printf("\n");
    }

    return 0;
}