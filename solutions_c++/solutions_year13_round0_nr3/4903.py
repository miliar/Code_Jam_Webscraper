#include<iostream>
#include<cstdio>
using namespace std;
int arr[23];
int oneDigit(int num)
{
  return (num >= 0 && num < 10);

}
 bool isPalUtil(int num, int* dupNum)
{
    if (oneDigit(num))
        return (num == (*dupNum) % 10);
    if (!isPalUtil(num/10, dupNum))
        return false;
    *dupNum /= 10;
    return (num % 10 == (*dupNum) % 10);
}
int isPal(int num)
{
    int *dupNum = new int(num);
    return isPalUtil(num, dupNum);
}
int main(){
int t;
scanf("%d",&t);
int i,j,cp=0;
for(i=1;i<=10000000;i++){
 if(isPal(i)){
	j=i*i;
	if(isPal(j))
	{arr[cp]=j;
	cp++;
	//printf("%d ",arr[cp-1]);
	}
}
}
//printf("%d",cp);
j=1;
while(t--){
int m,n,count=0;
scanf("%d%d",&m,&n);
for(i=0;i<cp;i++)
{if(arr[i]>n)
break;
if(arr[i]>=m)
 count++;
}
printf("Case #%d: %d\n",j,count);
j++;
}
return 0;
}
