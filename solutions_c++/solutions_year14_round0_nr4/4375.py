#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int test = 1; test<=T; test++){
        int N, y = 0, z = 0;
        double d;
        cin >> N;
        vector<double> naomi, ken;
        for (int i = 0; i<N; i++){
            cin >> d;
            naomi.push_back(d);
        }
        for (int i = 0; i<N; i++){
            cin >> d;
            ken.push_back(d);
        }
        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());
        bool found1[1005] = {0};
        bool found2[1005] = {0};
        for (int i = 0; i<N; i++){
            for (int j = 0; j<N; j++){
                if (!found1[j] && naomi[i]<ken[j]){
                    found1[j] = true;
                    break;
                }
                if (j == N-1) {
                    z++;
                    //cout << "Naomi's "<< naomi[i] << " is undefeated."<< endl;
                }
            }
        }
        for (int i = 0; i<N; i++){
            for (int j = 0; j<N; j++){
                if (!found2[j] && ken[i]<naomi[j]){
                    //cout << "Naomi's block value " << naomi[j] << " deafeats Ken's " << ken[i] << endl;
                    found2[j] = true;
                    y++;
                    break;
                }
            }
        }
        printf("Case #%d: %d %d\n", test, y, z);
    }
}
