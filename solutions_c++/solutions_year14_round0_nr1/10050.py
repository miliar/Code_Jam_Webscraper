#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<set>
using namespace std;
int m[4][4];

int main(){
    int t,a,b,st;
    cin>>t;
    for (int tt = 0; tt < t; ++tt){
        cin>>a;
        set<int> s; s.clear();
        for (int i=0; i<4; ++i){
            for (int j=0; j<4; ++j){
                cin>>m[i][j];
                if (i == a-1) s.insert(m[i][j]);
            }
        }
        st=-1;
        cin>>a;
        for (int i=0; i<4; ++i){
            for (int j=0; j<4; ++j){
                cin>>m[i][j];
                if (i == a-1 && s.count(m[i][j])){
                    if (st == -1) st=m[i][j];
                    else
                    if (st > 0 ) st=-2;
                }
            }
        }
        char buff[5];
        sprintf(buff, "%d", st);
        cout<<"Case #"<<tt+1<<": "<<(st == -1 ? "Volunteer cheated!" : st == -2 ? "Bad magician!" : buff)<<endl;
    }
    return 0;
}

