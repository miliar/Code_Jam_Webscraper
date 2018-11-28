#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>

using namespace std;

FILE *in = fopen("C-small.in","r");
FILE *out = fopen("C-small.out","w");

long long pow[16];
long long fands[10000];
int nfands=0;

int checkPalindrome(long long n, int d){
    for(int i=0;i<d/2;i++)
            if(n%pow[i+1]!=n/pow[d-i-1]) return 0;
    return 1;
}

int numDigits(long long n){
    for(int i=0;i<15;i++)
            if(pow[i]>n)
                        return i;
}

void generatePalindromes(int n, int i, int t){
     if(i<t/2) {
               long long p = (long long)n*(long long)n;
               //printf("%d %I64d %d\n",n,p,numDigits(p));
               if(checkPalindrome(p,numDigits(p))) {
                     printf("%d\n",n);
                     fands[nfands++]=p;
               }
               return;
               }
     for(int j=1;j<10;j++)
             generatePalindromes(n+pow[i]*j+((i!=t/2||(i==t/2&&t%2==0))?pow[t-i-1]*j:0),i-1,t);
}

main()
{
       int n,r;
       long long a,b;
       pow[0]=1ll;
       for(int i=1;i<16;i++) {
               pow[i] = 10ll*pow[i-1];
               printf("%I64d\n",pow[i]);
       }
       fscanf(in,"%d",&n);
       for(int i=0;i<=7;i++) {
               generatePalindromes(0,i-1,i);
               //system("PAUSE");
       }
       for(int i=0;i<n;i++){
               r=0;
               fscanf(in,"%I64d %I64d",&a,&b);
               for(int j=0;j<nfands;j++) {
                       printf("%I64d %I64d %I64d\n",a,b,fands[j]);
                       if(fands[j]>=a&&fands[j]<=b)
                                                   r++;
               }
               fprintf(out,"Case #%d: %d\n",i+1,r);
       }
       fclose(in);
       fclose(out);
       system("PAUSE");
}
