#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;


int solveWar(vector<double> Naomi, vector<double> Ken){
    const int n = Naomi.size();
    vector<int> match(Naomi.size(), -1);

    int matches = 0;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if (Naomi[j] < Ken[i] && match[j] == -1) {
                match[j] = i;
                matches++;
                break;
            }
        }
    }
    
    return n-matches;
}

int solveDeceitfulWar(vector<double> Naomi, vector<double> Ken) {
    const int n = Naomi.size();
    vector<int> match(Naomi.size(), -1);

    int matches = 0;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if (Ken[j] < Naomi[i] && match[j] == -1) {
                match[j] = i;
                matches++;
                break;
            }
        }
    }
    return matches;
}

int main() {
    int T;
    scanf("%d", &T);

    for (int testcase = 1; testcase <= T; testcase++) {
        int N;
        scanf("%d", &N);
        vector<double> Naomi;
        vector<double> Ken;

        for(int i = 0; i < N; i++) {
            double d;
            scanf("%lf", &d);
            Naomi.push_back(d);
        }
        for(int i = 0; i < N; i++) {
            double d;
            scanf("%lf", &d);
            Ken.push_back(d);
        }
        

        sort(Naomi.begin(), Naomi.end());
        sort(Ken.begin(), Ken.end());

        printf("Case #%d: %d %d\n", testcase, 
            solveDeceitfulWar(Naomi, Ken), solveWar(Naomi, Ken));
    }
    return 0;
}
