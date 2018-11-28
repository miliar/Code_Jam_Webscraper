#include <iostream>
#include <cstdio>
#include <cassert>
#include <cstring>
#include <vector>
#include <valarray>
#include <array>
#include <queue>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <cmath>
#include <complex>
#include <random>

using namespace std;

typedef unsigned long long ll;

int main() {
    freopen("/Users/shitian/Desktop/gcj/gcj/A-large.in", "r", stdin);
    freopen("/Users/shitian/Desktop/gcj/gcj/out.txt", "w", stdout);
    
    int tcase;
    cin>>tcase;
    for(int tca=1;tca<=tcase;tca++){
        cout<<"Case #"<<tca<<": ";
        
        int p;
        priority_queue<pair<int,int> >que;
        cin>>p;
        int all=0;
        for(int i=0;i<p;i++){
            int j;
            cin>>j;
            all+=j;
            que.push(make_pair(j,i));
        }
        while(all){
            pair<int,int>t=que.top();
            que.pop();
            t.first-=1;
            all-=1;
            char c='A'+t.second;
            cout<<c;
            if(que.size()){
                pair<int,int>t2=que.top();
                if(t2.first>all/2){
                    all-=1;
                    t2.first-=1;
                    que.pop();
                    char c2='A'+t2.second;
                    cout<<c2;
                    if(t2.first>0)que.push(t2);
                }
            }
            if(t.first>0){
                que.push(t);
            }
            cout<<" ";
        }
        cout<<endl;
    }
    return 0;
}