#include <bits/stdc++.h>

using namespace std;

int vis[1 << 15];

void setTo(int& num, int pos, int val){

    if(((num >> pos)&1) != val){
        num ^= 1 << pos;
    }
}

int solve(int which, int n){
    queue<int> q;
    q.push(which);
    vis[which] = 0;
    while(!q.empty()){
        int top = q.front() ; q.pop();
        if(top == ((1<<n)-1)){
            break;
        }
        int now = top;
        for(int i = 0 ;i< n ; i++){
            now ^= (1 << i);
            int toCall = now;
            for(int j = 0 ;j <= i/2 ; j++){
                int other = i -j;
                setTo(toCall, j, (now>>other)&1);
                setTo(toCall, other, (now>>j)&1);
            }
            if(vis[toCall] == -1){
                vis[toCall] = vis[top] + 1;
                q.push(toCall);
            }
        }
    }
    return vis[(1 << n)-1];
}

int main(){
    int test;
    cin >> test;
    for(int t = 1 ;t <= test; t++){
        memset(vis, -1, sizeof vis);
        string str;
        cin >> str;
        int num = 0;
        for(int i = 0 ;i < (int)str.size(); i ++){
            if(str[i] == '+')
                num |= (1 << i); 
        }
        cout << "Case #" << t << ": " << solve(num, str.size()) << endl;
    }
    return 0;
}
