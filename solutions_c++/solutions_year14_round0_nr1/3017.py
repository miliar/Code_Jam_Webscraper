 #include<iostream>
 #include<cstdio>
 #include<cstdlib>
 #include<cstring>
 #include<cmath>
 #include<algorithm>
 #include<vector>
 #include<map>
 #include<utility>
 #define mod 1000000007
 

 using namespace std;
 int main(){
 freopen("input.txt","r",stdin);
 freopen("output.txt","w",stdout);
 int t,x=1;
 scanf("%d",&t);
 while(t--){
            
  int ans1,ans2,a[4][4],i,j,b[4][4],flag1=0,flag2=0,flag3=0,flag4=0,ans=0;
  scanf("%d",&ans1);
  
  for(i=0;i<4;i++)
  for(j=0;j<4;j++)
  scanf("%d",&a[i][j]);
  
  scanf("%d",&ans2);
  
  for(i=0;i<4;i++)
  for(j=0;j<4;j++)
  scanf("%d",&b[i][j]);
  
  if(a[ans1-1][0]==b[ans2-1][0]||a[ans1-1][0]==b[ans2-1][1]||a[ans1-1][0]==b[ans2-1][2]||a[ans1-1][0]==b[ans2-1][3]){
  flag1=1;
  ans=a[ans1-1][0]; }
  
   if(a[ans1-1][1]==b[ans2-1][0]||a[ans1-1][1]==b[ans2-1][1]||a[ans1-1][1]==b[ans2-1][2]||a[ans1-1][1]==b[ans2-1][3]){
  flag2=1;
  ans=a[ans1-1][1]; }
            
   if(a[ans1-1][2]==b[ans2-1][0]||a[ans1-1][2]==b[ans2-1][1]||a[ans1-1][2]==b[ans2-1][2]||a[ans1-1][2]==b[ans2-1][3]){
  flag3=1;
  ans=a[ans1-1][2]; }
  
   if(a[ans1-1][3]==b[ans2-1][0]||a[ans1-1][3]==b[ans2-1][1]||a[ans1-1][3]==b[ans2-1][2]||a[ans1-1][3]==b[ans2-1][3]){
  flag4=1;
  ans=a[ans1-1][3]; }

 if( (flag1==1&&flag2==0&&flag3==0&&flag4==0) ||(flag2==1&&flag1==0&&flag3==0&&flag4==0)||(flag3==1&&flag2==0&&flag1==0&&flag4==0)||(flag4==1&&flag2==0&&flag3==0&&flag1==0) ){
 printf("Case #%d: %d\n",x++,ans);
 continue ;}
 
 if(flag1==0&&flag2==0&&flag3==0&&flag4==0)
 printf("Case #%d: Volunteer cheated!\n",x++);
 
 else
 printf("Case #%d: Bad magician!\n",x++);
           
 
   }
//system("Pause");
return 0;
}
