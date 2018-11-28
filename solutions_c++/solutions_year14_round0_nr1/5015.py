#include <stdio.h>
#include <malloc.h>


void MagicTrick();


int main(void) {
	// your code goes here
	
	MagicTrick();
	
	return 0;
}


void MagicTrick()
{
	int Fans,Sans,i,j,t,T,e,c;

	
	int FA[4][4],SA[4][4];	
	
	scanf("%d",&T);
	t = 1;
	while(t<=T)
	{
	scanf("%d",&Fans);
	
	for(i=0;i<4;i++){
	for(j=0;j<4;j++){
		scanf("%d",&FA[i][j]);
		
	}
	}
	
	scanf("%d",&Sans);
	
	for(i=0;i<4;i++){
	for(j=0;j<4;j++){
		scanf("%d",&SA[i][j]);
		
	}

	}
	
	//trickBuster(*(FA+Fans-1),*(SA+Sans-1),t);
	//*************************************
	c=0;
    for(i=0;i<4;i++){
	for(j=0;j<4;j++){
	if(FA[Fans-1][i] == SA[Sans-1][j]){
		e = FA[Fans-1][i] ;
		c++;              
	}
	}
	}
	
switch(c)
{
	case 0:
	printf("Case #%d: Volunteer cheated!\n",t);
	break;
	
	case 1:
	printf("Case #%d: %d\n",t,e);
	break;
	
	default:
	printf("Case #%d: Bad magician!\n",t);
	break;
}
	
// end
	
	t++;
}
	
 }
