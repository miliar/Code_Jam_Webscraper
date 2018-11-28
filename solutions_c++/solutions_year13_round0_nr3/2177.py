#include<cstdio>
#include<cstring>
#include<iostream>
#include<cmath>

using namespace std;

bool isPal(long long n){
    char num[20];
    sprintf(num, "%d", n);
    int len = strlen(num);
    for(int i = 0, j = len-1; i < j; i++, j--){
        if(num[i] != num[j]) return false;
    }
    return true;
}

int main(){
    freopen("pcout.txt", "w", stdout);
    int T;
    long long A, B, ans;
    int cnt = 0;
    scanf("%d", &T);
    while(T--){
        cin >> A >> B;
        ans = 0;
        long long s =(long long)ceil(sqrt((double)A));
        for(long long i = s; i*i <= B; i++){
            if(isPal(i) && isPal(i*i)){
                ans++;
            }
        }
        cout << "Case #" << ++cnt << ": " << ans << endl;
    }
    return 0;
}
