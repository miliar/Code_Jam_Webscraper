#include <bits/stdc++.h>
using namespace std;
#define FL(a) memset(a, 0, sizeof a);
#define pi(a) cout <<  a << endl;
#define si(n) scanf("%d",&n)
#define pis(n) printf("%d ",n);
#define FREP(b) for(int i=0;i<b;i++)
#define REP(a,b,c) for(int a=b;a<c;a++)
typedef pair<int,int> ii;
typedef long long LL;
/*
struct data{
};
bool operator < (const data &a1, const data &a2){
}
*/
int A[4][4];
int B[4][4];
int a,b;
int main()
{
    int tc;
    cin >> tc;
    REP(t,0,tc){
        cin >> a;
        a--;
        map<int, int> store;
        FREP(4) REP(j,0,4){
            cin >> A[i][j];
            if(i == a) store[A[i][j]] = 1;
        }
        cin >> b;
        b--;
        int same = 0, ans;
        FREP(4) REP(j,0,4){
            cin >> B[i][j];
            if(i == b){
                same += store[B[i][j]];
                if(store[B[i][j]]) ans = B[i][j];
            }
        }
        printf("Case #%d: ", t+1);
        if(same == 1) cout << ans << endl;
        else if(same > 1) cout << "Bad magician!" << endl;
        else cout << "Volunteer cheated!" << endl;
    }
    return 0;
}

