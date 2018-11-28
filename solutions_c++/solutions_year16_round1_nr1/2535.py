#include<stdio.h>
#include<string.h>
#include<deque>
using namespace std;

int main(){
    freopen("/Users/WarYi/Desktop/a.in", "r", stdin);
    freopen("/Users/WarYi/Desktop/a.out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++){
        char s[1005];
        scanf("%s", s);
        int len = strlen(s);

        
        deque<char> dq;
        dq.push_front(s[0]);
        int cnt = 1;
        while(cnt < len){
            if(dq.front() <= s[cnt])
                dq.push_front(s[cnt]);
            else
                dq.push_back(s[cnt]);
            
            cnt++;
        }
        
        printf("Case #%d: ", t);
        while(!dq.empty()){
            printf("%c", dq.front());
            dq.pop_front();
        }
        printf("\n");
    }
}