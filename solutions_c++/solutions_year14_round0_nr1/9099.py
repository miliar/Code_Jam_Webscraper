#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("A-small-attempt0.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int TC;
    cin >> TC;
    int cas= 1;
    while(TC--){
        int row1, row2, arr1[4], arr2[4];
        int grid[4][4];
        cin >> row1;
        row1--;
        for(int i= 0; i< 4; i++)
            for(int j= 0; j< 4; j++)
                cin >> grid[i][j];

        for(int i= 0; i< 4 ; i++)
            arr1[i]= grid[row1][i];


        cin >> row2;
        row2--;
        for(int i= 0; i< 4; i++)
            for(int j= 0; j< 4; j++)
                cin >> grid[i][j];

        for(int i= 0; i< 4 ; i++)
            arr2[i]= grid[row2][i];

        int ans= -1;
        for(int i= 0; i< 4; i++){
            for(int j= 0; j< 4; j++){
                if(arr1[i]==arr2[j]){
                    if(ans == -1)
                        ans= arr1[i];
                    else{
                        ans= (1<<20);
                        i= (1<<20);
                        j= (1<<20);
                    }
                }
            }
        }

        cout << "Case #" << cas << ": ";
        if(ans == -1) cout << "Volunteer cheated!";
        else if(ans == (1<<20)) cout << "Bad magician!";
        else cout << ans;

        cout << endl;
        cas++;
    }
}

