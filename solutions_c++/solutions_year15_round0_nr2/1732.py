#include <iostream>
#include <algorithm>
#include <queue>
#include <map>
using namespace std;

map<vector<int>, int> cache;

int process2(vector<int> &cakes) {
    if(cakes.empty()) return 0;
    if(cache.find(cakes) != cache.end()) return cache[cakes];
    int min = *max_element(cakes.begin(), cakes.end());
    int back = min;
    cakes.erase(find(cakes.begin(), cakes.end(), back));
    for(int i=1; i<=back/2; i++) {
        vector<int> temp(cakes);
        temp.push_back(i);
        temp.push_back(back - i); 
        min = std::min(min, 1 + process2(temp));
    }
    cakes.push_back(back);
    cache[cakes] = min;
    return min;
}

int process(vector<int> &cakes) {
    int min = *max_element(cakes.begin(), cakes.end());
    for(int i=1; i<=1000; i++) {
        int cur=0;
        for(int cake : cakes) {
            if(cake % i == 0) cur += cake/i - 1;
            else cur += cake/i;
        }
        min = std::min(min, cur + i);
    }
    return min;
}

int main() {
    int T;
    cin>>T;
    for(int tcas=1; tcas<=T; tcas++) {
        int M;
        cin>>M;
        vector<int> cakes;
        int cake;
        for(int i=0; i<M; i++) {
            cin>>cake;
            cakes.push_back(cake);
        }
        cache.clear();
        cache.clear();
        cout<<"Case #"<<tcas<<": "<<process(cakes)<<endl;
    }
}
        
