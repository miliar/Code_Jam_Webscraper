#include<stdio.h>
#include<algorithm>
#include<string>
using namespace std;
string Print(int A, int B, int C){
    if(A+B+C==1){
        if(A)return "R";
        if(B)return "P";
        if(C)return "S";
    }
    string r1, r2;
    if(A%2==0){
        r1 = Print(A/2, B/2, C-C/2);
        r2 = Print(A/2, B-B/2, C/2);
    }
    else if(B%2==0){
        r1 = Print(A/2, B/2, C-C/2);
        r2 = Print(A-A/2, B/2, C/2);
    }
    else{
        r1 = Print(A-A/2, B/2, C/2);
        r2 = Print(A/2, B-B/2, C/2);
    }
    if(r1 < r2)return r1+r2;
    return r2+r1;
}
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int TC, TT, A,B,C, m1, m2, n;
    scanf("%d",&TC);
    for(TT=1;TT<=TC;TT++){
        printf("Case #%d: ", TT);
        scanf("%d%d%d%d",&n,&A,&B,&C);
        m1 = min(min(A,B),C);
        m2 = max(max(A,B),C);
        if(m2>m1+1){
            printf("IMPOSSIBLE\n");
            continue;
        }
        printf("%s\n",Print(A,B,C).c_str());
    }
}
