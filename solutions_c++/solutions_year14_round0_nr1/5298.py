#include <iostream>
#include <stdio.h>

using namespace std;

int main(){
    int total_cases, row1, row2;
    int possible[17];
    int cur;
    cin >> total_cases;

    for(int cur_case = 1; cur_case <= total_cases ; cur_case++ )
    {
        int result = -2; 
        cin >> row1;
        memset(possible, 0, sizeof(possible));
        for(int r = 1; r <= 4; r++)
            for(int c = 1; c <= 4; c++)
        {
            cin >> cur;
            if(r == row1)
                possible[cur] = 1;
        }
        cin >> row2;
        for(int r = 1; r <= 4; r++)
            for(int c = 1; c <= 4; c++)
        {
            cin >> cur;
            if(r == row2 && possible[cur])
            {
                if(result > 0)
                    result = -1;
                else if(result == -2)
                    result = cur;
            }
        }         
        final:
        cout << "Case #" << cur_case << ": ";
        if(result == -2)
            cout << "Volunteer cheated!\n" ;
        else if(result == -1)
            cout << "Bad magician!\n" ;
        else
            cout << result << "\n";
    }
    return 0;
}
