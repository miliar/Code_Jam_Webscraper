#include <iostream>
#include <string>
#include <set>
#define forn(i,x,y) for(int i=x;i<y;i++)

using namespace std;

set<int> p;
set<int> f;
set<int>::iterator it;

int str_to_num(string s) {
    int res = 0;
    forn(i,0,s.size())
        res = res*10 + (s[i] - '0');
    return res;
}

void calc_nums(void) {
    string n = "0123456789";
    forn(i,0,10) p.insert(i);
    forn(a,1,10) forn(b,0,10) forn(c,0,10) forn(d,0,10) {
        string s = "";
        s+= n[a]; s+=n[b]; s+=n[c]; s+=n[d]; s+=n[c];s+=n[b]; s+=n[a];
        p.insert(str_to_num(s));
        s = ""; s += n[a]; s+=n[b];s+=n[c];s+=n[c];s+=n[b];s+=n[a];
        p.insert(str_to_num(s));
        s = ""; s +=n[a]; s+=n[b];s+=n[c];s+=n[b];s+=n[a];
        p.insert(str_to_num(s));
        s = ""; s +=n[a];s+=n[b];s+=n[b];s+=n[a];
        p.insert(str_to_num(s));
        s = ""; s +=n[a];s+=n[b];s+=n[a];
        p.insert(str_to_num(s));
        s = ""; s +=n[a];s+=n[a];
        p.insert(str_to_num(s));
    }
    for(it = p.begin(); it != p.end(); it++) {
        int a = *it;
        if(p.count(a*a))
            f.insert(a*a);
    }
}


int main(void) {
    calc_nums();
    int tests; cin >> tests;
    forn(t,1,tests+1) {
        unsigned long long int a,b; cin >> a >> b;
        int res = 0;
        for(it = f.begin(); it != f.end(); it++)
            if(*it >= a && *it <= b) res++;
        cout << "Case #" << t << ": " << res << endl;
    }
}
