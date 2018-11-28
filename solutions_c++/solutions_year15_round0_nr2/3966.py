#include <bits/stdc++.h>
using namespace std;

#define FOR(p,star,end) for(int p = star ; p<end ; p++)
#define FORR(p,star,end) for(int p = star ; p>=end ; p--)
#define INF 1000000000
#define MOD 1000000007
#define MAX 1002

#define pii pair<int ,int >
#define vi vector<int>
#define vii vector< pair<int ,int> >
#define pb push_back
#define mp make_pair
#define ll long long
int res;
map<vi,bool>vis;
void solve(vi A , int steps)
{

    if(A.size()==0)
        return ;

    sort(A.begin(),A.end());
    //  if(steps+A[A.size()-1]>res)
//        return
    if(vis.find(A)!=vis.end())
        return ;

    vis[A]=1;
    res = min ( res , A[A.size()-1] + steps);
    if(A.back()==1)
        return ;
    /* FOR(i,0,A.size())
     {
         cout << A[i] << " ";
     }
     cout <<endl;*/
    FORR(j,A.size()-1,0)
    {
        int cur = A[j];
        vi B;
        FOR(q,0,A.size())
        if(q!=j)
            B.pb(A[q]);
        FOR(k,1,cur/2 + 1 )
        {

            B.pb(k);
            B.pb(cur-k);


            solve(B,steps+1);

            B.pop_back();
            B.pop_back();


        }
    }
}
int main()
{
     freopen("B-small-attempt4.in","r",stdin);
     freopen("out.txt","w",stdout);

    int t;
    cin >> t;
    FOR(tc,1,t+1)
    {
        int n;

        cin >> n ;

        vi A;
        int u ;
        FOR(i,0,n)
        {
            scanf("%d",&u);
            A.pb(u);
        }
        res=INF;

        solve(A,0);

        printf("Case #%d: %d\n",tc,res);

        vis.clear();

    }

    return 0;


}





