#include <iostream>
#include <vector>
#include <cstdio>
#include <set>
#include <map>
#include <fstream>
#include <algorithm>
#include <map>
#include <queue>


using namespace std;

int t;
int r, c;
string v[200];
bool tilt[200][200][5];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("Akinagyonjo.out", "w", stdout);
    cin >> t;

    for (int ttt=1;ttt<=t;ttt++) {
        cin >> r>>c;
        for (int i=0;i<r;i++) cin >> v[i];

        for (int i=0;i<r;i++) {
            for (int j=0;j<c;j++) {
                for (int k=0;k<5;k++) tilt[i][j][k]=false;
            }
        }
        int szam=0;
        bool lehet=true;
        for (int i=0;i<r;i++) {
            for (int j=0;j<c;j++) if (v[i][j]!='.') {

                bool a=true;
                for (int k=0;k<i;k++) {
                    if (v[k][j]!='.') a=false;
                }
                if (a) {
                    tilt[i][j][1]=true;
                }

                a=true;
                for (int k=i+1;k<r;k++) {
                    if (v[k][j]!='.') a=false;
                }
                if (a) {
                    tilt[i][j][3]=true;
                }


                a=true;
                for (int k=0;k<j;k++) {
                    if (v[i][k]!='.') a=false;
                }
                if (a) {
                    tilt[i][j][4]=true;
                }

                a=true;
                for (int k=j+1;k<c;k++) {
                    if (v[i][k]!='.') a=false;
                }
                if (a) {
                    tilt[i][j][2]=true;
                }


                if (tilt[i][j][1] &&tilt[i][j][2] &&tilt[i][j][3] && tilt[i][j][4]) {
                    lehet=false;
                    break;
                }
                if (v[i][j]=='^' && tilt[i][j][1]) szam++;
                if (v[i][j]=='>' && tilt[i][j][2]) szam++;
                if (v[i][j]=='v' && tilt[i][j][3]) szam++;
                if (v[i][j]=='<' && tilt[i][j][4]) szam++;
            }
        }
        cout << "Case #" << ttt<<": ";
        if (lehet) {
            cout << szam<<endl;
        }
        else {
            cout << "IMPOSSIBLE"<<endl;
        }
    }


    return 0;
}
