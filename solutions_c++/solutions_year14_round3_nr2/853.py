#include <iostream>
#include <string>
#include <algorithm>
#include <cstdio>
using namespace std;

int ans;
string train[20];
int T,N;
bool visited[20];

void backtrack(string str, int num)
{
    if (num == N) {
        char a = str[0];
        int b[150] = {0};
        b[str[0]] = 1;
        for (int i = 1; i < str.size(); ++i) {
            if (str[i] != str[i-1] && b[str[i]])
                return;
            else ++b[str[i]];
        }
      //  cout << str << endl;
        ++ans;
        return;
    }
    for (int i = 0; i < N; ++i) {
        if (visited[i]) continue;

        visited[i] = true;
        backtrack(string(str+train[i]), num+1);
       // if (!str.empty()) backtrack(string(train[i]+str), num+1);
        visited[i] = false;
    }
}

int main()
{
    freopen("B-small-attempt0.in", "rt", stdin);
    freopen("Bout.txt", "wt", stdout);

    int Case = 1;
    cin >> T;
    while (T--) {
        cin >> N;
        for (int i = 0; i < N; ++i)
            cin >> train[i];

        ans = 0;
        fill(visited, visited+N, 0);
        backtrack(string(""),0);

        cout << "Case #" << Case++ << ": " << ans << endl;
    }
}
