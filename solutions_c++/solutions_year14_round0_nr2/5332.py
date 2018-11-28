#include <vector>
#include <cmath>
#include <cstdio>
#include <list>
#include <cctype>
#include <cstring>
#include <iomanip>
#include <stack>
#include <map>
#include <iostream>
#include <string>
#include <set>

using namespace std;

double c,f,x;

double dfs(double fre) {
    if (x/(fre+f) < (x-c)/fre)
        return c/fre + dfs(fre+f);
    else 
        return x/fre;
}

void func() {
    cin >> c >> f >> x;
    cout.precision(7);
    cout.setf(ios::fixed); 

    double tt = 0.0;
    double fre = 2.0;
    while (x/(fre+f) < (x-c)/fre) {
        tt += c/fre;
        fre = fre+f;
    }
    tt += x/fre;


    cout << tt << endl;
}


//////////////////////////////

char in_file[] = "B-large.in";
char out_file[] = "test.out";

int main() {
    int case_count, t;

    freopen(in_file, "r", stdin);
    freopen(out_file,"w", stdout);

    cin >> case_count;
    string s;
    getline(cin, s);
    for (t = 1; t <= case_count; t++) {
        cerr << "\nDealing Case #" << t << endl;
        cout << "Case #" << t << ": ";
        func();
    }

	return 0;    
}
