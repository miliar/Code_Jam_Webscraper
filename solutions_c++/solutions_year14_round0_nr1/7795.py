#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int num[20];

int main()
{
    int T;
    scanf("%d",&T);
    int t=1;
 
    while(t<=T){
	int a,tmp;
	memset(num,0,sizeof(num));
	scanf("%d",&a);
	for(int i=0;i<16;i++){
	    scanf("%d",&tmp);
	    if(i/4+1==a)
		num[tmp]++;
	}
	scanf("%d",&a);
	for(int i=0;i<16;i++){
	    scanf("%d",&tmp);
	    if(i/4+1==a)
		num[tmp]++;
	}
	int ans=-1;
	for(int i=1;i<=16;i++){
	    if(num[i]==2)
		ans=(ans<0)?i:99;
	}
	printf("Case #%d: ",t++);
	if(ans<0)
	    puts("Volunteer cheated!");
	else if(ans>90)
	    puts("Bad magician!");
	else
	    printf("%d\n",ans);
    }
    return 0;
}

