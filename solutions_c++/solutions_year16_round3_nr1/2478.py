//Senate Evacuation
#include <iostream>
#include <stdio.h>
#include <deque>
#include <algorithm>

using namespace std;

struct Party {
    int c;
    int n;
    void operator=(Party& rhs){
        this->c = rhs.c;
        this->n = rhs.n;
    }
};

bool COMP (Party p1, Party p2){
    return p1.n > p2.n;
}

int main() {
    //freopen("input.txt", "r", stdin);
    int T;
    scanf("%d", &T);
    
    for (int i=1; i<=T; i++) {
        deque<Party> P;
        int N;
        scanf("%d", &N);
        for (int j=0; j<N; j++){
            Party t;
            t.c=j;
            scanf("%d", &t.n);
            P.push_back(t);
        }
        sort(P.begin(), P.end(), COMP);
        cout << "Case #" << i << ": ";
        while (!P.empty()) {
            int s = P.size();
            if (s==2) {                
                while (P[0].n && P[1].n) {
                    char c1 = (char)(int('A')+P[0].c);
                    char c2 = (char)(int('A')+P[1].c);
                    printf("%c%c ",c1,c2);
                    P[0].n--;
                    P[1].n--;
                }
                P.pop_front();
                P.pop_front();
                continue;
            }

            if (P[1].n > P[2].n) {
                int d=P[1].n-P[2].n;
                while(d) {
                    char c1 = (char)(int('A')+P[0].c);
                    char c2 = (char)(int('A')+P[1].c);
                    printf("%c%c ",c1,c2);
                    d--;
                    P[0].n--;
                    P[1].n--;
                }
            }
            
            while (P[0].n) {
                char c = (char)(int('A')+P[0].c);
                if (P[0].n > 1) {
                    printf("%c%c ",c,c);
                    P[0].n -= 2;
                } else {
                    printf("%c ",c);
                    P[0].n--;
                }
            }
            P.pop_front();
        }
        cout << endl;
    }
    
    return 0;
}
