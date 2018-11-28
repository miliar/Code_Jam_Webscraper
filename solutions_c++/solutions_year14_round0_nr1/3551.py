#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <string>
#include <queue>
#include <stack>

#define sqr(x) (x*x)
#define cube(x) (x*x*x)

using namespace std;

bool check1[17],check2[17];
int first,second,grid[5][5];

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    int t;
    cin>>t;

    for (int i=1; i<=t; i++)
    {
        memset(check1,false,sizeof(check1));
        memset(check2,false,sizeof(check2));

        cin>>first;
        for (int j=0; j<4; j++)
            for (int k=0; k<4; k++)
                cin>>grid[j][k];

        for (int j=0; j<4; j++)
            check1[grid[first-1][j]]=true;

        cin>>second;
        for (int j=0; j<4; j++)
            for (int k=0; k<4; k++)
                cin>>grid[j][k];

        for (int j=0; j<4; j++)
            check2[grid[second-1][j]]=true;

        int cnt=0,choice;

        for (int j=1; j<=16; j++)
            if (check1[j]==check2[j] && check1[j])
            {
                cnt++;
                choice=j;
            }

        printf("Case #%d: ",i);
        if (cnt==1)    cout<<choice<<endl;
        else if (!cnt) cout<<"Volunteer cheated!"<<endl;
        else           cout<<"Bad magician!"<<endl;
    }

    return 0;
}
