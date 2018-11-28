#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;
int N;
int bitmap[10];
int cnt;
void fill_bitmap(int num){
    while(num){
        int cur = num % 10;
        if(bitmap[cur] == 0)
            cnt--;
        bitmap[cur] = 1;
        num = num / 10;
    }
    return;
}
void solve(int t){
    cin >> N;
    if(N == 0){
        cout << "Case #" << t << ": " << "INSOMNIA" << endl;
        return;
    }
    int ans;
    cnt = 10;
    for(int i = 0; i < 10; ++i)
        bitmap[i] = 0;
    int num = 0;
    do{
        num += N;
        fill_bitmap(num);
    }while(cnt > 0);
        
    ans = num;
    cout << "Case #" << t << ": " << ans << endl;
    return;
}

using namespace std;
int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;++t){
        solve(t);
    }

    return 0;
}
