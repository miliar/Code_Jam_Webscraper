#include <cstdio>
#include <algorithm>
using namespace std;
int a[5], b[5], A, B;
int main(){
    int T, x;
    scanf("%d", &T);
    for(int c=1;c<=T;c++){
        scanf("%d", &A);
        for(int i=1;i<=4;i++){
            for(int j=1;j<=4;j++){
                if(i==A)scanf("%d", &a[j]);
                else scanf("%d", &x);
            }
        }
        scanf("%d", &B);
        for(int i=1;i<=4;i++){
            for(int j=1;j<=4;j++){
                if(i==B)scanf("%d", &b[j]);
                else scanf("%d", &x);
            }
        }
        int cnt=0;
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                if(a[i]==b[j])cnt++, x=a[i];
        printf("Case #%d: ", c);
        if(cnt==1)printf("%d\n",x);
        else if(cnt)printf("Bad magician!\n");
        else printf("Volunteer cheated!\n");
    }
    return 0;
}
