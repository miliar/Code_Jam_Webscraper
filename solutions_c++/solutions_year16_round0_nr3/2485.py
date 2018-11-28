//By Tapesh Joham
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

LL isPrime(LL n)
{
    if (n <= 1)  return 1;
    if (n <= 3)  return n;
    if (n%2==0)
        return 2;
    if(n%3==0)
        return 3;
    for (LL i=5; i*i<=n; i=i+6){
        if(n%i==0)
            return i;
        if(n%(i+2)==0)
            return i+2;
    }
    return n;
}

char alpha[]={'0','1'};

void compute(string prefix,vector<string>& arr,int s)
{
    if(s==0){
        arr.push_back(prefix+"1");
        return;
    }
    FOR(i,0,2){
        string new_prefix=prefix+alpha[i];
        compute(new_prefix,arr,s-1);
    }
}

LL power(int base,int p)
{
    if(p==0)
        return 1;
    LL ans = 1;
    FOR(i,0,p)
        ans *= base;
    return ans;
}

int main()
{
    int test,n,x,cnt=0;
    SCAN(test);
    while(test--){
        cnt++;
        SCAN2(n,x);
        vector<string> arr;
        printf("Case #%d:\n",cnt);
        compute("1",arr,n-2);
        int iter=0;
        FOR(i,0,(int)arr.size()){
            if(iter==x)
                break;
            int flag = 1;
            vector<LL> divis;
           // cout << arr[i] << " ";
            FOR(j,2,11){
                LL sum = 0,ans;
                FOR(k,0,16){
                    if(arr[i][k]=='1')
                        sum += power(j,n-1-k);
                }
                //cout << sum << " ";
                ans = isPrime(sum);
               // cout << ans << " ";
                if(ans==sum){
                    flag = 0;
                    break;
                }
                divis.push_back(ans);
            }
            if(flag){
                cout << arr[i] << " ";
                FOR(it,0,(int)divis.size())
                    cout << divis[it] << " ";
                printf("\n");
                iter++;
            }
        }
    }
    return 0;
}
