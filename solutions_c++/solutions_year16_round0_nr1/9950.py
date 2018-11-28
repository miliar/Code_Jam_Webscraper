#include<cmath>
#include<cstdlib>
#include<string>
#include<sstream>
#include<vector>
#include<iostream>
#include<queue>
#include<deque>
#include<map>
#include<set>
#include<stack>
#include<list>
#include<algorithm>
using namespace std;

vector<int> digit_numbers(int n){
    vector<int> v;
    if(n==0) v.push_back(0);
    while(n>0){
        v.push_back(n%10);
        n /= 10;
    }
    return v;
}

int main(){
    int T;
    cin >> T;
    set<int> s;
    for(int t=1; t<=T; t++){
        int n;
        cin >> n;
        int ans;
        if(n==0){
            cout << "Case #" << t << ": " << "INSOMNIA" << endl;
        }
        else{
            int m;
            int k = 1;
            while(s.size() < 10){
                m = n * k;
                vector<int> v = digit_numbers(m);
                for(int i=0; i<v.size(); i++) s.insert(v[i]);
                k++;
            }
            cout << "Case #" << t << ": " << m << endl;
            s.clear();
        }
    }
}
