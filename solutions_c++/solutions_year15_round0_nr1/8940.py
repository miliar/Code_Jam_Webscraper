#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;
int T,Smax,totalClappers,needClappers; string Si;

int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    freopen("stuff.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;
    for (int i=0; i<T; i++){
        cin >> Smax >> Si;
        totalClappers = 0;
        needClappers = 0;
        for(int j=0; j<=Smax; j++){
            if(totalClappers<j){
                needClappers += (j-totalClappers);
                totalClappers += (j-totalClappers);
            }
            totalClappers += (Si[j]-'0');
        }
        cout << "Case #" << i+1 << ": " << needClappers << "\n";
    }
    return 0;
}
