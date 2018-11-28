#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream h;
    h.open("input.in");
    int t,count,t1 = 4,t2 = 4;
    bool iscompleted;
    char w;
    h >> t;
    char l[4][4];
    freopen("output.out","w",stdout);
    for(int y = 0;y<t;y++){
        iscompleted = 1;
        for(int j = 0;j<4;j++){
            for(int i = 0;i<4;i++){
                h >> l[j][i];
                if(l[j][i] == 'T'){
                    t1 = j;
                    t2 = i;
                }
                if(l[j][i] == '.') iscompleted = 0;

            }
        }
        count = 0;
        for(int j = 0;j<4;j++){
            if(((l[j][0] == 'X') || (l[j][1] == 'X')) && t1 < 4) l[t1][t2] = 'X';
            if(((l[j][0] == 'O') || (l[j][1] == 'O')) && t1 < 4) l[t1][t2] = 'O';
            if((l[j][0] == l[j][1]) && (l[j][0] == l[j][2]) && (l[j][0] == l[j][3]) && (l[j][0] != '.')){
                w = l[j][0];
                count++;
                j = 4;
            }
            if (j != 4){
                if(((l[0][j] == 'X') || (l[1][j] == 'X')) && t1 < 4) l[t1][t2] = 'X';
                if(((l[0][j] == 'O') || (l[1][j] == 'O')) && t1 < 4) l[t1][t2] = 'O';
                if((l[0][j] == l[1][j]) && (l[0][j] == l[2][j]) && (l[0][j] == l[3][j])&& (l[j][0] != '.')){
                    w = l[0][j];
                    count++;
                    j = 4;
                }
            }
        }
        if(count == 0){
            if(((l[0][0] == 'X') || (l[1][1] == 'X')) && t1 < 4) l[t1][t2] = 'X';
            if(((l[0][0] == 'O') || (l[1][1] == 'O')) && t1 < 4) l[t1][t2] = 'O';
            if((l[0][0] == l[1][1]) && (l[0][0] == l[2][2]) && (l[0][0] == l[3][3])&& (l[0][0] != '.')){
                w = l[0][0];
                count++;
            }
            if(((l[0][3] == 'X') || (l[1][2] == 'X')) && t1 < 4) l[t1][t2] = 'X';
            if(((l[0][3] == 'O') || (l[1][2] == 'O')) && t1 < 4) l[t1][t2] = 'O';

            if((l[0][3] == l[1][2]) && (l[0][3] == l[2][1]) && (l[0][3] == l[3][0])&& (l[0][3] != '.')){
                w = l[0][3];
                count++;
            }
        }
        cout << "Case #" << y + 1 << ": ";
        if(count == 0){
            if(!iscompleted) cout << "Game has not completed";
            else cout << "Draw";
        }
        else cout << w << " won";
        cout << endl;
    }
    return 0;
}
