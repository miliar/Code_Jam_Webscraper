#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<vector>
#include<stack>
#include<map>
#include<queue>
#include<set>
using namespace std;
//int m[6];
//int ma[6];
bool impossible = false;

int solve(string s, int count,int k){
    if (s.size()<k) {
        for (int i = 0;  i<s.size(); i++) {
            if (s[i]=='-') {
                impossible = true;
                return -1;
            }
        }
        return count;
    }
    if (s[0] == '+') {
        return solve(s.substr(1), count,k);
    }
    else{
        for (int i=1; i<k; i++) {
            if (s[i]=='+') {
                s[i]='-';
            }
            else{
                s[i]='+';
            }
        }
        return 1+solve(s.substr(1), count,k);
    }
}

int main()
{
    freopen ("/Users/Victor/Desktop/myfile.txt","w",stdout);
    freopen ("/Users/Victor/Desktop/A-large.in","r",stdin);
    int T;
    cin >> T;
    for (int i=0; i<T; i++) {
        string S;
        int K;
        cin >> S >> K;
        impossible = false;
        int ans = solve(S, 0, K);
        
        if (impossible) {
            cout << "Case #"<<i+1<<": IMPOSSIBLE"<< endl;
        }
        else{
            cout << "Case #"<<i+1<<": "<<ans<< endl;
        }
    }
    return 0;
}

