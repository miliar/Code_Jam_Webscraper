#include <bits/stdc++.h>
using namespace std;
string  arr;
string dig[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
int curr[26];
int ans[10];
bool solve(int i){
    if(i == 10){
        for(int i=0;i<26;i++)if(curr[i] > 0)return false;
        return true;
    }
    if(solve(i+1))return true;
    int k = 0;
    while(true){
        bool flag = false;
        k++;
        ans[i]++;
        for(int x=0;x<dig[i].size();x++){
            curr[dig[i][x]-'A']--;
            if(curr[dig[i][x]-'A'] < 0)flag = true;
        }
        if(flag)break;
        if(solve(i+1))return true;
    }
    while(k--){
        ans[i] --;
        for(int x=0;x<dig[i].size();x++){
            curr[dig[i][x]-'A']++;
        }
    }
    return false;
}
int main(){
    freopen("test.in","r",stdin);
        freopen("test.out","w",stdout);
    int T;
    cin >> T;
    int t = 1;
    while(T--){
        cout << "Case #"<<t++<<": ";
        cin >> arr;
        memset(curr,0,sizeof curr);
        memset(ans,0,sizeof ans);
        for(int i=0;i<arr.size();i++)curr[arr[i]-'A']++;
        solve(0);
        for(int i=0;i<10;i++)while(ans[i]--)cout << i;
        cout << endl;
    }
    return 0;
}
//2 9 , 3 ,  9-2 = 7
