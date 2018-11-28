#include <iostream>

using namespace std;

int main()
{
    int tests;
    cin >> tests;
    int t = 1;
    while(tests--){
        long a,b,k;
        cin >> a >> b >> k;
        int cnt = 0;
        for(int i = 0; i < a; ++i){
            for(int j = 0; j < b; ++j){
                if( (i&j) < k) cnt++;
            }
        }
        cout << "Case #"<<t<<": "<< cnt << endl;
        t++;
    }
    return 0;
}
