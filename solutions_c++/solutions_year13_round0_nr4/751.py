#include <iostream>
using namespace std;
bool visited[1048576];
int T,K,N;
//int init_keycounts[2000];
int keycounts[200];
int chest_keycounts[20][200];
int lock_type[20];
int order[20];

int dfs(int state, int idx) {
    if(visited[state])
        return 0;
    if(idx == N)
        return 1;
    visited[state] = true;
    for(int i=0;i<N;++i) {
        if(((state & (1<<i)) == 0) && (keycounts[lock_type[i]] > 0)) {
            keycounts[lock_type[i]]--;
            for(int j=0;j<200;++j)
                keycounts[j] += chest_keycounts[i][j];
            order[idx] = i;
            if(dfs(state | (1 << i), idx + 1))
                return 1;
            for(int j=0;j<200;++j)
                keycounts[j] -= chest_keycounts[i][j];
            keycounts[lock_type[i]]++;
        }
    }
    return 0;
}

int main()
{
    cin >> T;
    for(int qq=0;qq<T;++qq) {
        memset(keycounts, 0, 200*sizeof(int));
        memset(chest_keycounts, 0, 4000*sizeof(int));
        memset(visited, 0, 1048576*sizeof(bool));
        cin >> K >> N;
        int keytype;
        for (int i=0;i<K;++i)
        {
            cin >> keytype;
            keycounts[keytype-1]++;
        }
        int nkeys_this_chest;
        for(int i=0;i<N;++i)
        {
            cin >> lock_type[i];
            lock_type[i]--;
            cin >> nkeys_this_chest;
            for(int j=0;j<nkeys_this_chest;++j)
            {
                cin >> keytype;
                chest_keycounts[i][keytype-1]++;
            }
        }
        if(dfs(0,0)) {
            cout << "Case #" << (qq+1) << ":";
            for (int i=0; i<N;++i)
                cout << " " << (order[i]+1);
            cout << endl;
        } else {
            cout << "Case #" << (qq+1) << ": IMPOSSIBLE" << endl;
        }
    }
}
