#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>

using namespace std;

#define dump(x)  cerr << #x << " = " << (x) << endl;
#define PB push_back
#define MP make_pair
#define ll long long

inline int toInt(string s){int v;istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x){ostringstream sout;sout<<x;return sout.str();}

int main(){
    int cases;
    cin >> cases;

    for(int x=1;x<=cases;x++){
        int before = 0;
        int after = 0;
        int n,m,s,e,p;

        cin >> n >> m;
        vector<int> num(n,0);
        for(int i=0;i<m;i++){
            cin >> s >> e >> p;
            for(int k=s-1;k<e-1;k++){
                num[k] += p;
            }
            before += (e-s)*(e-s-1)/2 * p;
        }
        while(1){
            bool ended = true;
            int begin;
            for(int i=0;i<n;i++){
                if(num[i] != 0){
                    ended = false;
                    begin = i;
                    break;
                }
            }
            if(ended) break;
            int contnum = 0;
            for(int i=begin;i<n && num[i] > 0;i++){
                contnum++;
                num[i]--;
            }
            after += contnum * (contnum - 1) / 2;
        }
        cout << "Case #" << x << ": " << after - before << endl;
    }
}
