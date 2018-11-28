#include<stdio.h>
#include<math.h>
int chkpal(int n)
{
int n1,rev=0,rem;
n1 = n;
while (n > 0){
rem = n % 10;
rev = rev * 10 + rem;
n = n / 10; }
if (n1 == rev){
return 1;}
else{
return 0;}
}
int main()
{
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        int answer=0,lb,ub,lo;
        float sq;
	scanf("%d %d",&lb,&ub);
        for(int i=lb;i<=ub;i++)
        {
	        sq = sqrt(i);lo=sq;
	        if(sq==lo)
	        {
			if((chkpal(i)==1)&&(chkpal(lo)==1)){answer++;}
	        }
        }
        printf("Case #%d: %d\n",cas,answer);       
    }
}