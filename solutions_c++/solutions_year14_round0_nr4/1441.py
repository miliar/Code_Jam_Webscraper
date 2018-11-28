#include<cstdio>
#include<stdlib.h>
#include<algorithm>
#include<memory.h>
using namespace std;

FILE *fin;
FILE *fout;

int i,k,n,t,p1,p2,ans1,ans2;
double a[1000],b[1000];

int main(){
  fin=fopen("D-large.in","r");
  fout=fopen("output.txt","w+");
  fscanf(fin,"%d",&t);
  for (k=0;k<t;k++){
    memset(a,0,sizeof(a));
    memset(b,0,sizeof(b));
    fscanf(fin,"%d",&n);
    for (i=0;i<n;i++){
      fscanf(fin,"%lf",&a[i]);
    }
    for (i=0;i<n;i++){
      fscanf(fin,"%lf",&b[i]);
    }
    sort(a,a+n);
    sort(b,b+n);
    ans1=0;ans2=n;
    p1=n-1;p2=n-1;
    while (p2>=0){
      while (a[p1]<b[p2] & p2>=0) p2--;
      if (p2>=0 & a[p1]>b[p2]){
        ans1++;
        p1--;
        p2--;  
      }
    }
    p1=0;p2=0;
    while (p2<n){
      while (a[p1]>b[p2] & p2<n) p2++;
      if (p2<n & a[p1]<b[p2]){
        ans2--;
        p1++;
        p2++; 
      }
    }
    fprintf(fout,"Case #%d: %d %d\n",k+1,ans1,ans2);
  }
  fclose(fin);
  fclose(fout);
  system("pause");
  return 0;
}
