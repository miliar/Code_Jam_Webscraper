#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;


int s[5][5];
char ch[150000];
int icase, n, t;
const int MA = 1000000;

int main() {
    ios_base::sync_with_stdio(false);
    s[1][1]=1; s[1][2]=2;   s[1][3]=3;  s[1][4]=4;
    s[2][1]=2; s[2][2]=-1;  s[2][3]=4;  s[2][4]=-3;
    s[3][1]=3; s[3][2]=-4;  s[3][3]=-1; s[3][4]=2;
    s[4][1]=4; s[4][2]=3;   s[4][3]=-2; s[4][4]=-1;
    cin>>icase;
    for (int c = 1; c <= icase; c++) {
        cin>>n>>t>>ch;
        int flag = 1, tmp = 1;
        int pi = MA, pj = MA;
        for (int j = 0; j < t; j++)
            for (int i=0; i<n; i++) {
                int u = 1;
                if (ch[i] == 'i') u = 2;
                if (ch[i] == 'j') u = 3;
                if (ch[i] == 'k') u = 4;
                if (s[tmp][u] < 0)
                    flag = -flag;
                tmp = abs(s[tmp][u]);

                if (tmp == 2 && flag == 1 && j * n + i < pi)
                    pi = j * n + i;
                if (pi != MA && flag == 1 && tmp == 4 && j * n + i < pj)
                    pj = j * n + i;
            }
        if (flag == -1 && tmp == 1 && pi != MA && pj != MA) 
            printf("Case #%d: YES\n", c);
        else
            printf("Case #%d: NO\n", c);
    }
    return 0;
}
