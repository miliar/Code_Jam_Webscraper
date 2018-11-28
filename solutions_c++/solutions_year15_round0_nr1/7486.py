#include <iostream>
using namespace std;
int main(){
    int c;
    cin>>c;
    for(int cc = 1; cc <= c; cc++){
        int s_max;
        cin>>s_max;
        char s_k[s_max+1];
        cin>>s_k;
        int ans = 0;
        int nowCnt = 0;
        for(int i=1; i<=s_max; i++){
            nowCnt += (s_k[i-1] - '0');
            if(nowCnt < i){
                ans += i - nowCnt;
                nowCnt = i;
            }
        }
        cout<<"Case #"<<cc<<": "<<ans<<endl;
    }
    return 0;
}
