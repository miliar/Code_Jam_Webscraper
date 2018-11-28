#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <fstream>
#include <cstring>
#include <limits>

using namespace std;

int cost (string a, string b){
    int l1 = a.length();
    int l2 = b.length();

    int ret = 0;
    int lastJ = 0;

    for (int i = 0; i < l1;){
        int ic = 1;
        for (int k = i+1; k < l1; k++){
            if (a[i] == a[k]){ ic++; }
            else break;
        }

        int ij = 0;
        int j = 0;
        for (j = lastJ; j < l2; j++){
            if (b[j] != a[i]){
                if (ij == 0) return -1;
                break;
            }
            ij++;
        }

        if (ij == 0) return -1;

        lastJ = j;

        ret += (max(ij, ic) - min(ij, ic));
        i += ic;
    }

    return ret;
}

int main(){
    ifstream cin("A.in");
    ofstream cout ("A.out");


    int n;
    cin >> n;
    for (int k = 1; k <= n; k++){
        int l;
        cin >> l;

        int minCost = numeric_limits<int>::max();

        string s[l];
        for (int i = 0; i < l; i++){
            cin >> s[i];
        }

        for (int i = 0; i < l; i++){
            int c = 0;
            for (int j = 0; j < l; j++){
                if (i == j) continue;

                int c1 = cost(s[i], s[j]);
                int c2 = cost(s[j], s[i]);
                if (c1 != c2)
                    minCost = -1;

                c += cost(s[i], s[j]);
            }

            if (c < minCost) minCost = c;
        }

        cout << "Case #" << k << ": ";

        if (minCost == -1) cout << "Fegla Won";
        else cout << minCost;

        cout << endl;
    }

    return 0;
}
