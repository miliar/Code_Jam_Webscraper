#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <map>
#include <utility>
#include <set>
#include <vector>
#include <string.h>
#include <queue>
#include <iostream>
#include <stdlib.h>

using namespace std;

#define MAXN 1000005
#define MOD 1000000007
#define INF (1 << 30)
#define st first
#define nd second

double A, B, C;

int main() {
    int T;
    cin >> T;
    for(int i = 1; i <= T; i++){
        
        cin >> A >> B >> C;
        cout << "Case #" << i << ": ";
        double answer = C / 2.0;
        double V = 2.0;
        double time = 0.0;
        for(int k = 1; k < MAXN && time <= answer; k++){
            time += A / V;
            V += B;
            
            answer = min(answer, time + C / V);
        }
        printf("%.6lf\n", answer);
    }
    return 0;
}
