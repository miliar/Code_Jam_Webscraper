#include <iostream>
#include <cstdio>
#include <queue>

using namespace std;

int main()
{
    freopen("B-large (2).in" , "r" , stdin);
    freopen("myout.txt" , "w" , stdout);
    int T;
    int N;
    int ind;
    int counting[2501];
    priority_queue<int> pq;
    scanf("%d" , &T);
    for(int i = 1; i <= T; i ++){
        for(int c = 1; c <= 2500; c++){
            counting[c] = 0;
        }
        scanf("%d" , &N);
        for(int c = 0; c < 2 * N - 1; c++){
            for(int c1 = 0; c1 < N; c1++){
                scanf("%d" , &ind);
                counting[ind] ++;
            }
        }
        for(int c = 1; c <= 2500; c++){
            if(counting[c] % 2 == 1){
                pq.push(-c);
            }
        }
        printf("Case #%d: " , i);
        while(!pq.empty()){
            printf("%d " , -pq.top());
            pq.pop();
        }
        printf("\n");
    }
    return 0;
}
