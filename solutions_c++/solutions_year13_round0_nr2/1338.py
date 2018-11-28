#include <iostream>
#include <vector>

using namespace std;

bool solve(){
    int n,m; cin>>n>>m;
    vector<int> mrow(n,0), mcol(m,0);
    vector<vector<int> > lawn(m,vector<int>(n,0));

    for (int yi=0; yi<n; yi++)
        for (int xi=0; xi<m; xi++)
        {
            cin>>lawn[xi][yi];
            if(lawn[xi][yi]>mrow[yi]) mrow[yi]=lawn[xi][yi];
            if(lawn[xi][yi]>mcol[xi]) mcol[xi]=lawn[xi][yi];
        }

    bool result=true;
    for (int yi=0; yi<n; yi++)
        for (int xi=0; xi<m; xi++)
            if ((lawn[xi][yi]!=mrow[yi]) && (lawn[xi][yi]!=mcol[xi])) result=false;
    return result;
}

int main()
{
    int t; cin>>t;
    for (int i=1; i<=t; i++)
        if (solve()) cout<<"Case #"<<i<<": "<<"YES"<<endl;
        else cout<<"Case #"<<i<<": "<<"NO"<<endl;
    return 0;
}

