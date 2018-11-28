#include<iostream>
#include<string>
#include<vector>
#include<cstdio>
using namespace std;
int main(){
    freopen("A-large.in","r",stdin);
    freopen("write.out","w",stdout);
    int t;
    cin >> t;
    for(int d=1; d<=t; d++){
        vector<string>v;
        string s;
        for(int i=0; i<4; i++){
            cin >> s;
            v.push_back(s);
        }
        int f=0,cnt,df=0;  char ch='X';
        for(int i=0; i<2; i++){
            for(int i=0; i<4; i++){
                    cnt=0;
                for(int j=0; j<4; j++){
                    if(v[i][j]==ch||v[i][j]=='T')cnt++;
                    else if(v[i][j]=='.')df=1;
                }
                if(cnt==4){f=1; break;}
            }
            if(cnt==4){f=1; break;}
            ch='O';
        }
        if(cnt!=4){
            ch='X';
        for(int i=0; i<2; i++){
            for(int i=0; i<4; i++){
                    cnt=0;
                for(int j=0; j<4; j++){
                    if(v[j][i]==ch||v[j][i]=='T')cnt++;
                    else if(v[j][i]=='.')df=1;
                }
                if(cnt==4){f=1; break;}
            }
            if(cnt==4){f=1; break;}
            ch='O';
        }
        }
        if(cnt!=4){
            ch='X';
            for(int i=0; i<2; i++){
                    cnt=0;
                for(int j=0; j<4; j++){
                    if(v[j][j]==ch||v[j][j]=='T')cnt++;
                    else if(v[j][j]=='.')df=1;
                }
            if(cnt==4){f=1; break;}
            ch='O';
            }
        }
        if(cnt!=4){
            ch='X';
            for(int i=0; i<2; i++){
                    cnt=0; int z=3;
                for(int j=0; j<4; j++){
                    if(v[j][z]==ch || v[j][z]=='T')cnt++;
                    else if(v[j][z]=='.')df=1;
                    z--;
                }
                if(cnt==4){f=1; break;}
                ch='O';
            }
        }
        if(f==1&&cnt==4)cout << "Case #" << d << ": " << ch << " won\n";
        else if(cnt!=4&&df==1)cout << "Case #" << d << ": " << "Game has not completed\n";
        else cout << "Case #" << d << ": " << "Draw\n";
    }

return 0;
}
/*
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O
*/
