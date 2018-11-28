#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

set<int>& filter(set<int>& st, long long n){
    while(n > 0){
        st.erase(n%10);
        n/= 10;
    }
    return st;
}

long long solve(long long n){
    int digits[] = {0,1,2,3,4,5,6,7,8,9};
    set<int> was(digits, digits+10);
    for(long long i = 1; i < 1000000; i++){
        if(filter(was, n*i).empty()){
            return i*n;
        }
    }
    return -1;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    long long n;
    int digits[] = {0,1,2,3,4,5,6,7,8,9};
    set<int> was(digits, digits+10);
    int T;
    cin >> T;
    for(int qqq = 1; qqq <= T; qqq++){
        long long t;
        cin >> t;
        t = solve(t);
        cout << "Case #" << qqq << ": ";
        if(t == -1){
            cout << "INSOMNIA" << endl;
        }else{
            cout << t << endl;
        }
    }
    return 0;
}
