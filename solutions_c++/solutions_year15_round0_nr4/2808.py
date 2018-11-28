#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <utility>
#include <set>
#include <math.h>
#include <bitset>
const int MaxN = int (1e5);
using namespace std;

int main()
{
    freopen( "in.txt" , "r" , stdin);
    freopen( "out.txt" , "w" , stdout);

    int T , R , X , C;
    cin >> T ;

    for (int i=1; i<=T; i++){
        cin  >> X >> R >> C;
        if (X==1){
            cout << "Case #" << i<< ": " << "GABRIEL"<< endl;
        }
        else if (X==2){
            if((R*C)%2 != 0){
                cout << "Case #" << i<< ": " << "RICHARD"<< endl;
            }
            else
                cout << "Case #" << i<< ": " << "GABRIEL"<< endl;
        }
        else if (X==3){
            if ((R*C) <6){
                cout << "Case #" << i<< ": " << "RICHARD"<< endl;
            }
            else {
                if ((R*C)%3 != 0){
                    cout << "Case #" << i<< ": " << "RICHARD"<< endl;
                }
                else {
                    cout << "Case #" << i<< ": " << "GABRIEL"<< endl;
                }
            }
        }
        else if (X==4){
            if ((R*C)<12){
                cout << "Case #" << i<< ": " << "RICHARD"<< endl;
            }
            else {
                cout << "Case #" << i<< ": " << "GABRIEL"<< endl;
            }
        }
        /*else if (X==5){

        }
        else if (X==6){

        }
        else if (X>=7){
            cout << "Case #" << i<< ": " << "RICHARD"<< endl;
        }*/
    }

    return 0;
}
