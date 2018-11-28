#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>

using namespace std;
#define FOR(i,a,b) for(int i=int(a);i<int(b);i++)
#define MAX 4
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin>>T;
    FOR(k,1,T+1){
        char mat[MAX+5][MAX+5];
        bool not_complete=false;;
        FOR(i,0,4){
            FOR(j,0,4){
                cin>>mat[i][j];
                if(mat[i][j]=='.')
                    not_complete=true;
            }
        }
        bool x,y;
        //revision fila//
        FOR(i,0,4){
            //X//
            x=true;
            FOR(j,0,4){
                if(mat[i][j]=='O'||mat[i][j]=='.'){
                    x=false;
                    break;
                }
            }
            if(x) break;

            //Y//
            y=true;
            FOR(j,0,4){
                if(mat[i][j]=='X'||mat[i][j]=='.'){
                    y=false;
                    break;
                }
            }
            if(y)break;
        }
        if(x||y){
            if(x)cout<<"Case #"<<k<<": X won"<<endl;
            else cout<<"Case #"<<k<<": O won"<<endl;
        }
        else{
            //revision columna//
            FOR(i,0,4){
                //X//
                x=true;
                FOR(j,0,4){
                    if(mat[j][i]=='O'||mat[j][i]=='.'){
                        x=false;
                        break;
                    }
                }
                if(x) break;

                //Y//
                y=true;
                FOR(j,0,4){
                    if(mat[j][i]=='X'||mat[j][i]=='.'){
                        y=false;
                        break;
                    }
                }
                if(y)break;
            }
            if(x||y){
                if(x)cout<<"Case #"<<k<<": X won"<<endl;
                else cout<<"Case #"<<k<<": O won"<<endl;
            }
            else{

                //revision diagonal//
                if((mat[0][0]=='X'||mat[0][0]=='T')&&(mat[1][1]=='X'||mat[1][1]=='T')&&(mat[2][2]=='X'||mat[2][2]=='T')&&(mat[3][3]=='X'||mat[3][3]=='T'))
                    cout<<"Case #"<<k<<": X won"<<endl;
                else if((mat[0][0]=='O'||mat[0][0]=='T')&&(mat[1][1]=='O'||mat[1][1]=='T')&&(mat[2][2]=='O'||mat[2][2]=='T')&&(mat[3][3]=='O'||mat[3][3]=='T'))
                    cout<<"Case #"<<k<<": O won"<<endl;
                else if((mat[3][0]=='X'||mat[3][0]=='T')&&(mat[2][1]=='X'||mat[2][1]=='T')&&(mat[1][2]=='X'||mat[1][2]=='T')&&(mat[0][3]=='X'||mat[0][3]=='T'))
                    cout<<"Case #"<<k<<": X won"<<endl;
                else if((mat[3][0]=='O'||mat[3][0]=='T')&&(mat[2][1]=='O'||mat[2][1]=='T')&&(mat[1][2]=='O'||mat[1][2]=='T')&&(mat[0][3]=='O'||mat[0][3]=='T'))
                    cout<<"Case #"<<k<<": O won"<<endl;
                else if(not_complete)cout<<"Case #"<<k<<": Game has not completed"<<endl;
                else cout<<"Case #"<<k<<": Draw"<<endl;
            }
        }
    }
    return 0;
}
