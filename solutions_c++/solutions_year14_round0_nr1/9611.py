#include <iostream>
#include <cstdio>
#include <algorithm>
#include <math.h>
using namespace std;
int mass1[4][4], mass2[4][4];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n;
    cin >> n;
    for(int i = 1; i <= n;i ++){
        int s1;
        cin >> s1;
        s1 --;
        for(int j = 0; j < 4; j ++){
            cin >> mass1[j][0] >> mass1[j][1] >> mass1[j][2] >> mass1[j][3];
        }
        int s2;
        cin >> s2;
        s2 --;
        for(int j = 0; j < 4; j ++){
            cin >> mass2[j][0] >> mass2[j][1] >> mass2[j][2] >> mass2[j][3];
        }
        int res = 0;
        int pos = 0;
        for(int j = 0; j < 4; j ++){
            for(int k = 0;k < 4; k ++){
                if(mass1[s1][j] == mass2[s2][k]){
                    res ++;
                    pos = j;
                }
            }
        }
        if(res == 0){
            cout << "Case #"<<i << ": Volunteer cheated!"<<endl;
            continue;
        }
        if(res == 1){
            cout << "Case #"<<i << ": "<<mass1[s1][pos]<<endl;
            continue;
        }
        cout <<"Case #"<<i << ": Bad magician!"<<endl;

    }
    return 0;
}
