#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>
using namespace std;
int main()
{
	freopen( "A-small-attempt1.in", "r", stdin );
	freopen( "A-small-attempt1.out", "w", stdout );
    int t, no;
    cin>>t;
    for(no = 0;no < t;no++)
    {
        int a[4][4],b[4][4],r1,r2,i,j,c[4],cnt =0;

        cin>>r1;
        r1--;
        for(i = 0;i < 4;i++)
            for(j = 0;j < 4;j++)
                cin>>a[i][j];

        cin>>r2;
        r2--;
        for(i = 0;i < 4;i++)
            for(j = 0;j < 4;j++)
                cin>>b[i][j];

        for(i = 0;i < 4; i++)
            c[i]=0;

        for(i = 0;i < 4;i++)
        {
            for(j = 0;j < 4;j++)
            {
                if(a[r1][i] == b[r2][j])
                {
                    c[i]++;
                    break;
                }
            }
        }

        for(i = 0;i < 4;i++)
        {
            if(c[i] == 1)
                cnt++;
        }
        if(!cnt)
        {
            cout<<"Case #"<<no+1<<": "<<"Volunteer cheated!"<<"\n";
        }
        else if(cnt >1)
        {
            cout<<"Case #"<<no+1<<": "<<"Bad magician!"<<"\n";
        }
        else
        {
            for(i = 0;i < 4;i++)
                if(c[i] == 1)
                    break;
            cout<<"Case #"<<no+1<<": "<<a[r1][i]<<"\n";
        }
    }

    return 0;
}
