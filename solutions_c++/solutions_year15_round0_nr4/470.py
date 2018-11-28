#include<stdio.h>
#include<algorithm>
using namespace std;
int main(){
    int test;
    scanf("%d", &test);
    for(int tt=1; tt<=test; tt++){
        int x, r, c;
        scanf("%d %d %d", &x, &r, &c);
        if(r>c)swap(r,c);
        printf("Case #%d: ", tt);
        if(x>=4){
            if(r>=3 && c>=4)printf("GABRIEL\n");
            else printf("RICHARD\n");
        }
        else if(x==3){
            if((r==3 || c==3)&& r>=2)printf("GABRIEL\n");
            else printf("RICHARD\n");
        }
        else if(x==2){
            if(r%2==0 || c%2==0)printf("GABRIEL\n");
            else printf("RICHARD\n");
        }
        else printf("GABRIEL\n");
    }
    return 0;
}
