#include<stdio.h>
#include<algorithm>
#include<queue>
using namespace std;

#define mp make_pair

bool digit[10];
priority_queue<pair<int,int>> Q;
int main(){
    int n,t,i,j,k;
    int in,ans,sum;

    //Q.push(mp(1,2));
    //Q.push(mp(5,1));
   // Q.push(mp(10,10));

    //printf("%d %d",Q.top().first,Q.top().second);

    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    scanf("%d",&t);
    //t = 1000000;
    for(k=1;k<=t;k++) {
        scanf("%d",&n);
        sum = 0;
        while(!Q.empty()) Q.pop();

        for(i=0;i<n;i++) {
            scanf("%d",&in);
            sum += in;
            Q.push(mp(in,i));
        }

        printf("Case #%d: ",k);

        pair<int,int> tmp1,tmp2;

        while(sum > 3) {
            tmp1 = Q.top();
            Q.pop();
            tmp2 = Q.top();
            Q.pop();

            if(tmp1.first > tmp2.first) {
                printf("%c%c ",'A'+tmp1.second, 'A'+tmp1.second);
                tmp1.first -= 2;
                sum-=2;
                if(tmp1.first > 0) Q.push(tmp1);
                Q.push(tmp2);
            } else {
                printf("%c%c ",'A'+tmp1.second, 'A'+tmp2.second);
                tmp1.first--;
                tmp2.first--;
                sum-=2;
                if(tmp1.first > 0) Q.push(tmp1);
                if(tmp2.first > 0) Q.push(tmp2);
            }

        }

        if(sum == 3) {
            printf("%c ",'A'+Q.top().second);
            Q.pop();
            printf("%c",'A'+Q.top().second);
            Q.pop();
            printf("%c",'A'+Q.top().second);
        }
        else if(sum == 2) {
            printf("%c",'A'+Q.top().second);
            Q.pop();
            printf("%c",'A'+Q.top().second);
        }
        else if(sum == 1) {
            printf("%c",'A'+Q.top().second);
        }

        printf("\n");
    }
}
