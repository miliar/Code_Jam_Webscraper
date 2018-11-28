#include <iostream>
using namespace std;
int main()
{
    int T,t,r;
    int x,y,sum,cnt;
    cin >> T;
    int k = 0;
    while(T--){
        k++;
        cin >> r >> t;
        sum = 0;
        cnt = 0;
        x = r;
        while(sum <= t){
            y = x+1;
            sum += (y*y)-(x*x);
            if(sum <= t){
                cnt++;
                x = y+1;
            }
            else{
                break;
            }
        }
        cout << "Case #" << k << ": "<< cnt << endl;
    }
}
