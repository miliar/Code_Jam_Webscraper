///     Raihan Ruhin
///     CSE, Jahangirnagar University.
///     Dhaka-Bangladesh.
///     id: raihanruhin (topcoder / codeforces / codechef / hackerrank), 3235 (lightoj)
///     mail: raihanruhin@ (yahoo / gmail / facebook)
///     blog: ruhinraihan.blogspot.com

#include<bits/stdc++.h>
using namespace std;

#define SET(a) memset(a,-1,sizeof(a))
#define CLR(a) memset(a,0,sizeof(a))
#define PI acos(-1.0)

#define MOD 1000000007
#define MX 100010

#define READ freopen("A-small-attempt0.in", "r", stdin)
#define WRITE freopen("output.txt", "w", stdout)


int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    READ;
    WRITE;

    int tc,kk=1, a, am[6][6], b, bm[6][6];
    cin>>tc;

    while(tc--)
    {
        vector<int>ans;
        cin>>a;
        a--;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>am[i][j];
        cin>>b;
        b--;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>bm[i][j];

        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                if(am[a][i]==bm[b][j])
                    ans.push_back(am[a][i]);
                    //cout<<am[a][i]<<" "<<bm[b][i]<<endl;

        //for(int i=0;i<ans.size();i++) cout<<ans[i]<<endl;
        if(ans.size()==1)
            cout<<"Case #"<<kk++<<": "<<ans[0]<<endl;
        else if(ans.size()>1)
            cout<<"Case #"<<kk++<<": Bad magician!"<<endl;
        else cout<<"Case #"<<kk++<<": Volunteer cheated!"<<endl;
    }
    return 0;
}

