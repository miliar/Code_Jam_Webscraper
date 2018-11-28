//
#include<iostream>
#include<cmath>
#include<algorithm>
#include<vector>
#include<cstring>
#include<string>
#include<map>
#include<set>
#include<climits>
#include<fstream>
#include<iomanip>
#include<queue>
#include<stack>
#define lli long long

using namespace std;


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    ifstream cin("D.in");
    ofstream cout("D.out");


    int T,a,b,c;
    cin>>T;
    for(int t1=1;t1<=T;t1++)
    {
        cin>>a>>b>>c;
        cout<<"Case #"<<t1<<": ";
        for(int i=1;i<a;i++)
        {
            cout<<i<<" ";
        }
        cout<<a<<"\n";
    }
    return 0;
}


