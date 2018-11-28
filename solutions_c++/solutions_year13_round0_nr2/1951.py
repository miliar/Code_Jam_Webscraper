#include<cstdio>
#include<iostream.h>

int board[1001][1001];

int main(){
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int t,_ca = 0;
    while(cin >> t){
    for(;_ca < t; ++_ca){
        int n,m;
        cin >> n >> m;
        for(int i = 0; i < n; ++i)
            for(int j = 0; j < m; ++j)
                cin >> board[i][j];
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < m; ++j){
                int dir[][2] = {{0,1},{0,-1},{-1,0},{1,0}};

                bool bigTip = 0;

                for(int k = 0; k < 2; ++k){
                    int srci = i,srcj = j;
                    bool tip = 0;
                    while(srci + dir[k][0] > -1 &&
                            srci + dir[k][0] < n &&
                                srcj + dir[k][1] > -1 &&
                                    srcj + dir[k][1] < m){
                        srci += dir[k][0];
                        srcj += dir[k][1];
                        if(board[srci][srcj] > board[i][j]){
                            tip = 1;
                            //cout << i << "-" << j << endl;
                            //cout << srci << " " << srcj << endl;
                            break;
                        }
                    }
                    if(tip){
                        bigTip = 1;
                        break;
                    }
                }
                if(0 == bigTip){
                    // ´ËÂ·Í¨
                }else{
                    bigTip = 0;
                    for(int k = 2; k < 4; ++k){
                        int srci = i,srcj = j;
                        bool tip = 0;
                        while(srci + dir[k][0] > -1 &&
                                srci + dir[k][0] < n &&
                                    srcj + dir[k][1] > -1 &&
                                        srcj + dir[k][1] < m){
                            srci += dir[k][0];
                            srcj += dir[k][1];
                            if(board[srci][srcj] > board[i][j]){
                                tip = 1;
                                //cout << i << "-" << j << endl;
                                //cout << srci << " " << srcj << endl;
                                break;
                            }
                        }
                        if(tip){
                            bigTip = 1;
                            break;
                        }
                    }
                    if(0 == bigTip){
                    }else{
                        printf("Case #%d: NO\n",_ca + 1);
                        goto EXITS;
                    }
                }
                
            }
        }
        printf("Case #%d: YES\n",_ca + 1);
EXITS:
        ;
    }
    }
    return 0;
}
/*
3
3 3
2 1 2
1 1 1
2 1 2
5 5
2 2 2 2 2
2 1 1 1 2
2 1 2 1 2
2 1 1 1 2
2 2 2 2 2
1 3
1 2 1
*/
