#include <bits/stdc++.h>
using namespace std;

int main() {
    
    ifstream cin("testC.in");
    ofstream cout("testC.out");

    int t; cin >> t;
    for(int t_case = 1; t_case <= t; ++t_case) {
        cout << "Case #" << t_case << ": ";
        
        int n; cin >> n;
        string english, french;
        getline(cin, english);
        getline(cin, english);
        getline(cin, french);

        istringstream englishss(english), frenchss(french);

        map<string, int> M;
        vector<vector<int>> type(2005 + n * 20, vector<int>(2, 0));
        int m = 0;

        string word;
        while(englishss >> word) {
            M[word] = m++;
            type[M[word]][0] = 1;
        }

        while(frenchss >> word) {
            if(M.find(word) == M.end()) {
                M[word] = m++;
            }
            type[M[word]][1] = 1;
        }
        
        vector<vector<int>> A(n - 2, vector<int>());

        for(int i = 0; i < n - 2; ++i) {
            string line; getline(cin, line);
            istringstream currentLine(line);
            string temp;

            while(currentLine >> temp) {
                if(M.find(temp) == M.end()) 
                    M[temp] = m++;
                A[i].push_back(M[temp]);
            }
        }

        unordered_set<int> already;
        for(int i = 0; i < m; ++i)
            if(type[i][0] == 1 && type[i][1])
                already.insert(i);
 
        int ans = 1e6;
        
        cerr << t_case << "\n";

        for(int mask = 0; mask < (1 << (n - 2)); ++mask) {
            unordered_set<int> E, F;

            for(int i = 0; i < n - 2; ++i)
                if((1 << i) & mask) {
                    for(auto temp : A[i]) {
                        if(type[temp][1])
                            F.insert(temp);
                        E.insert(temp);
                    }
                } else {
                    for(auto temp : A[i]) {
                        if(type[temp][0])
                            E.insert(temp);
                        F.insert(temp);
                    }
                }
            
            unordered_set<int> both;

            for(auto temp : E)
                if(F.find(temp) != F.end())
                    both.insert(temp);
            
            int tmp = already.size() + both.size();
            for(auto temp : both)
                if(already.find(temp) != already.end())
                    tmp--;
            
            ans = min(ans, tmp);
        }

        cout << ans << "\n";
    }
}
