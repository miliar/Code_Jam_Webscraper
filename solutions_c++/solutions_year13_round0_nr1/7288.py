#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string.h>

using namespace std;

int main(int argc, char *argv[])
{
    freopen("1.in", "rt", stdin);
    freopen("A.out","wt",stdout);
    int T,i,j,ocnt,xcnt,tcnt,c=0;
    bool x,o,nc;
    string rw[4];
    cin>>T;
    while(T--){
        c++;
        nc=false;x=false;o=false;
        ocnt=0;xcnt=0;tcnt=0;
        for(i=0;i<4;i++){
            cin>>rw[i];
        }
        if(!x&&!o){
            for(i=0;i<4;i++){
                if(rw[i][i]=='X')xcnt++;
                if(rw[i][i]=='O')ocnt++;
                if(rw[i][i]=='T')tcnt++;
                if((xcnt==3&&tcnt==1)||xcnt==4)x=true;
                if((ocnt==3&&tcnt==1)||ocnt==4)o=true;
            }
        }
        ocnt=0;xcnt=0;tcnt=0;
        if(!x&&!o){
            for(j=0;j<4;j++){
                if(rw[j][3-j]=='X')xcnt++;
                if(rw[j][3-j]=='O')ocnt++;
                if(rw[j][3-j]=='T')tcnt++;
                if((xcnt==3&&tcnt==1)||xcnt==4)x=true;
                if((ocnt==3&&tcnt==1)||ocnt==4)o=true;
            }
        }
        ocnt=0;xcnt=0;tcnt=0;
        if(!x&&!o){
            for(i=0;i<4;i++){
                if(x==true||o==true)break;
                ocnt=0;xcnt=0;tcnt=0;    
                for(j=0;j<4;j++){
                    if(rw[i][j]=='X')xcnt++;
                    if(rw[i][j]=='T')tcnt++;
                    if(rw[i][j]=='O')ocnt++;
                    if((xcnt==3&&tcnt==1)||xcnt==4){
                        x=true;
                        break;
                    }
                    if((ocnt==3&&tcnt==1)||ocnt==4){
                        o=true;
                        break;
                    }
                }
            }
        }
        ocnt=0;xcnt=0;tcnt=0;
        if(!x&&!o){
            for(i=0;i<4;i++){
                if(x==true||o==true)break;
                ocnt=0;xcnt=0;tcnt=0;    
                for(j=0;j<4;j++){
                    if(rw[j][i]=='X')xcnt++;
                    if(rw[j][i]=='T')tcnt++;
                    if(rw[j][i]=='O')ocnt++;
                    if((xcnt==3&&tcnt==1)||xcnt==4){
                        x=true;
                        break;
                    }
                    if((ocnt==3&&tcnt==1)||ocnt==4){
                        o=true;
                        break;
                    }
                }
            }
        }
        ocnt=0;xcnt=0;tcnt=0;
        if(!x&&!o){
            for(i=0;i<4;i++){
                if(nc)break;
                for(j=0;j<4;j++){
                    if(rw[i][j]=='.'){
                        nc=true;
                        break;
                    }
                }
            }
        }
        if(x)
            printf("Case #%d: X won\n",c);
        if(o)
            printf("Case #%d: O won\n",c);
        if(nc)
            printf("Case #%d: Game has not completed\n",c);
        if(!nc&&!o&&!x)
            printf("Case #%d: Draw\n",c);
    }
    //system("PAUSE");
    return 0;//EXIT_SUCCESS;
}
