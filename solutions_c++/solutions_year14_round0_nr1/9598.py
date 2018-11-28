#include <stdio.h>

int main(int argc,char *argv[]){
int t,a1,a2;
long long int a=1;
int arr1[4][4],arr2[4][4];
long long int ans;
FILE *fpr = fopen(argv[1],"r");
fscanf(fpr,"%d",&t);
int p=0;
while(p<t)
{ int pos,count=0;
  fscanf(fpr,"%d",&a1);
  for(int i=0; i<4; ++i)
   for(int j=0; j<4; ++j)
    fscanf(fpr,"%d",&arr1[i][j]);
    
  fscanf(fpr,"%d",&a2);
  for(int i=0; i<4; ++i)
   for(int j=0; j<4; ++j)
    fscanf(fpr,"%d",&arr2[i][j]);
    
  for(int i=0; i<4;++i)
   for(int j=0; j<4; ++j)
   { ans = (a<<arr1[a1-1][i]) & (a<<arr2[a2-1][j]);
     if(ans)
      {count++;
       pos=i;
      }
   }
   
   if(count==0)
     printf("Case #%d: Volunteer cheated!\n",p+1);
   else if(count==1)
     printf("Case #%d: %d\n",p+1,arr1[a1-1][pos]);
   else printf("Case #%d: Bad magician!\n",p+1);
   
  p++;
}
fclose(fpr);
return 0;
}
