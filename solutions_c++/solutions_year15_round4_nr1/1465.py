#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include <sstream>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <cstdlib>
#include <cstdio>
#include <iterator>
#include <functional>
#include <bitset>
typedef long long ll;
using namespace std;
char G[111][111];
int R,C;
int ccc(int i, int j){
    int a,b;
    int dir[]={0,0,0,0};//down,up,right,left
    for(int a=i+1;a<R;a++){
        if(G[a][j]!='.'){
            dir[0]=1;
            break;
        }
    }
    for(int a=i-1;a>=0;a--){
        if(G[a][j]!='.'){
            dir[1]=1;
            break;
        }
    }
    for(int a=j+1;a<C;a++){
        if(G[i][a]!='.'){
            dir[2]=1;
            break;
        }
    }
    for(int a=j-1;a>=0;a--){
        if(G[i][a]!='.'){
            dir[3]=1;
            break;
        }
    }
    if(G[i][j]=='v' && dir[0]==1){
        return 0;
    } else if(G[i][j]=='^' && dir[1]==1){
        return 0;
    } else if(G[i][j]=='>' && dir[2]==1){
        return 0;
    } else if(G[i][j]=='<' && dir[3]==1){
        return 0;
    }
    for(int i=0;i<4;i++){
        if(dir[i]==1)return 1;
    }
    return -1;
}
int countt(){
    int tot=0;
    for(int i=0;i<R;i++){
        for(int j=0;j<C;j++){
            if(G[i][j]!='.'){
                int num=ccc(i,j);
                if(num==-1)return -1;
                tot+=num;
            }

        }
    }
    return tot;
}
int main()
{
    freopen("txt.in","r",stdin);
    //freopen("out","w",stdout);
    int T;
    cin >> T;
    for(int t=0;t<T;t++){
        cin >> R >> C;
        for(int i=0;i<R;i++){
            for(int j=0;j<C;j++){
                cin >> G[i][j];
            }
        }
        int res=countt();
        cout << "Case #" << (t+1) << ": ";
        if(res==-1){
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << res << endl;
        }
    }
    return 0;
}
