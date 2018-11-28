#include <iostream>
#include <vector>
#include <map>
#include <utility>
using namespace std;
map<char,int> M{{'^',0},{'>',1},{'v',2},{'<',3},{'.',-1}};
map<int,pair<int,int> > Moves{{0,{-1,0} },{1,{0,1} },{2,{1,0} },{3,{0,-1} }};

bool ruszaj(int x,int y,int k,vector<vector<int> > &Map){
    while(Map[x+Moves[k].first][y+Moves[k].second]!=-2){
        x+=Moves[k].first;
        y+=Moves[k].second;
        if(Map[x][y]>-1)
            return true;
    }
    return false;
}
main(){
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    int licznik=1;
    while(T--){
        int R,C;
        cin >> R >> C;
        vector<vector<int> > Map(R+2,vector<int>(C+2,-2));
        for(int i=1;i<=R;i++){
            for(int j=1;j<=C;j++){
                char c;
                cin >> c;
                Map[i][j]=M[c];
            }
        }
        bool flaga=true;
        int res=0;
        for(int i=1;i<=R && flaga;i++){
            for(int j=1;j<=C && flaga;j++){
                if(Map[i][j]==-1)
                    continue;
                if(ruszaj(i,j,Map[i][j],Map))//widzi
                    continue;
                else{//nie widzi
                    bool see=false;
                    for(int k=0;k<4 && !see;k++){
                        if(ruszaj(i,j,k,Map))
                            see=true;
                    }
                    if(!see)
                        flaga=false;
                    else
                        res++;
                }
            }
        }
        if(flaga){
            cout << "Case #"<<licznik++<< ": "<< res << endl;
        }
        else
            cout << "Case #"<<licznik++<< ": IMPOSSIBLE" << endl;
    }
    return 0;
}
