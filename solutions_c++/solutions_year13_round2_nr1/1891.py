#include <vector>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;

vector<int> m(1000002);
vector<int> as(1000002);

int main()
{
    int T;
    int A, N;
    int ans;
    int cnt;
    int his;
    scanf("%d", &T);
    int tmp;
    for(int i=1;i<=T;++i)
    {
        scanf("%d%d",&A, &N);
        for(int j=0;j<N;++j)
            scanf("%d", &m[j]);
        sort(m.begin(), m.begin()+N);
        ans = 0;
        his = 0;
        tmp = N-1;
        if(A==1){
            printf("Case #%d: %d\n", i, N);
            continue;
        }
        
        for(int j=0;j<N;++j)
        {
            if(A>m[j]){
                as[j]=his+N-j;
                A=A+m[j];
                continue;
            }
            else{
                ans = A;
                cnt = 0;
                
                while(ans<=m[j]){
                    ans = 2*ans - 1;
                    ++cnt;
                }
                if(cnt>N-j){
                    as[j]=his+N-j;
                    his = his+N-j;
                    tmp = j;
                    break;
                }
                else{
                    A = ans+m[j];
                    as[j]=his+N-j;
                    his+=cnt;
                }
            }
        }
        
        for(int j=0;j<=tmp;++j)
            if(as[j]<his)
                his = as[j];
        printf("Case #%d: %d\n", i, his);
    }
    return 0;
}
