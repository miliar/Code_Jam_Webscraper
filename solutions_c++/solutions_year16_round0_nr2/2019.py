#include <iostream>

#include <queue>
#include <string>
#include <map>

#include <algorithm>

using namespace std;

string flip(string S, int k) {
   reverse(S.begin(), S.begin()+k);
   for (int i = 0; i < k; ++i)
      S[i] = S[i] == '-' ? '+' : '-';
   return S;
}

int bfs(string src) {
   queue<string> q;
   q.push(src);
   map<string, int> D;
   D[src] = 0;
   while (!q.empty()) {
      string cur = q.front();
      q.pop();
      int dist = D[cur];
      if (cur.find('-') == string::npos)
         return dist;
      for (int k = 1; k <= (int) cur.size(); ++k) {
         string nxt = flip(cur, k);
         if (D.count(nxt) == 0) {
            D[nxt] = dist + 1;
            q.push(nxt);
         }
      }
   }
   return -1;
}

int main(int argc, char* argv[]) {
   ios_base::sync_with_stdio(false); 
   cin.tie(NULL);

   int TC;
   cin >> TC;
   for (int tc = 1; tc <= TC; ++tc) {
      string S;
      cin >> S;
      int res = bfs(S);
      cout << "Case #" << tc << ": " << res << endl;
   }

   return 0;
}
