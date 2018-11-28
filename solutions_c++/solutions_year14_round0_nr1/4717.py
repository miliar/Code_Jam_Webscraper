#include <bits/stdc++.h>

#define rep(i,n) for(int i=0; i<n; i++)
#define repa(i,a,b,d) for(int i=a; i<=b; i+=d)
#define repd(i,a,b,d) for(int i=a; i>=b; i-=d)
#define repi(it,stl) for(auto it = (stl).begin(); (it)!=stl.end(); ++(it))
#define sz(a) ((int)(a).size())
#define mem(a,n) memset((a), (n), sizeof(a))
#define all(n) (n).begin(),(n).end()
#define rall(n) (n).rbegin(),(n).rend()
#define mp(a,b) make_pair((a),(b))
#define pii pair<int,int>
#define vi vector<int>
#define vs vector<string>
#define sstr stringstream
#define myfind(v,x) (find(all((v)),(x))-(v).begin())

typedef long long ll;
using namespace std;

int main()
{

#ifndef ONLINE_JUDGE
    freopen("code.txt", "rt", stdin);
    freopen("out.txt", "wt", stdout);
#endif

    int tst;
    scanf("%d", &tst);
    repa(tt, 1, tst, 1) {
        int q1, q2;
        int mat1[4][4] = {0}, mat2[4][4] = {0};
        vi res(4);

        scanf("%d", &q1);
        rep(i, 4) rep(j, 4) scanf("%d", &mat1[i][j]);

        scanf("%d", &q2);
        rep(i, 4) rep(j, 4) scanf("%d", &mat2[i][j]);
        --q1, --q2;

        sort(mat1[q1], mat1[q1] + 4);
        sort(mat2[q2], mat2[q2] + 4);

        auto it = set_intersection(mat1[q1], mat1[q1] + 4, mat2[q2], mat2[q2] + 4, res.begin());
        res.resize(it - res.begin());
        printf("Case #%d: ", tt);
        if(sz(res) == 0)
            printf("Volunteer cheated!\n");
        else if(sz(res) == 1)
            printf("%d\n", *res.begin());
        else
            printf("Bad magician!\n");

    }
    return 0;
}