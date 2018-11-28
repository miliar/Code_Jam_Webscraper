#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <cmath>
#include <vector>

using namespace std;
typedef long long ll;

ifstream in("input.txt");
ofstream out("output.txt");
vector<ll> pows;

pair<ll, ll> getNum(string s) {
    ll a, b;
    int i = 0;
    a = 0;
    b = 0;
    while (i < s.size() && s[i] != '/') {
        a = a * 10 + (s[i] - 48);
        i++;
    }
    i++;
    while (i < s.size()) {
        b = b * 10 + (s[i] - 48);
        i++;
    }
    return make_pair(a, b);
}

ll gcd (ll a, ll b) {
	return b ? gcd (b, a % b) : a;
}

int main()
{
    int t;
    in >> t;
    pows = vector<ll>(41);
    pows[0] = 1;
    for (int i = 1; i < 41; i++)
        pows[i] = pows[i - 1] * 2;
    for (int test = 0; test < t; test++) {
        string str;
        in >> str;
        ll p, q;
        pair<ll, ll> pr = getNum(str);
        p = pr.first;
        q = pr.second;
        ll g = gcd(p, q);
        p /= g;
        q /= g;
        int cnt = 0;
        int cnt2 = 0;
        ll pw = 1;
        for (; p >= pw; pw *= 2, cnt2++);
        for (;q % 2 == 0; q /= 2, cnt++);
        out << "Case #" << test + 1 << ": ";
        if (q == 1)
            out  << (pows[cnt - 1] < p ? 1 : cnt - cnt2 + 1) << endl;
        else
            out << "impossible" << endl;
    }
    in.close();
    out.close();
    return 0;
}


        /*



                p /= q;
        set<double> s = set<double>();
        set<double> s_tmp = set<double>();
        map<double, double> m = map<double, double>();
        s.insert(1);
        s.insert(0);
        for (int d = 0; d < 40; d++) {
            if (s.find(p) != s.end())
                cerr << d << endl;
            set<double>::iterator i = s.begin();
            set<double>::iterator j;
            s_tmp.clear();
            for (; i != s.end(); i++)
                for (j = s.begin(); j != s.end(); j++) {
                    s_tmp.insert((*i + *j) / 2);
                }

//            for (j = s_tmp.begin(); j != s_tmp.end(); j++)
//                cerr << *j << endl;
            s = s_tmp;
        }
        */
