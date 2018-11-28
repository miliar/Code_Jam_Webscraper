#include <bits/stdc++.h>
#define reset(arr,j) memset(arr,j,sizeof(arr));
#define pb push_back
#define f first
#define s second
#define vec vector<int>
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
#define printmatrix(M) fa(i,M.size()){ fa(j,M[i].size()) cout << M[i][j]; cout << endl;}
int dx[] = {0,1,-1,0,1,-1,1,-1,-2,2,0,0},dy[] = {1,0,0,-1,-1,1,1,-1,0,0,-2,2};
using namespace std;
//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//

bool board[10001][10001];
int R,C,N;
int getNeig(int x,int y){
    int ret = 0;
    fa(i,4){
        int xx = x+dx[i],yy = y+dy[i];
        if(xx >= 0 && xx < R && yy >= 0 && yy < C){
            ret+= board[xx][yy];
        }
    }
    return ret;
}
main(){
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    cin >> T;
    for(int t = 1;t <= T;t++){
        reset(board,0);
        cin >> R >> C >> N;
        int N2 = N;
        for(int i = 0;i < R;i++){
            for(int j = 0;j < C;j++){
                int neigh = getNeig(i,j);
                if(!neigh && N){
                    board[i][j] = 1;
                    N--;
                }
            }
        }
        //cout << "here\n";
//        fa(i,R){
//            fa(j,C){
//                cout << board[i][j];
//
//            }
//            cout << endl;
//        }
        priority_queue<pair<int,pair<int,int> >,vector<pair<int,pair<int,int> > >,greater<pair<int,pair<int,int> > > > pq;
        fa(i,R) fa(j,C){
            if(!board[i][j]){
                pq.push(mp(getNeig(i,j),mp(i,j)));
                //cout << getNeig(i,j) << " " << i << " " << j << endl;
            }
        }

        int ans = 0;
        while(N--){
            pair<int,pair<int,int> > top = pq.top(); pq.pop();
            ans+= top.f;
        }

        int ans2 = 0;
        reset(board,0);
        bool first = (C > 1);
        for(int i = 0;i < R;i++){
            for(int j = first;j < C;j++){
                int neigh = getNeig(i,j);
                if(!neigh && N2){
                    board[i][j] = 1;
                    N2--;
                }
                first = 0;
            }
        }
        //cout << N2 << endl;
        priority_queue<pair<int,pair<int,int> >,vector<pair<int,pair<int,int> > >,greater<pair<int,pair<int,int> > > > pq2;
        fa(i,R) fa(j,C){
            if(!board[i][j]){
                pq2.push(mp(getNeig(i,j),mp(i,j)));
            }
        }
        while(N2--){
            pair<int,pair<int,int> > top = pq2.top(); pq2.pop();
            ans2+= top.f;
        }
        printf("Case #%d: ",t);
        cout << min(ans,ans2) << endl;

    }
}
