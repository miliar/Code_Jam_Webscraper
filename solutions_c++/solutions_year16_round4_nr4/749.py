#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string.h>
using namespace std;

void useFile(const string& str = "")
{
    if(str != "" && str != "std"){
        freopen( (str+".in").c_str(), "r", stdin );
        freopen( (str+".out").c_str(), "w", stdout);
    }
}

int lowbit(int x){
    return x & (-x);
}

int cnt_bit(int a)
{
    int cnt = 0;
    while (a != 0){
        a = a - lowbit(a);
        cnt++;
    }
    return cnt;
}

int get_bin(vector<int> & a)
{
    int x = 0;
    for (int i = 0; i < a.size(); i++){
        if (a[i]) {
            x = x | (1 << i);
        }
    }
    return x;
}

bool check(vector<vector<int> >& a)
{
    int n = a.size();
    vector<int> s;
    vector<int> bit_num;
    for (int i = 0; i < n; i++){
        s.push_back(get_bin(a[i]));
        bit_num.push_back(cnt_bit(s[i]));
    }
    for (int i = 0; i < n; i++){
        int cnt = 0;
        for (int j = 0; j < n; j++){
            if (s[i] == s[j]){
                cnt++;
            }else{
                if (s[j] & s[i]){
                    return false;
                }
            }
        }
        if (cnt != bit_num[i]){
            return false;
        }
    }
    return true;
}

int calc(vector<string> & work)
{
    int n = work.size();
    int N = n * n;
    vector<vector<int> > vec(n);

    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            vec[i].push_back(work[i][j] - '0');
        }
    }

    int min_ans = N;
    for (int bit = 0; bit < (1<<N); bit++){
        bool need_calc = true;
        auto s = vec;
        int cost = 0;
        for (int i = 0; i < N; i++){
            int x = i / n;
            int y = i % n;
            if (s[x][y] == 0 && ((bit >> i) & 1) == 1){
                cost++;
                s[x][y] = 1;
            }else if (s[x][y] == 1 && ((bit >> i) & 1) == 0){
                need_calc = false;
                break;
            }
        }
        if (need_calc && check(s)){
            min_ans = min(min_ans, cost);
        }
    }
    return min_ans;
}

int main(){
    useFile("D1");
    int T = 0;
    cin >> T;
    for(int ca = 1; ca <= T; ca++){
        int N;
        cin >> N;
        std::vector<string> vec;
        for (int i = 0; i < N; i++){
            string a;
            cin >> a;
            vec.push_back(a);
        }
        cout << "Case #" << ca << ": " << calc(vec) << endl;
    }
}
