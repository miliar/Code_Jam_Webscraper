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
int n,i,j,warn=0,dwarn=0;
double naomi[2000],ken[2000],naomi1[2000],ken1[2000];

scanf("%d",&n);

for(i=0;i<n;i++){
scanf("%lf",&naomi[i]);
naomi1[i]=naomi[i];}

for(i=0;i<n;i++){
scanf("%lf",&ken[i]);
ken1[i]=ken[i];}

sort(naomi,naomi+n);
sort(ken,ken+n);
sort(naomi1,naomi1+n);
sort(ken1,ken1+n);

 for(i=0;i<n;i++)
 for(j=0;j<n;j++){
 
   if(ken[j]>naomi[i]){
   naomi[i]=-0.9;
   ken[j]=-0.9;
   break;
   }
    
}
 for(i=0;i<n;i++)    // naomi wins if playing war
  if(naomi[i]!=(-0.9))
  warn++;
  
  
  for(i=0;i<n;i++)
  for(j=0;j<n;j++){

    if(naomi1[j]>ken1[i]){
    dwarn++; 
    naomi1[j]=-0.9;
    ken1[i]=-0.9;
    break ;
    }  
  
  }
 printf("Case #%d: %d %d\n",x++,dwarn,warn);
 
 

           }
//system("Pause");
return 0;
}
