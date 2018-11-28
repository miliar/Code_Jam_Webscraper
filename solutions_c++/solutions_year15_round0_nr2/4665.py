#define _CRT_SECURE_NO_WARNINGS

#define max(a,b) ((a) > (b) ? (a) : (b))
#include<stdio.h>
#include<queue>

using namespace std;

typedef priority_queue<int> PQ;
struct Data{ PQ q; int t; };
Data data[100][100];

int main(void){

    int T;
    scanf("%d",&T);

    for(int r = 0;r < T;++r){
        int d;
        int p[2000];
        int ans = 0;
        PQ q;
        scanf("%d",&d);
        for(int i = 0;i < d;++i){
            scanf("%d",p+i);
            q.push(p[i]);
        }
        data[0][0].q = q;
        data[0][0].t = q.top();

        //printf("%d ",d);
        //for(int i = 0;i < d;++i){
        //    printf("%d ",p[i]);
        //}
        //printf("\n");

        // >3なところから何回3を引き出すか、じゃないかなぁ。
        // その後で、その回数+全体のmaxじゃないかなぁ。
        // -> ちがう。一回一回、そのまま行くか、maxを分解するかを判断しないと行けない。
        // -> たぶん、さらに分解方法を3-にするか、当分にするかで選択が発生する。
        int mintime = q.top();
        for(int i = 0;i < 0xFF;++i){
            q = data[0][0].q;
            int b = i;
            int st = 0;
            while(b){
                int t = q.top();
                if(t<=3) break;
                q.pop();
                if(b&1){
                    q.push(3);
                    q.push(t-3);
                }else{
                    q.push(t/2);
                    q.push(t/2+(t&1));
                }
                b>>=1;
                ++st;
                int nt = st + q.top();
                if(nt < mintime){
                    mintime = nt;
                }
            }
        }
        ans = mintime;

        printf("Case #%d: %d\n",r+1,ans);
    }

}
