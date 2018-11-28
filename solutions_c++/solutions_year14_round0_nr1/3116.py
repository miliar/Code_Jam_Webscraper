#include <map>
#include <set>
#include <cmath>
#include <stack>
#include <queue>
#include <cstdio>
#include <vector>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define rep(i,n) for(int i=0; i<n; i++)
#define fr(i,a,b) for(int i=a; i<=b; i++)
#define debug(a) cout<< #a << " = " <<a<<endl;

#define ff first
#define ss second
#define mp make_pair
#define pb push_back

#define MaxInt 2147483647
#define INF 12512523232344LL
#define pi 3.1415926535897932

#define read(a) scanf("%d",&a);
#define read2(a,b) scanf("d",&a,&b);
#define read3(a,b,c) scanf("d%d",&a,&b,&c);

int TestCase,row1,row2,cnt,A[100][100],B[100][100],T;

int main(){

    #ifndef ONLINE_JUDGE
    freopen("input.in", "r", stdin);
    freopen("OUTPUT.OUT", "w", stdout);
    #endif // ONLINE_JUDGE

    cin>>T;
    for(int TestCase = 1; TestCase <= T; TestCase++)
    {

        cnt = 0;
        cin>>row1;
        for(int i=1; i<=4; i++)
        {
            for(int j=1; j<=4; j++)
            {
                cin>>A[i][j];
            }
        }

        cin>>row2;

        for(int i=1; i<=4; i++)
        {
            for(int j=1; j<=4; j++)
            {
                cin>>B[i][j];
            }
        }
        int val = -1;
        for(int i=1; i<=4; i++)
        {
            for(int j = 1; j<=4; j++)
            if(A[row1][i] == B[row2][j])
            {
                val = A[row1][i];
                cnt++;
            }
        }
        printf("Case #%d: ",TestCase);
        if(cnt == 1) cout<<val<<endl;
        else if(cnt>=2) cout<<"Bad magician!"<<endl;
        else cout<<"Volunteer cheated!"<<endl;

    }



return 0;
}

