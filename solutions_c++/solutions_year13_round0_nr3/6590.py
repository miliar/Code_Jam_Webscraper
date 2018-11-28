#include <iostream>
#include <math.h>

int ispfsquare(int num){
	if(num==1){
	return num;}
	for(int i=1;i<num;i++){
	if(num==i*i)
	return i;}
	return 0;
}
int palindrome(int num){
	int dig,rev,n;
 n = num;
 rev = 0;
 while (num > 0)
 {
      dig = num % 10;
      rev = rev * 10 + dig;
      num = num / 10;
 }
 if(n==rev){
 return 1;
 }
 else return 0;
}

void main(){
int times,limit[2],amount=0;
do{
scanf("%d",&times);
	fflush(stdin);
}while(times<1 || times > 100);
//main process
for(int i=1;i<=times;i++){
	amount=0;
	do{
	scanf("%d %d",&limit[0],&limit[1]);
	fflush(stdin);
	}while(limit[0]<0||limit[0]>limit[1]||limit[0]>1000||limit[1]<1||limit[1]>1000);

	for(int a=limit[0];a<=limit[1];a++){
		if(palindrome(a)==1){
			if(ispfsquare(a)!=0){
				if(palindrome(ispfsquare(a))==1){
					amount++;
				}
		}
	}
	}
	printf("Case #%d: %d",i,amount);
}
getchar();

}