#include <cstdio>
#include <cmath>
#include <fstream>
int t,a,b,casee;

FILE *fout =fopen("output.out","w");


bool check(int i) {
     int k=sqrt(i);
     int soll,solk;
     if (i<10) soll=1;
     else if (i<100) soll=10;
     else if (i<1000) soll=100;
     else soll=1000; 
     if (k<10) solk=1;
     else if(k<100) solk=10;
     else if (k<1000) solk=100;
     else solk=1000;
     int p=k,c=solk,rez=0;
     while(p!=0) {
                 rez+=c*(p%10);
                 p/=10;
                 c/=10;}
     if (rez!=k) return 0;
     p=i;
     rez=0;
     c=soll;
     while(p!=0) {
                 rez+=c*(p%10);
                 p/=10;
                 c/=10;}
     if (rez!=i) return 0;
     return 1;}


void solve() {
     casee++;
     int sol=0;
     scanf("%d%d",&a,&b);
     for (int i=a;i<=b;i++) {
         int k=sqrt(i);
         if (k*k==i && check(i)==1) {sol++;}}
     fprintf(fout,"Case #%d: %d\n",casee,sol);}





int main() {
    scanf("%d",&t);
    while(t--) solve();
    return 0;}
