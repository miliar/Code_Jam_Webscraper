#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <stack>
#include <queue>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("Aout","w",stdout);
    int col[4] , row[4] , tri , utr;
    char a[4][4];
    int cnt;
    cin >> cnt;
    int M = 1;
    while(cnt --){
        int mi = -1,mj = -1;
        bool e = true;
        tri = utr = 0;
        memset(col , 0 , sizeof(col));
        memset(row , 0 , sizeof(row));
        for(int i = 0 ; i < 4 ; i++)
            for(int j =0 ; j < 4 ; j++){
                cin >> a[i][j];
                if(a[i][j] == 'T')
                    mi = i , mj = j;
                if(a[i][j] == '.')
                    e = false;
            }
        int ans = 0;
        for(int i = 0 ; i < 4 ; i++){
            if(a[mi][i] == 'X')
                ans++;
            else if(a[mi][i] == 'O')
                ans--;
        }
        if(ans == 3){
            cout <<"Case #" << M++ << ": X won" <<endl;
            continue;
        }
        else if(ans == -3){
            cout <<"Case #" << M++ << ": O won" <<endl;
            continue;
        }
        ans = 0;
        for(int i = 0 ; i < 4 ; i++){
            if(a[i][mj] == 'X')
                ans++;
            else if(a[i][mj] == 'O')
                ans--;
        }
        if(ans == 3){
            cout <<"Case #" << M++ << ": X won" <<endl;
            continue;
        }
        else if(ans == -3){
            cout <<"Case #" << M++ << ": O won" <<endl;
            continue;
        }
        if(mi+mj == 3){
            int i = 0 , j = 3;
            ans = 0;
            for(;j>=0 ; j-- , i++){
                if(a[i][j] == 'X') ans ++;
                else if(a[i][j] == 'O') ans --;
            }
            if(ans == 3){
                cout <<"Case #" << M++ << ": X won" <<endl;
                continue;
            }
            else if(ans == -3){
                cout <<"Case #" << M++ << ": O won" <<endl;
                continue;
            }
        }
        if(mi == mj){
            int i = 0 , j = 0;
            ans = 0;
            for(;j<4 ; j++ , i++){
                if(a[i][j] == 'X') ans ++;
                else if(a[i][j] == 'O') ans --;
            }
            if(ans == 3){
                cout <<"Case #" << M++ << ": X won" <<endl;
                continue;
            }
            else if(ans == -3){
                cout <<"Case #" << M++ << ": O won" <<endl;
                continue;
            }
        }
        for(int i = 0 ; i < 4 ; i++){
            ans = 0;
            for(int j = 0 ; j < 4 ; j++){
                if(a[i][j] == 'X') ans++;
                else if(a[i][j] == 'O') ans --;
            }
            col[i] = ans;
        }
        for(int i = 0 ; i < 4 ; i++){
            ans = 0;
            for(int j = 0 ; j < 4 ; j++){
                if(a[j][i] == 'X') ans++;
                else if(a[j][i] == 'O') ans --;
            }
            row[i] = ans;
        }
        for(int i = 0 ; i < 4 ; i++)
        {
            if(a[i][i] == 'X') tri ++;
            else if(a[i][i] == 'O') tri--;
        }
        for(int i = 0 ; i < 4 ; i++)
        {
            if(a[i][3-i] == 'X') utr ++;
            else if(a[i][3-i] == 'O') utr--;
        }
        bool t= false;
        if(!t){
            for(int i = 0 ; !t&&i < 4 ; i++){
                if(col[i] == 4){
                    t = true;
                    cout <<"Case #" << M++ << ": X won" <<endl;
                    break;
                }
                else if(col[i] == -4){
                    t = true;
                    cout <<"Case #" << M++ << ": O won" <<endl;
                    break;
                }
            }
        }
        if(!t){
            for(int i = 0 ; !t&&i < 4 ; i++){
                if(row[i] == 4){
                    t = true;
                    cout <<"Case #" << M++ << ": X won" <<endl;
                    break;
                }
                else if(row[i] == -4){
                    t = true;
                    cout <<"Case #" << M++ << ": O won" <<endl;
                    break;
                }
            }
        }
        if(!t && tri == 4){
            t = true;
            cout <<"Case #" << M++ << ": X won" <<endl;
        }
        else if(!t && tri == -4){
            t = true;
            cout <<"Case #" << M++ << ": O won" <<endl;
        }
        if(!t && utr == 4){
            t = true;
            cout <<"Case #" << M++ << ": X won" <<endl;
        }
        else if(!t && utr == -4){
            t = true;
            cout <<"Case #" << M++ << ": O won" <<endl;
        }
        if(!t&&e)
            cout <<"Case #" << M++ << ": Draw" <<endl;
        if(!t && !e)
            cout <<"Case #" << M++ << ": Game has not completed" <<endl;
    }

	return 0;
}
