//
// Created by elvis on 2016/4/9.
//
#include<iostream>
#include <fstream>
#include <set>
//#define ONLINE_JUDGE
using namespace std;

int main(){
#ifndef ONLINE_JUDGE
    ifstream cin("A-small-attempt0.in");
    ofstream out("A-small.out");
#else
    // online submission
#endif
    int n;
    cin >> n;
    int num[n];
    for(int i = 0; i < n; i ++){
        cin >> num[i];
    }

    long long ans, tmp;
    for (int i = 0; i < n; ++i) {
        if(num[i]==0) {
            cout<<"Case #"<<(i+1)<<": INSOMNIA"<<endl;
            out<<"Case #"<<(i+1)<<": INSOMNIA"<<endl;
            continue;
        }
        set<int> s;
        int j = 1;
        while(1){
            tmp = num[i]*j;
            ans = tmp;
            while(tmp!=0){
                s.insert(tmp%10);
                tmp/=10;
            }
            if(s.size()>9) {
                break;
            }
            j++;
        }
        cout<<"Case #"<<(i+1)<<": "<<ans<<endl;
        out<<"Case #"<<(i+1)<<": "<<ans<<endl;
    }
    return 0;
}
