#include <iostream>
using namespace std;
#define CASET int ___T, case_n = 1; scanf("%d ", &___T); while (___T-- > 0)
char arr[1010];
int main() {
    CASET {
        int an1 = 0;
        int n;
        int cur=0;
        cin>>n>>arr;
        
        int i;
        for(i=0;i<=n;i++) {
            if(an1 < i)  {
                cur = cur + i - an1;
                an1 += (i - an1);
            }
            an1 += (arr[i] - '0');
        }
        
        
        printf("Case #%d: %d\n",case_n++,cur);
    }
}