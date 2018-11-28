#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
#include<cstring>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<string>
#include<iterator>
#include<string>
#include<sstream>
#include<cassert>
#include<ctime>
#include<cmath>

#define MP make_pair
#define PB push_back
#define X first
#define Y second
#define oo 2000000000
#define MOD 1000000007
#define LL long long int
#define PII pair<int,int>
#define DEBUG 0

#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;

using namespace std;
vector<int>  v1,v2;
int main(){
    int T;
    freopen("out.txt","w",stdout);
    freopen("in.txt","r",stdin);
    scanf("%d",&T);
    for(int I=1;I<=T;I++){
        int r1,r2,x;
        v1.clear(), v2.clear();
        scanf("%d",&r1);
        for(int i=0;i<4;i++) for(int j=0;j<4;j++){
            scanf("%d",&x);
            if(i == r1-1) v1.PB(x);
        }
        scanf("%d",&r2);
        for(int i=0;i<4;i++) for(int j=0;j<4;j++){
            scanf("%d",&x);
            if(i == r2-1) v2.PB(x);
        }
        vector<int> res(8);
        sort(v1.begin(),v1.end());
        sort(v2.begin(),v2.end());
        auto it=set_intersection(v1.begin(),v1.end(),v2.begin(),v2.end(),res.begin());
        res.resize(it-res.begin());
        trace1(res.size());
        printf("Case #%d: ",I);
        if(res.size() == 1) printf("%d\n", res[0]);
        else if(res.size() > 1) puts("Bad magician!");
        else puts("Volunteer cheated!");
    }
    return 0;
}
