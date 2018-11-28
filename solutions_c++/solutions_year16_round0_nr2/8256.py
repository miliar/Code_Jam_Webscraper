#include <iostream>
using namespace std;

int main(){

    freopen("B-large.in", "r", stdin);
    freopen("Blargeoutput.txt", "w", stdout);

    int total;
    cin >> total;
    for(int i=0;i<total;i++){
        int length=0, l=0, ans=0;
        char pancake[110], now;
        cin >> pancake;
        while(pancake[l]=='+' || pancake[l]=='-'){
            length++;
            l++;
        }
        now = pancake[length-1];
        if(pancake[length-1]=='-')
            ans++;

        for(l=length-2;l>=0;l--){
            if(pancake[l]!=now){
                ans++;
                now = pancake[l];
            }
        }
        cout << "Case #" << i+1 << ": " << ans << endl;
    }
    return 0;
}
