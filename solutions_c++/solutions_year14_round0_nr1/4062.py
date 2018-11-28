#include<stdio.h>

int main(){

int n=1, input;
scanf("%d", &input);
int i, j, cardno, flag, ch1, ch2, ans1[4], ans2[4], arr1[4][4], arr2[4][4];

while(n<=input){
    scanf("%d", &ch1);
    for(i=0; i<4; i++)
	for(j=0; j<4; j++)
	    scanf("%d", &arr1[i][j]);
    scanf("%d", &ch2);
    for(i=0; i<4; i++)
	for(j=0; j<4; j++)
	    scanf("%d", &arr2[i][j]);
    for(i=0; i<4; i++)
	ans1[i]=arr1[ch1-1][i];
	
    for(i=0; i<4; i++)
	ans2[i]=arr2[ch2-1][i];
    for(i=0, flag=0; i<4; i++)
	for(j=0; j<4; j++)
	    if(ans1[i]==ans2[j])
		{flag++; cardno=i;}
    if(flag==0)
	printf("Case #%d%s%s", n, ": ", "Volunteer cheated!");
    if(flag>1)
 	printf("Case #%d%s%s", n, ": ", "Bad magician!");
    if(flag==1)
	printf("Case #%d%s%d", n, ": ", ans1[cardno]);
n++;   printf("\n"); 
}
    return 0;

   
}
