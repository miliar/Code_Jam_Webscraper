#include <bits/stdc++.h>

using namespace std;

char winner(char a, char b)
{
    assert(a != b);
    if (a > b) swap(a, b);
    if (a == 'P' && b == 'R') return 'P';
    if (a == 'P' && b == 'S') return 'S';
    return 'R';
}

string solve(int P, int R, int S, string priority)
{
    int n = P + R + S;
    
    if (n == 1)
    {
        if (P) return "P";
        if (R) return "R";
        if (S) return "S";
    }
    
    if ((R - P + S) % 2 != 0 || (P + S - R) % 2 != 0 || (R + S - P) % 2 != 0) return "";
    int p = (R + P - S) / 2, r = (R + S - P) / 2, s = (P + S - R) / 2;
    
    if (p < 0 || r < 0 || s < 0) return "";
    
    map<char, int> value;
    for (int i = 0; i < 3; i++)
        value[priority[i]] = i;
    
    string newPriority = string() +
        winner(priority[0], priority[1]) +
        winner(priority[0], priority[2]) +
        winner(priority[1], priority[2]);
        
    //printf("newp '%s'\n", newPriority.c_str());
    
    string up = solve(p, r, s, newPriority);
    string now = "";
    for (char c: up)
        if (c == 'P')
            now += value['P'] < value['R'] ? "PR" : "RP";
        else if (c == 'R')
            now += value['R'] < value['S'] ? "RS" : "SR";
        else
            now += value['P'] < value['S'] ? "PS" : "SP";
        
    return now;
}

void solve(int caseN)
{
    int n, P, R, S;
    scanf("%d %d %d %d", &n, &R, &P, &S);
    
    string s = solve(P, R, S, "PRS");
    if (s.empty()) s = "IMPOSSIBLE";
    
    printf("Case #%d: %s\n", caseN, s.c_str());
}

int main()
{
    int nt;
    scanf("%d", &nt);
    
    for (int i = 0; i < nt; i++)
        solve(i + 1);
    
    return 0;
}
