// compile in C++11. use -std=c++11.
#include <iostream>
#include <iomanip>
#include <vector>
#include <valarray>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <stack>
#include <bitset>
#include <utility>
#include <numeric>
#include <algorithm>
#include <functional>
#include <complex>
#include <string>
#include <sstream>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>

// this require C++11
#include <unordered_set>
#include <unordered_map>
#include <random>

using namespace std;

#define all(c) c.begin(),c.end()
#define repeat(i,n) for(int i=0;i<static_cast<int>(n);i++)
#define debug(x) #x << "=" << (x)
#define dump(x) cerr << debug(x) << " (L:" << __LINE__ << ")"<< endl

using ll = long long;

template<typename T>
ostream& operator<<(ostream& os,const vector<T>& vec){
    os << "[";
    for(const auto& v : vec){
        os << v << ",";
    }
    os << "]";
    return os;
}

template<typename T>
T input(){
    T t;cin >> t;
    return t;
}

template<typename T>
vector<T> input(const int N){
    vector<T> v(N);
    repeat(i,N) cin >> v[i];
    return v;
}

const string multiple = "Bad magician!";
const string noans = "Volunteer cheated!";

string solve(int first,int second,vector<vector<int>> first_board,vector<vector<int>> second_board){
    map<int,int> cnt;
    for(int i : first_board[first]){
        cnt[i]++;
    }
    for(int i : second_board[second]){
        cnt[i]++;
    }
    vector<int> ans;
    for(pair<int,int> p : cnt){
        if(p.second == 2){
            ans.push_back(p.first);
        }
    }
    if(ans.size() >= 2){
        return multiple;
    }else if(ans.size() == 1){
        string ret;
        stringstream ss;
        ss << ans.front();
        ss >> ret;
        return ret;
    }else{
        return noans;
    }
}

int main(){
    int T;cin >> T;
    for(int test=1;test<=T;test++){
        int first,second;
        vector<vector<int>> board1(4,vector<int>(4)),board2(4,vector<int>(4));
        cin >> first;
        repeat(r,4){
            repeat(c,4){
                cin >> board1[r][c];
            }
        }
        cin >> second;
        repeat(r,4){
            repeat(c,4){
                cin >> board2[r][c];
            }
        }
        first--;second--;
        string ans = solve(first,second,board1,board2);
        cout << "Case #" << test << ": " << ans << endl;
    }
    return 0;
}
