// Example program
#include <iostream>
#include <string>

using namespace std;

int cnt;

int visited[10];

void updateCnt(long long x) {
    while(x > 0) {
        if(visited[x % 10] == 0) {
            visited[x % 10] = 1;
            cnt++;
        }
        x /= 10;
    }
}

int main()
{
  long long t,n;
  scanf("%lld",&t);
  for(int k = 0 ; k < t ; k++) {
    cnt = 0;
    for(int i = 0 ; i < 10 ; i++) visited[i] = 0;
    scanf("%lld",&n);
    if(n<=0) {
        printf("Case #%d: INSOMNIA\n",k+1);
        continue;
    }
    int i = 1;
    for(; i < 1000000; i++) {
        updateCnt(i*n);
        if(cnt >= 10) {
            printf("Case #%d: %lld\n",k+1,i*n);
            break;
        }
    }
    if(i == 1000000) {
        printf("Case #%d: INSOMNIA\n",k+1);
    }
  }
}
