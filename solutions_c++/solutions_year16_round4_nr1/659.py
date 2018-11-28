
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <utility>
#include <queue>
#include <stack>
#include <set>
#include <map>

using namespace std ; 

typedef long long ll ; 

string minv(string s1, string s2){
    return s1 < s2 ? s1 : s2 ; 
}

int r, p, s, possible ; 
string mk(char win, int lay){
    if(lay == 0){
        if(win == 'R')
            r-- ; 
        if(win == 'P')
            p-- ; 
        if(win == 'S')
            s-- ; 
        string rtn ; 
        rtn += win ; 
        return rtn ; 
    }
    if(win == 'R'){
        string s1 = mk('R', lay-1) ; 
        string s2 = mk('S', lay-1) ; 
        return minv(s1+s2, s2+s1) ; 
    }
    else if(win == 'P'){
        string s1 = mk('P', lay-1) ; 
        string s2 = mk('R', lay-1) ; 
        return minv(s1+s2, s2+s1) ; 
    }
    else if(win == 'S'){
        string s1 = mk('S', lay-1) ; 
        string s2 = mk('P', lay-1) ; 
        return minv(s1+s2, s2+s1) ; 
    }
}

void sol(){
    int N, R, P, S ; 
    scanf("%d%d%d%d", &N, &R, &P, &S) ; 
    vector<string> ss ; 
    r = R ; 
    p = P ; 
    s = S ; 
    string ans = mk('R', N) ; 
    if(r == 0 && p == 0 && s == 0)
        ss.push_back(ans) ;
    r = R ; 
    p = P ; 
    s = S ; 
    ans = mk('P', N) ; 
    if(r == 0 && p == 0 && s == 0)
        ss.push_back(ans) ;
    r = R ; 
    p = P ; 
    s = S ; 
    ans = mk('S', N) ; 
    if(r == 0 && p == 0 && s == 0)
        ss.push_back(ans) ;
    sort(ss.begin(), ss.end()) ; 
    if(ss.empty())
        puts("IMPOSSIBLE") ; 
    else
        puts(ss[0].c_str()) ; 
}

int main()
{
    int T ; 
    scanf("%d", &T) ; 
    for(int time = 1 ; time <= T ; time++){
        fprintf(stderr, "solving case (%d / %d)...\n", time, T) ; 
        printf("Case #%d: ", time) ; 
        sol() ; 
    }
    return 0 ; 
}


