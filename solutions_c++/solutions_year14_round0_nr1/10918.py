#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
    unsigned long long  n;
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        int t; cin>>t;
        int a[5][5];
        for(int j=1;j<5;j++)
            for(int k=1;k<5;k++)
                cin>>a[j][k];
        int s;cin>>s;
        int b[5][5];
        for(int j=1;j<5;j++)
            for(int k=1;k<5;k++)
                cin>>b[j][k];
        bool f1[17],f2[17];
        for(int j=1;j<17;j++)
            f1[j]=false,f2[j]=false;
        for(int j=1;j<5;j++)
            f1[a[t][j]]=true,f2[b[s][j]]=true;
        int kk=0;
        int tt=0;
        for(int j=1;j<17;j++)
            if(f1[j] && f1[j]==f2[j])
                kk++,tt=j;
        cout<<"Case #"<<i<<": ";
        if(kk==0)
            cout<<"Volunteer cheated!";
        if(kk==1)
            cout<<tt;
        if(kk>1)
            cout<<"Bad magician!";
        cout<<endl;
            

    }
}