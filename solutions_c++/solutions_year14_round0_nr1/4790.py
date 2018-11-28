#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<cmath>
#include<string.h>
#include<ctime>
#include<set>
#include<vector>
#include<stack>
#include<queue>
#include <cstdio>
//#define F first
//#define S second
//#define mp make_pair
#define inf 1000*1000*1000
#define mod 1000000007
double delta=0.0000001;
using namespace std;
int t, ind, row, row2, a[9][9], b[9][9], u[29];
int main()
{
    //ifstream cin("A-small-attempt2.in");
    //ofstream cout("A-small-attempt2.out");
    cin>>t;
    while(t--)
    {
        ind ++;
        cin>>row;
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                cin>>a[i][j];
        cin>>row2;
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                cin>>b[i][j];
        cout<<"Case #"<<ind<<": ";
        for(int j=1;j<=4;j++)
        {
            u[a[row][j]]++;
        }
        int k = 0, ans;
        for(int j=1;j<=4;j++)
        {
            if(u[b[row2][j]])
            {
                k++;
                ans = b[row2][j];
            }
        }
        for(int i=1;i<=4;i++)
            u[a[row][i]] = 0;
        if(k == 1)
            cout<<ans<<endl;
        if(!k)
            cout<<"Volunteer cheated!"<<endl;
        if(k > 1)
            cout<<"Bad magician!"<<endl;
    }
}
