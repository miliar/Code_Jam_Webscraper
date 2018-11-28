#include<stdio.h>
int main()
{ int t,i;
int n,j,k,l,m,min,x;
char str[100][101];
scanf("%d",&t);
for(i=1;i<=t;i++)
{ scanf("%d",&n);
for(x=0;x<n;x++)
scanf("%s",str[x]);
printf("Case #%d: ",i);
min=0;
for(j=k=0;str[0][j]&&str[1][k];)
{ for(l=j+1;str[0][l]&&str[0][l]==str[0][j];l++);
  for(m=k+1;str[1][m]&&str[1][m]==str[1][k];m++);
  if(str[0][j]!=str[1][k]||(str[0][l]=='\0'&&str[1][m])||(str[0][l]&&str[1][m]=='\0'))
  { printf("Fegla Won\n");
    break;
  }
  min+=(l-j>m-k)?l-j-m+k:m-k-l+j;
  j=l;
  k=m;
}
if(!str[0][j]&&!str[1][k])
printf("%d\n",min);  
}
return 0;
}
