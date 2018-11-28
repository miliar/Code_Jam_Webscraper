#include<stdio.h>
#include<math.h>
int palindrome(int number);
int main(){

int t,a,b,count,i,test=1;

scanf("%d",&t);


while(t--){
count=0;
scanf("%d %d",&a,&b);

for(i=a;i<=b;i++){

if(palindrome(i)){

if( ( ceil((int)sqrt(i))-sqrt(i) == 0.0f ) && palindrome((int)sqrt(i)) ){
count++;
}

}
}
printf("Case #%d: %d\n",test,count);
test++;
}
return 0;
}

int palindrome(int number){

int sum=0,temp=number;

while(temp!=0){
sum=sum*10+temp%10;
temp=temp/10;
}

if(sum==number)
return 1;

return 0;
}
