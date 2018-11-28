#include<bits/stdc++.h>
using namespace std;

#define LL long long int
#define ULL unsigned LL
#define PII pair<int,int>
#define PB push_back
#define MP make_pair
#define INF 1000000000
#define MOD 1000000007

int main(){
    int t, cs=0;
    scanf("%d", &t);
    while(t--){
        printf("Case #%d: ", ++ cs);
        int i,j,r1,r2,m1=0, m2=0, x;
        cin >> r1;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++){
                cin >> x;
                if(i == r1)
                    m1 |= (1<<x);
            }
        cin >> r2;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++){
                cin >> x;
                if(i == r2)
                    m2 |= (1<<x);
            }
        int an = (m1&m2);
        if(an == 0)
            printf("Volunteer cheated!\n");
        else if((an&(an - 1)) != 0)
            printf("Bad magician!\n");
        else{
            int r = 0;
            while((an&1) == 0){
                r ++, an >>= 1;
            }
            printf("%d\n", r);
        }
    }
    return 0;
}

