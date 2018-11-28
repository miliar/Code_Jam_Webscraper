#include <bits/stdc++.h>
#include <unordered_map>
#define reset(arr,j) memset(arr,j,sizeof(arr));
#define pb push_back
#define f first
#define s second
#define mp make_pair
#define LL long long
#define fa(i,n) for(int i=0;i<n;i++)
#define take(vec,n) vector<int> vec; for(int i=0;i<n;i++){int a; cin >> a; vec.pb(a);};
#define print(arr,n) fa(i,n) cout << arr[i] << " "; cout << endl;
#define fd(i,n) for(int i=n-1;i>=0;i--)
#define vpair vector < pair <int ,int> >
#define Vec(name,size) vector<int> name(size);
#define matrix vector<vector<LL> >
#define initmatrix(m,a,b,x) fa(i,a){ vector<LL> c; m.pb(c); fa(j,b) m[i].pb(x);};
#define printmatrix(M) fa(i,M.size()){ fa(j,M[i].size()) cout << M[i][j].f <<" "; cout << endl;}
int dx[] = {0,1,-1,0,1,-1,1,-1,-2,2,0,0},dy[] = {1,0,0,-1,-1,1,1,-1,0,0,-2,2};
using namespace std;
//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//
main(){
    freopen("input.in","r",stdin);
    freopen("out.in","w",stdout);
    int T;
    cin >> T;
    for(int t=1;t<= T;t++){
        int n;
        string ppl;
        cin >> n >> ppl;
        int ans = 0,stood = 0;
        fa(i,ppl.size()){
            int x = ppl[i]-'0';
            //cout << ans << " " << stood << endl;
            if(stood >= i){
                stood+= x;
            }
            else if(x){
                ans += i - stood;
                stood += x+(i-stood);
            }

        }
        printf("Case #%d: %d\n",t,ans);
    }
}
