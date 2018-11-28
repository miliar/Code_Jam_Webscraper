#include <bits/stdc++.h>
#define reset(arr,j) memset(arr,j,sizeof(arr));
#define pb push_back
#define f first
#define s second
#define mp make_pair
#define vec vector<int>
#define LL long long
#define fa(i,n) for(int i=0;i<n;i++)
#define fb(i,n) for(int i=1;i<=n;i++)
#define take(vec,n) for(int i=0;i<n;i++){int a; cin >> a; vec.pb(a);};
#define print(arr,n) fa(i,n) cout << arr[i] << " "; cout << endl;
#define mod(n,m) (n + m) % m;
#define fd(i,n) for(int i=n-1;i>=0;i--)
#define vpair vector < pair <int ,int> >
#define Vec(name,size) vector<int> name(size);
#define matrix vector<vector<LL> >
#define initmatrix(m,a,b,x) fa(i,a){ vector<LL> c; m.pb(c); fa(j,b) m[i].pb(x);};
#define printmatrix(M) fa(i,M.size()){ fa(j,M[i].size()) cout << M[i][j].f <<" "; cout << endl;}
#define O4 10005
#define O5 100006
#define O6 1000005
#define O7 10000007
int dx[] = {0,1,-1,0,1,-1,1,-1,-2,2,0,0},dy[] = {1,0,0,-1,-1,1,1,-1,0,0,-2,2};
using namespace std;
//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//

main(){
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    ios_base::sync_with_stdio(0);cin.tie(0);
    int T;
    cin >> T;
    for(int t = 1;t <= T;t++){
        int n;
        cin >> n;
        vec v;
        take(v,n);
        int x = 0,y = 0,maxdiff = 0;
        fa(i,n-1){
            maxdiff = max(v[i]-v[i+1],maxdiff);
        }
        fa(i,n-1){
            if(v[i] >= maxdiff)
                y+= maxdiff;
            else if(v[i] < maxdiff)
                y+= v[i];
        }
        for(int i = 1;i < n;i++){
            if(v[i] < v[i-1])
                x+= v[i-1] - v[i];
        }
        printf("Case #%d: %d %d\n",t,x,y);
    }

}
