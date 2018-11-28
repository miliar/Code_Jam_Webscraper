
#include<string.h>

#include<stdio.h>

#include<stdlib.h>

#include<ctype.h>

#include <map>
#include <string>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include<cstdlib>
#include <cstdio>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <vector>
#include <utility>
#include <fstream>
#define INF     9999999
using namespace std;
int main()
{
    ifstream cin("A-small-attempt0.in");
    ofstream cout("out.out");
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++){
        cout<<"Case #"<<tt<<": ";
        int row1;
        int cards1[4][4];
        cin>>row1;
        row1--;
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        {
            cin>>cards1[i][j];

        }
           int row2;
        int cards2[4][4];
        cin>>row2;
        row2--;
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        {
            cin>>cards2[i][j];

        }
        int res=-1;
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        {
            if(cards1[row1][i]==cards2[row2][j])
            {

                if(res==-1)res=cards1[row1][i];
                else res=-2;
            }

        }
        if(res==-1)cout<<"Volunteer cheated!"<<endl;
        else if(res==-2 )cout<<"Bad magician!"<<endl;
        else cout<<res<<endl;

    }
  return 0;
}
