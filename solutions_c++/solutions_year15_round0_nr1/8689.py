#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main()
{
    freopen("A-large.in", "r", stdin);
	freopen("A-LARGE.out", "w", stdout);
    int T,Sm,Sum=0,num,cnt=0; cin >> T ;
    string S ;
    for (int j=1 ; T--; ++j,Sum=0,cnt=0){
        cin >> Sm >> S ;
        for (int i=0; i<=Sm; ++i) {
            num=S[i]-'0';
            if (Sum<i && num) cnt+=i-Sum,Sum+=i-Sum;
            Sum+=num;
        }
        cout << "Case #" << j << ": " << cnt << endl ;
    }
    return 0;
}
