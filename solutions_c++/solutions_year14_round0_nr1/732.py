#include <cstdlib>
#include <iostream>
#include "set"

using namespace std;

int main(int argc, char *argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T;
    cin >> T;
    
    int Row1[4];
    int Row2[4];
    int Row_I;    

    int found;
	int y;
	int LastFound;
	int CountFound;
	int dump1;
	int dump2;
	int dump3;
	int dump4;
    for (int T_i=0; T_i<T;T_i++){
        cin >> Row_I;
        for (int T_ii=1;T_ii <= 4; T_ii++){
            if (T_ii == Row_I) for (int T_iii=0;T_iii < 4; T_iii++) cin >> Row1[T_iii]; else cin >> dump1 >> dump2 >> dump3 >> dump4;
        }
        cin >> Row_I;
        for (int T_ii=1;T_ii <= 4; T_ii++){
            if (T_ii == Row_I) for (int T_iii=0;T_iii < 4; T_iii++) cin >> Row2[T_iii]; else cin >> dump1 >> dump2 >> dump3 >> dump4;
        }
        LastFound=0;
        CountFound=0;
 
        for (int a = 0; a < 4; a++){
            found = 0;
            for (int b=0; b<4; b++){
                if (Row1[a]== Row2[b]) found = 1;
            }
            if (found==1) {
               CountFound ++;
               LastFound = Row1[a];
                          } 
        }
        if (CountFound==1) {
        cout << "Case #" << T_i+1 << ": " << LastFound << endl;
                           }
        if (CountFound>1) {
        cout << "Case #" << T_i+1 << ": Bad magician!" << endl;
                           }
        if (CountFound==0) {
        cout << "Case #" << T_i+1 << ": Volunteer cheated!" << endl;
                           }
        
    }
    return EXIT_SUCCESS;
}
