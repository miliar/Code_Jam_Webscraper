#include <cstdio>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cassert>

using namespace std;

#define MOD 1000000007

int strings;
int servers;
string str[10];
int which[10];
int maxn;
int cmax;

int countNodes(int server) {
    int ans = 1;
    int maxlen = 0;
    int i, j, k;
    for (i = 0; i < strings; i++)
        if (which[i] == server && str[i].length() > maxlen)
            maxlen = str[i].length();
    for (i = 1; i <= maxlen; i++) {
        string prefs[10];
        int prefCount = 0;
        for (j = 0; j < strings; j++) {
            if (which[j] != server || str[j].length() < i)
                continue;
            string pref = str[j].substr(0, i);
            for (k = 0; k < prefCount; k++)
                if (pref == prefs[k])
                    break;
            if (k == prefCount) {
                prefs[k] = pref;
                prefCount++;
                ans++;
            }
        }
    }
    return ans;
}

int main() {
    int T, TT;
    scanf("%d", &TT);
    for (T = 1; T <= TT; T++) {
        printf("Case #%d: ", T);
        scanf("%d %d", &strings, &servers);
        int i, j, k;
        char temp[50];
        for (i = 0; i < strings; i++) {
            scanf("%s", temp);
            str[i] = temp;
            which[i] = 0;
        }
        maxn = 0;
        cmax = 0;
        
        while (which[0] != servers) {
            
            for (j = 0; j < servers; j++) {
                for (k = 0; k < strings; k++) {
                    if (which[k] == j)
                        break;
                }
                if (k == strings)
                    break;
            }
            
            if (j == servers) {
                int nodes = 0;
                for (k = 0; k < servers; k++)
                    nodes += countNodes(k);
                if (nodes > maxn) {
                    maxn = nodes;
                    cmax = 0;
                }
                if (nodes == maxn)
                    cmax++;
            }
            
            
            which[strings-1]++;
            for (j = strings-1; j > 0 && which[j] == servers; j--) {
                which[j] = 0;
                which[j-1]++;
            }
            
        }
        
        printf("%d %d\n", maxn, cmax);
            
    }
}