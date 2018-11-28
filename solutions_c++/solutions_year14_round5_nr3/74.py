#include <cstdio>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cassert>

using namespace std;

int n;
bool in[15];
int id[15];
vector<int> ids;
int tid[15];
int minIn;

void check() {
    //first see if its possible, ie, no one enters who is alrady in
    int numIn = 0;
    int inside[15];
    int numOut = 0;
    int outside[15];
    int unknownIn = 0;
    int i, j;
    for (i = 0; i < n; i++) {
        if (in[i]) {
            if (tid[i] == 0) {
                unknownIn++;
                continue;
            }
            for (j = 0; j < numIn; j++)
                if (inside[j] == tid[i])
                    return;
            inside[numIn] = tid[i];
            numIn++;
            for (j = 0; j < numOut; j++) {
                if (outside[j] == tid[i]) {
                    outside[j] = outside[numOut-1];
                    numOut--;
                }
            }
        } else {
            if (tid[i] == 0) {
                unknownIn = max(unknownIn - 1, 0);
                continue;
            }
            for (j = 0; j < numOut; j++)
                if (outside[j] == tid[i])
                    return;
            outside[numOut] = tid[i];
            numOut++;
            for (j = 0; j < numIn; j++) {
                if (inside[j] == tid[i]) {
                    inside[j] = inside[numIn-1];
                    numIn--;
                }
            }
        }
    }
    if (unknownIn + numIn < minIn)
        minIn = unknownIn + numIn;
}

void bruteforce(int where) {
    if (where == n) {
        check();
        return;
    }
    tid[where] = id[where];
    if (id[where] != 0) {
        bruteforce(where+1);
        return;
    }
    int i;
    for (i = 0; i < ids.size(); i++) {
        tid[where] = ids[i];
        bruteforce(where+1);
    }
}

int main() {
    int T, TT;
    scanf("%d", &TT);
    for (T = 1; T <= TT; T++) {
        printf("Case #%d: ", T);
        
        scanf("%d", &n);
        char temp[2];
        int i, j;
        ids.clear();
        for (i = 0; i < n; i++) {
            scanf("%s %d", temp, &id[i]);
            in[i] = temp[0] == 'E';
            for (j = 0; j < ids.size(); j++)
                if (ids[j] == id[i])
                    break;
           if (j == ids.size())
               ids.push_back(id[i]);
        }
        
        minIn = 1000000;
        bruteforce(0);
        if (minIn == 1000000)
            printf("CRIME TIME\n");
        else
            printf("%d\n", minIn);
            
    }
}