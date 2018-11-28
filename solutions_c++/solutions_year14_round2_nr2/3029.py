#include <iostream>
#include<stdio.h>
using namespace std;
int main(){
long long int t,a,b,k,i,j,cases=1,noc;
scanf("%lld",&t);
while (t--) {
noc=0;
scanf("%lld %lld %lld",&a,&b,&k);
for (i =0; i<a; i++) {
for (j =0 ; j<b; j++) {
if ((i&j)<k) {
noc++;
}
}
}
printf("Case #%lld: %lld\n",cases,noc);
cases++;
}
return 0;
}