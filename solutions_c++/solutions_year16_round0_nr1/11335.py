#include <bits/stdc++.h>

using namespace std;
set <int> numbers;

int travarse(int i, int n, set<int> s){
    // printf("travarse(%d, %d, set)\n", i, n);
    int nn = i*n;
    while(nn){
        s.insert(nn%10);
        nn/=10;
    }
    if(s.size() == 10){
        return i*n;
    }
    
    return travarse(i+1, n, s);
}

int main(){
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, cn = 1;
    cin>>T;
    while(T--){
        numbers.clear();
        int num;
        cin>>num;
        if( num == 0 ){
            printf("Case #%d: INSOMNIA\n",cn++);
            continue;
        }
        printf("Case #%d: %d\n",cn++, travarse(1, num, numbers));
    }
    
}