#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <utility>
#include <algorithm>

using namespace std;

int main(int argc, char **argv)
{
    int T, a, b, a1[4][4], a2[4][4], answer;
    cin>>T; //number of cases
    for(int i=1;i<=T;i++)
    {
        int counter=0;
        cin>>a;
        a--;
        for (int ii=0;ii<4;ii++)
        {
            for(int c=0;c<4;c++) cin >> a1[ii][c];
        }
        cin>>b;
        b--;
        for (int iii=0;iii<4;iii++)
        {
            for(int c1=0;c1<4;c1++) cin >> a2[iii][c1];
        }
        for (int i4=0; i4<4; i4++)
        {
            for (int i5=0; i5<4; i5++)
            {
                if(a1[a][i4]==a2[b][i5])
                {
                    counter++;
                    answer=a1[a][i4];
                }
            }
        }
        if (counter==0) cout<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
        if (counter==1) cout<<"Case #"<<i<<": "<<answer<<endl;
        if (counter>=2) cout<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
    }
    return 0;
}
