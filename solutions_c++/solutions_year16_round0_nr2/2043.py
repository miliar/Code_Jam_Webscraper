#include <bits/stdc++.h>

using namespace std;

char A[105];
int casos;

int main(){
    scanf("%d", &casos);
    for(int v=1; v<=casos; v++){
        scanf("%s", A);
        printf("Case #%d: ", v);
        
        int ans=0;
        if(A[0]=='-') ++ans;
        for(int i=1; A[i]!='\0'; i++){
            if(A[i]!=A[i-1] and A[i] == '-') ans+=2;
        }
        printf("%d", ans);
        printf("\n"); 
    }
    return 0;
}
