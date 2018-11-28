#include<bits/stdc++.h>
using namespace std;

#define SCAN(x) scanf("%d",&x)
#define SCAN2(x,y) scanf("%d%d",&x,&y)
#define PRI(x) printf("%d\n",x)
#define FOR(A,B,C) for(int A=B;A<C;A++)
#define RFOR(A,B,C) for(int A=B;A>=C;A--)
#define MEM(A,B) memset(A,B,sizeof(A))
#define mod 1000000007
#define gc getchar_unlocked
typedef long long int LL;
typedef long double LD;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<PII> VII;

string x;
int len;

int main()
{
    int test,cnt=0;
    SCAN(test);
    while(test--){
        cin >> x;
        cnt++;
        len = x.length();
        string p = "";
        string arr = p+x[0];
        FOR(i,1,len){
            if(x[i]>=arr[0])
                arr = x[i]+arr;
            else arr = arr +x[i];
        }
        printf("Case #%d: ",cnt);
        cout << arr << endl;
    }
    return 0;
}
