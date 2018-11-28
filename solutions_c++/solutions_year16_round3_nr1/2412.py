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

int main()
{
    int test,cnt=0;
    SCAN(test);
    while(test--){
        cnt++;
        printf("Case #%d: ",cnt);
        int n;
        SCAN(n);
        int arr[n];
        FOR(i,0,n)
            SCAN(arr[i]);
        while(1){
            int check=0,cnt=0;
            string ans;
            FOR(i,0,n){
                if(arr[i]!=0){
                    check=1;
                    break;
                }
            }
            if(!check)
                break;
            int maxv =arr[0],maxi=0,maxi2,flag=0;
            FOR(i,0,n){
                if(arr[i]>maxv){
                    maxi = i;
                    maxv = arr[i];
                }
                if(arr[i]!=0)
                    cnt+=arr[i];
            }
            FOR(i,0,n){
                if(arr[i]==maxv && i!=maxi && arr[i]!=1){
                    maxi2 = i;
                    flag = 1;
                    break;
                }
            }
            if(cnt==2){
                FOR(i,0,n){
                    if(arr[i]!=0){
                        ans += (char)(65+i);
                        arr[i] = 0;
                    }
                }
            }
            else{
                if(flag){
                    ans += (char)(65+maxi);
                    ans += (char)(65+maxi2);
                    arr[maxi]--;
                    arr[maxi2]--;
                }
                else{
                    ans += (char)(65+maxi);
                    arr[maxi]--;
                }
            }
            cout << ans << " ";
        }
        printf("\n");
    }
    return 0;
}
