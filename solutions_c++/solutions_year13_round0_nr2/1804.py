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

int n,m;

int findMin(vector<vector<int> > f){
    int ret = (1ll << 31) - 1;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            ret = min(ret, f[i][j]);
        }
    }
    return ret;
}



int main(){
    int cases;

    cin >> cases;
    for(int x=0;x<cases;x++){
        bool ret = true;
        cin >> n >> m;
        vector<vector<int> > f(n, vector<int>(m, 0));
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                cin >> f[i][j];
            }
        }
        while(1){
            vector<vector<int> > minMap(n, vector<int>(m, 0));
            vector<vector<int> > mask(n, vector<int>(m, 0));
            int min = findMin(f);
            if(min == 100) break;
            for(int i=0;i<n;i++){
                for(int j=0;j<m;j++){
                    if(f[i][j] == min){
                        minMap[i][j] = 1;
                    }
                }
            }
            //for each rows
            for(int i=0;i<n;i++){
                bool isok = true;
                for(int j=0;j<m;j++){
                    if(f[i][j] != min){
                        isok = false;
                        break;
                    }
                }
                if(isok){
                    for(int j=0;j<m;j++){
                        mask[i][j] = 1;
                    }
                }
            }
            //for each cols;
            for(int i=0;i<m;i++){
                bool isok = true;
                for(int j=0;j<n;j++){
                    if(f[j][i] != min){
                        isok = false;
                        break;
                    }
                }
                if(isok){
                    for(int j=0;j<n;j++){
                        mask[j][i] = 1;
                    }
                }
            }
            //compare minMap and mask
            bool isok = true;
            for(int i=0;i<n && isok ;i++){
                for(int j=0;j<m && isok ;j++){
                    if(minMap[i][j] != mask[i][j]){
                        isok = false;
                    }
                }
            }
            if(isok){
                for(int i=0;i<n;i++){
                    for(int j=0;j<m;j++){
                        if(f[i][j] == min) f[i][j]++;
                    }
                }
            }else{
                ret = false;
                break;
            }
        }
        cout << "Case #" << x+1 << ": ";
        if(ret == true){
            cout << "YES" << endl;
        }else{
            cout << "NO" << endl;
        }
    }
}
