#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <functional>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;

int main() {
    int t,a,b,c,aux;
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A-small-attempt2.out","w",stdout);
    cin >> t;
    for(int i = 0 ; i < t ; i ++)
    {
        int m[4][4],q[4][4];

        c = 0;
        cin >> a;
        for(int j =0 ; j < 4 ; j++)
            for(int k = 0 ; k < 4 ; k++)
                cin >> m[j][k];

        cin >> b;
        for(int j =0 ; j < 4 ; j++)
            for(int k = 0 ; k < 4 ; k++)
                cin >> q[j][k];


        for(int j =0 ; j < 4 ; j++)
            for(int k = 0; k < 4 ; k++)
            {
                if(m[a-1][j] == q [b-1][k])
                {
                    c ++;
                    aux =m[a-1][j];
                }
            }
        if(c == 1 ){
            printf("Case #%d: %d\n",i+1, aux);
        }
        else{

            if( c == 0){
                printf("Case #%d: Volunteer cheated!\n",i+1 );
            }
            else{
                if(c > 1)
                 printf("Case #%d: Bad magician!\n", i+1 );
            }
        }
    }
}
