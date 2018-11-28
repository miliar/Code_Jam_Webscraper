#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

int main()
{
    int T = 0, cnt = 0;
    cin>>T;
    while (T--) {
        cnt++;
        map <int, int> mp;
        int N;
        cin>>N;
        int tmp = 0;
        for (int i = 0; i < (2*N - 1); i++) {
            for (int j = 0; j < N; j++) {
                cin>>tmp;
                if (mp.find(tmp) == mp.end())
                    mp[tmp] = 1;
                else
                    mp[tmp]++;
            }
        }
        printf("Case #%d: ", cnt);
        for (auto k = mp.begin(); k != mp.end(); k++) {
            if (k->second % 2)
                printf("%d ", k->first);
        }
        printf("\n");
    }
    return 0;
}
