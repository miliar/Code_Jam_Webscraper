#include <iostream>
#include <cstdlib>
#include <cstdio>
using namespace std;

int a[22],b[22];

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int T;
    cin>>T;
    for (int _=1;_<=T;_++){
        int aa,bb;
        cin>>aa;
        for (int i=1;i<=4;i++)
        for (int j=1;j<=4;j++){
            int x;
            scanf("%d",&x);
            a[x]=i;
        }
        cin>>bb;
        for (int i=1;i<=4;i++)
        for (int j=1;j<=4;j++){
            int x;
            scanf("%d",&x);
            b[x]=i;
        }
        int ans=0,ansn=0;
        for (int i=1;i<=16;i++) if (a[i]==aa && b[i]==bb) {ans++; ansn=i;}
        printf("Case #%d: ",_);
        if (ans==1) printf("%d\n",ansn);
        if (ans==0) printf("Volunteer cheated!\n");
        if (ans>1) printf("Bad magician!\n");
    }
 //   system("pause");
}
/*
3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

*/
