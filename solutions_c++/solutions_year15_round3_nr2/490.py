#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <cmath>
#include <string>
#include <algorithm>
#include <cstdio>
#include <ctime>
#include <climits>


using namespace std;

map<char, int> u;
string c, b;
int l, s, k;
long double mm;

long double solve(int r, string q, long double p){
    if (r == 0){ 
        long double num = 0.0;
        for (int j=0;j<s-l+1;j++){
            bool f = true;
            for (int i=0;i<l;i++)
                if (b[i] != q[j+i])
                    f = false;
            if (f)
                num++;
        }
        if (mm < num)
            mm = num;
        return p*num;
    }
    long double res = 0;
    for (int i=0;i<c.length();i++){
        string w;
        for (int j=0;j<q.length();j++)
            w.push_back(q[j]);
        w.push_back(c[i]);
        res += solve(r-1, w, p*u[c[i]]*1.0/k);
    }
    return res;
}

int main(){
	freopen("/Users/Arseniy/All/A/input.txt", "r", stdin);
    freopen("/Users/Arseniy/All/A/output.txt", "w", stdout);
    int t;
    cin >> t;
    cout.precision(20);
    for (int o=0;o<t;o++){
    	cout << "Case #" << o+1 << ": ";
        cin >> k >> l >> s;
        string a;
        cin >> a >> b;
        c = "";
        
        u.clear();
        for (int i=0;i<a.length();i++){
            if (!u[a[i]])
                c.push_back(a[i]);
            u[a[i]]++;
        }
        mm = 0;
        long double ans =solve(s, "", 1);
        cout << mm - ans << endl;
    }
	return 0;
}