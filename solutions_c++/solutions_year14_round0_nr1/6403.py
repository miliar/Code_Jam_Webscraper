#include <stdio.h>

#include <fstream>
using namespace std;

int main()
{
   ofstream tt;
    tt.open("vats.txt");
    int t, k;
    scanf("%d",&t);
    for(k = 1; k <= t; k++) {
        int x, z, i, j;
        int y;
        int a1[4][4];
        int a2[4][4];
        scanf("%d",&x);
        for(i = 0; i < 4; i++) {
            for(j = 0; j < 4; j++) scanf("%d",&a1[i][j]);
        }
        scanf("%d",&y);
        for(i = 0; i < 4; i++) {
            for(j = 0; j < 4; j++) scanf("%d",&a2[i][j]);
        }
        int m = 0;
        for(i = 0; i < 4; i++) {
            for(j = 0; j < 4; j++) {
                if(a1[x - 1][i] == a2[y - 1][j]) {
                    m++;
                    z = a1[x - 1][i];
                }
            }
        }
        if(m == 1)
         tt<<"Case #"<<k<<": "<<z<<endl;
        else if(m == 0) tt<<"Case #"<<k<<": Volunteer cheated!"<<endl;
        else tt<<"Case #"<<k<<": Bad magician!"<<endl;
    }
    tt.close();
}
