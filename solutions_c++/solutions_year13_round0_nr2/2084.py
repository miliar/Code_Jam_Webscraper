#include<stdio.h>
//<conio.h>
int main()
{
  int B[101][101]={100},a,t,k,m,n;
  int M[101][101];
  int rmax=0,rmin=0;
  scanf("%d",&t);
  for( k=0;k<t;k++)
  {
  int row[101]={0},col[101]={0},c=0;
  scanf("%d%d",&m,&n);
  for(int i=0;i<m;i++)
  {
  rmax=0;
  for(int j=0;j<n;j++)
  {
  scanf("%d",&a);
  M[i][j]=a;
  if(a>rmax)
  rmax=a;
  if(col[j]<M[i][j])
  col[j]=M[i][j];
   
  }
  row[i]=rmax;
  }
  for(int i=0;i<m;i++)
  // printf("%d\n",row[i]);
  for(int i=0;i<m;i++)
  {
  for(int j=0;j<n;j++)
  {
  B[i][j]=row[i];
  }
  }
  for(int i=0;i<n;i++)
  {
  for(int j=0;j<m;j++)
  {
  if(B[j][i]>col[i])
  B[j][i]=col[i];
  }
  }  
   
  for(int i=0;i<m;i++)
  {
  for(int j=0;j<n;j++)
  {
  if(B[i][j]==M[i][j])
  c++;  
  }
  }
  if(c==(m*n))
  printf("Case #%d: YES\n",k+1);
  else
  printf("Case #%d: NO\n",k+1);
   
}
  //lawnmower(M,m,n);
   
  //getch();
  return 0; 
 }
// void lawnmower(int M[][)
