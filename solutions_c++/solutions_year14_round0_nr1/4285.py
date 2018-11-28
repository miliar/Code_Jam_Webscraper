#include<stdio.h>

int A[5][5],B[5][5];

int main() { int T,i,j,k,a,b,count,flag; scanf("%d",&T); for(k=1;k<=T;k++) { scanf("%d",&a); for(i=0;i<4;i++) for(j=0;j<4;j++) scanf("%d",&A[i][j]); scanf("%d",&b);

for(i=0;i<4;i++) for(j=0;j<4;j++) scanf("%d",&B[i][j]); count=0;flag=0;int num; for(i=0;i<4;i++) for(j=0;j<4;j++) if(A[a-1][i]==B[b-1][j]) { count++; num=A[a-1][i]; } if(count==0) printf("Case #%d: Volunteer cheated!\n",k); else if(count==1) printf("Case #%d: %d\n",k,num); else if(count>1) printf("Case #%d: Bad magician!\n",k); } }
