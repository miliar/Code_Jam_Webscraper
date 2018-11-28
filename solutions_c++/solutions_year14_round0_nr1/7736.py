#include <iostream>
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
using namespace std;

#define FOR(i,a,b)  for(int i=(a),_##i=(b);i<_##i;++i)
#define F(i,a)      FOR(i,0,a)
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define MP          make_pair
#define S           size()
typedef long long   LL;


int main() {
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("small-input.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas=1; cas<=T ;cas++) {
        printf("Case #%d: ", cas);
        int salida;
        int matrix_1[4][4];
        int matrix_2[4][4];
        int a,b;
        int v[4],w[4];
        cin>>a;a--;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>matrix_1[i][j];
            }
         }
         cin>>b;b--;
         for(int i=0;i<4;i++)
         {
            for(int j=0;j<4;j++)
            {
                cin>>matrix_2[i][j];
            }
         }
         v[0]=matrix_1[a][0];v[1]=matrix_1[a][1];v[2]=matrix_1[a][2];v[3]=matrix_1[a][3];
         w[0]=matrix_2[b][0];w[1]=matrix_2[b][1];w[2]=matrix_2[b][2];w[3]=matrix_2[b][3];
         int sum=0;
         /*for(int i=0;i<4;i++)
         {
            cout<<v[i]<<"   "<<w[i]<<endl;
         }*/
         for(int i=0;i<4;i++)
         {
            for(int j=0;j<4;j++)
            {
                if(v[i]==w[j])
                {
                    sum++;
                    salida = v[i];
                }
            }
         }
        if(sum==1)cout<<salida<<endl;
        else if(sum>1)cout<<"Bad magician!"<<endl;
        else if(sum==0)cout<<"Volunteer cheated!"<<endl;

    }
}
