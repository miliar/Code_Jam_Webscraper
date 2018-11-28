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
        int dx, dy;
        cin >> dx >> dy;
        string ret = "";

        if(dx > 0){
            dx--;
            ret += 'E';
            while(dx > 0){
                ret += "WE";
                dx--;
            }
        }else if(dx < 0){
            dx++;
            ret += 'W';
            while(dx < 0){
                ret += "EW";
                dx++;
            }
        }
        if(dy > 0){
            while(dy > 0){
                dy--;
                ret+= "SN";
            }
        }else if(dy < 0){
            while(dy < 0){
                ret += "NS";
                dy++;
            }
        }
        cout << "Case #" << x << ": " << ret << endl;
    }
}
