
#include <cstdio>
#include <queue>

using namespace std ;

int dat[1111] ;

int minv(int i1, int i2){
    return i1 < i2 ? i1 : i2 ;
}
int maxv(int i1, int i2){
    return i1 > i2 ? i1 : i2 ;
}

int main()
{
    int T ;
    scanf("%d", &T) ;
    for(int time = 1 ; time <= T ; time++){
        printf("Case #%d: ", time) ;
        int D ;
        scanf("%d", &D) ;
        /*
        priority_queue<int> PQ ;
        for(int i = 0 ; i != D ; i++){
            int now ;
            scanf("%d", &now) ;
            PQ.push(now) ;
        }
        int ans = 1111 ;
        int sum = 0 ; 
        for(int i = 1000 ; i > 0 ; i--){
            while(PQ.top() > i){
                int tmp = PQ.top() ;
                PQ.pop() ;
                PQ.push(tmp/2) ;
                PQ.push(tmp/2 + tmp%2) ;
                sum++ ;
            }
            ans = minv(ans, sum + PQ.top()) ;
            if(sum > ans)
                break ;
        }
        printf("%d\n", ans) ;
        */
        for(int i = 0 ; i != D ; i++)
            scanf("%d", dat+i) ;
        int ans = 9999 ; 
        for(int i = 1 ; i <= 1000 ; i++){
            int now = 0 ;
            for(int j = 0 ; j != D ; j++){
                if(dat[j] <= i)
                    ;
                else
                    now += maxv((dat[j]/i + bool(dat[j]%i)) - 1, 0) ;
            }
            ans = minv(ans, now+i) ;
        }
        printf("%d\n", ans) ;
    }
}


