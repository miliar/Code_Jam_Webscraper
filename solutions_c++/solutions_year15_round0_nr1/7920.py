#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
int test;
scanf("%d",&test);
long long int a[1010] , smax ;
char c;
long long int psum = 0 , ans = 0;
for(int o=1;o<=test;o++){
psum = 0;
ans  = 0;
scanf("%lld ",&smax);
for(int i=0;i<=smax;i++)
{
scanf("%c",&c);
a[i] = c - '0';
}
psum = a[0];
for(int i=1;i<=smax;i++){
if(psum < i){
	//printf("%d %d\n",psum , i );
	ans = ans + (i-psum);
	psum = i;
	psum += a[i];

}
else
	psum += a[i];
}
printf("Case #%d: %lld\n",o , ans );
}
return 0;	
}