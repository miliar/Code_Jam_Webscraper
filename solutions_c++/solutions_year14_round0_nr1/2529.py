#include<iostream>

using namespace std;

int main()
{
    int T, ans1, ans2, match, arr1[4][4], arr2[4][4], card;

    cin >> T;
    for(int turn=1; turn<=T; turn++){
        cin >> ans1;
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
                cin >> arr1[i][j];
        cin >> ans2;
        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
                cin >> arr2[i][j];
        match = 0;
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                if( arr1[ ans1-1 ][i] == arr2[ ans2-1 ][j] ){
                    match++;
                    card = arr1[ ans1-1 ][i];
                }
            }
        }
        if ( match==0 ){
            cout << "Case #" << turn << ": Volunteer cheated!\n";
        }
        else if (match == 1){
            cout << "Case #" << turn << ": " << card << '\n';
        }
        else    cout << "Case #" << turn << ": Bad magician!\n";
    }
}
