#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;



int main(void) {
    /* number of test cases */
    unsigned short int testcases;

    cin >> testcases;


    int H,W;
    for(int testcase=1; testcase <= testcases; testcase++) { //loops for each case
        cin >> H>>W;

        char g[W][H];
        char s[1000];

        for (int y=0;y<H;y++){
            cin >> s;
            for (int x=0;x<W; x++)
                g[x][y] = s[x];
        }

        int res = 0;
        bool imp = false;

        for (int x=0; (x<W) && (imp==false);x++){
            for (int y=0;(y<H) && (imp==false);y++){
                int dx=0,dy=0;
                char c = g[x][y];
                if (c=='.')
                    continue;

                if (c=='^')
                    dy = -1;                
                if (c=='v')
                    dy = 1;
                if (c=='<')
                    dx = -1;
                if (c=='>')
                    dx = 1;

                int nx=x+dx,ny=y+dy;
                bool ok = false;
                while (nx>=0 && nx < W && ny>=0 && ny<H){
                    if(g[nx][ny] != '.'){
                        ok=true;
                        break;
                    }
                    nx += dx;
                    ny+=dy;
                }

                if (ok)
                    continue;

                else{
                    res ++;

                    nx=0;
                    ny=y;
                    ok=false;

                    for (nx=0;nx<W;nx++){
                        if(nx!=x && g[nx][ny]!='.'){
                            ok=true;
                            break;
                        }
                    }

                    if(ok)
                        continue;

                    nx=x;
                    ny=0;
                    ok=false;

                    for (ny=0;ny<H;ny++){
                        if(ny!=y && g[nx][ny]!='.'){
                            ok=true;
                            break;
                        }
                    }

                    if(ok)
                        continue;

                    imp=true;
                }
            }
        }

        if(imp)
            cout << "Case #" << testcase << ": " << "IMPOSSIBLE" << endl;
        else
            cout << "Case #" << testcase << ": " << res << endl;


    }

    return 0;
}