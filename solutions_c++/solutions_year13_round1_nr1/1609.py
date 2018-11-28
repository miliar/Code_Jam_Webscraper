#include <stdio.h>
#include <string.h>
#include <utility>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <bitset>
using namespace std;
#define MAX_V 210

struct State {
    int position;
    bitset<21> visited;
    vector<int> keys;

    bool operator<(const State rhs) const {
        if (position == rhs.position) {
            if (visited.count() == rhs.visited.count()) {
            //if (visited.to_ulong() == rhs.visited.to_ulong()) {
                return keys < rhs.keys;
            }
            return visited.count() < rhs.visited.count();
            //return visited.to_ulong() < rhs.visited.to_ulong();
        }
        return position > rhs.position;
    }

    State() {
        position = 0;
        keys.resize(41);
    }

    bool operator==(const State rhs) const {
        return position == rhs.position && visited == rhs.visited && keys == rhs.keys;
    }
};

int testcase = 0;
void run()
{
    vector<int> initial_keys;
    initial_keys.resize(41);
    int k, n;
    scanf("%d%d", &k, &n);
    vector<int> start;
    for (int i = 0; i < k; ++i) {
        int key;
        scanf("%d", &key);
        start.push_back(key);
        ++initial_keys[key];
    }
    vector<int> chests_from_key[MAX_V+1];
    vector<int> keys_from_chest[MAX_V+1];
    for (int chest = 1; chest <= n; ++chest) {
        int necessary_key, qtd;
        scanf("%d%d", &necessary_key, &qtd);
        chests_from_key[necessary_key].push_back(chest);
        while (qtd--) {
            int key;
            scanf("%d", &key);
            keys_from_chest[chest].push_back(key);
        }
    }

    State invalid;
    invalid.position = -1;
    State blank;

    map<State, State> prev;
    priority_queue<State> q;
    for (int i = 0; i < k; ++i) {
        int key = start[i];
        for (int j = 0, size = chests_from_key[key].size(); j < size; ++j) {
            int v = chests_from_key[key][j];
            State st;
            st.position = v;
            st.visited[v] = true;
            st.keys = initial_keys;
            --st.keys[key];
            for (int i = 0, size = keys_from_chest[v].size(); i < size; ++i) {
                int new_key = keys_from_chest[v][i];
                ++st.keys[new_key];
            }
            prev[st] == invalid;
            q.push(st);
        }
    }

    State fim = invalid;
    while (!q.empty()) {
        State st = q.top();
        q.pop();

        if (st.visited.count() == n) {
            fim = st;
            break;
        }

        for (int key = 1; key <= 40; ++key) {
            if (st.keys[key]) {
                for (int j = 0, size = chests_from_key[key].size(); j < size; ++j) {
                    int next = chests_from_key[key][j];
                    if (st.visited[next] == false) {
                        State new_state;
                        new_state.position = next;
                        new_state.visited = st.visited;
                        new_state.visited[next] = true;
                        new_state.keys = st.keys;
                        --new_state.keys[key];
                        for (int i = 0, size = keys_from_chest[next].size(); i < size; ++i) {
                            int new_key = keys_from_chest[next][i];
                            ++new_state.keys[new_key];
                        }

                        if (prev[new_state] == blank) {
                            q.push(new_state);
                            prev[new_state] = st;
                        }
                    }
                }
            }
        }
    }
    if (fim == invalid)
        puts(" IMPOSSIBLE");
    else {
        stack<int> pos;
        State st = fim;
        while (!(st == blank || st == invalid)) {
            pos.push(st.position);
            st = prev[st];
        }
        while (!pos.empty()) {
            printf(" %d", pos.top());
            pos.pop();
        }
        putchar('\n');
    }
}

int main()
{
    #if 1
    freopen("input1.txt", "r", stdin);
    freopen("output1.txt", "w+", stdout);
    #endif // ONLINE_JUDGE

	int testcases;
	scanf("%d", &testcases);
	for (testcase = 1; testcase <= testcases; ++testcase)
	{
	    printf("Case #%d:", testcase);
		run();
	}
	return 0;
}
