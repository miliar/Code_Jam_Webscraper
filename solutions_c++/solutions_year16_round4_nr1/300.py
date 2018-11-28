#include <bits/stdc++.h>
using namespace std;

/*
bool check(string who) {
    string T = who;
    while(T.size() > 1) {
        int n = T.size();
        for(int i = 0; i < n; i += 2)
            if(T[i] == T[i + 1])
                return false;
            else tmp += win(T[i], T[i + 1]);
        T = tmp;
    }

    return true;
}*/

string getSol(int n, int r, int p, int s) {
    
    if(n == 0) {
        if(r == 1)
            return "R";
        else if(p == 1)
            return "P";
        return "S";
    }

    vector<string> sol;

    for(int many = 0; many <= p && many <= s; ++many) {
        if((s - many) > r)
            continue;
        if((p - many) != r - (s - many))
            continue;
        
        string who = "";
        for(auto temp : sol)
            who += temp;
            
        int newR = s - many;
        int newP = p - many;
        int newS = many;

        string best = getSol(n - 1, newR, newP, newS);
        if(best == "IMPOSSIBLE")
            return "IMPOSSIBLE";
        return best;
    }

    return "IMPOSSIBLE";
}

map<pair<int, char>, string> M;

string getMin(int n, char c) {

    if(M.find({n, c}) != M.end())
        return M[make_pair(n, c)];

    if(n == 0)
        return string(1, c);
    
    char lf = 'a', rt = 'b';

    if(c == 'R')
        lf = 'R', rt = 'S';
    else if(c == 'S')
        lf = 'S', rt = 'P';
    else
        lf = 'P', rt = 'R';

    string L = getMin(n - 1, lf);
    string R = getMin(n - 1, rt);

    if(L < R) {
        L += R;
        M[make_pair(n, c)] = L;
        return L;
    } else {
        R += L;
        M[make_pair(n, c)] = R;
        return R;
    }
}

char win(char a, char b) {
    if(a > b)
        swap(a, b);

    if(a == 'P' && b == 'R')
        return 'P';

    if(a == 'P' && b == 'S')
        return 'S';

    if(a == 'R' && b == 'S')
        return 'R';
}

string brut(int n, int r, int p, int s) {
    string A(p, 'P');
    string B(r, 'R');
    string C(s, 'S');

    A += B;
    A += C;
    
    string ans = "Z";

    do {
        bool can = true;
        string T = A;
        while(T.size() > 1) {
            int m = T.size();
            string temp;
            for(int i = 0; i < m; i += 2)
                if(T[i] == T[i + 1]) {
                    can = false;
                    break;
                } else temp += win(T[i], T[i + 1]); 
            if(!can)
                break;
            T = temp;
        }
        if(can)
            ans = min(ans, A);
    } while(next_permutation(A.begin(), A.end()));

    if(ans == "Z")
        return "IMPOSSIBLE";
    return ans;
}

int main() {

    ifstream cin("testA.in");
    ofstream cout("testA.out");

    int t; cin >> t;

    for(int t_case = 1; t_case <= t; ++t_case) {
        cout << "Case #" << t_case << ": ";
        cerr << t_case << "\n";

        int n, r, p, s; cin >> n >> r >> p >> s;
        
        string winner = getSol(n, r, p, s);
        string lineUp;

        if(winner == "IMPOSSIBLE")
            lineUp = "IMPOSSIBLE";
        else
            lineUp = getMin(n, winner[0]);

        cout << lineUp << "\n";
    }
}
