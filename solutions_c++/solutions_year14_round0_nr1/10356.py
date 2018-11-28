#include<stdio.h>
#include<conio.h>
int main()
{
int arr[4][4],match[4],re[4][4],match1[4],row1[101],row2[101],t,t1,i,j,r,q,c=0,y;
freopen("input2.in","r",stdin);
freopen("magic2.txt","w",stdout);
scanf("%d",&t);
for(t1=0;t1<t;t1++){
c=0;
scanf("%d",&row1[t1]);
for(i=0;i<4;i++){
for(j=0;j<4;j++){
scanf("%d",&arr[i][j]);
}
}
scanf("%d",&row2[t1]);
for(i=0;i<4;i++){
for(j=0;j<4;j++){
scanf("%d",&re[i][j]);
}
}
r=row1[t1];
for(i=0;i<4;i++){
match[i]=arr[r-1][i];
}
q=row2[t1];
for(i=0;i<4;i++){
match1[i]=re[q-1][i];
}
for(i=0;i<4;i++){
for(j=0;j<4;j++){
if(match[i]==match1[j]){
c++;
y=match[i];
}
}
}
if(c==0){
printf("Case #%d: Volunteer cheated!\n",t1+1);
}
else if(c==1){
printf("Case #%d: %d\n",t1+1,y);
}
else if(c>1){
printf("Case #%d: Bad magician!\n",t1+1);
}

}
return 0;
}