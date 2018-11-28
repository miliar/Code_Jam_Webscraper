
#include <iostream>
#include <stdio.h>
int countingSheep(int n);

int main(int argc, char **argv)
{
	int testCase,n;
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&testCase);
	for(int i=0;i<testCase;i++){
		scanf("%d",&n);
		if(n==0)
			printf("Case #%d: INSOMNIA\n",i+1);
		else{
			int result = countingSheep(n);
			printf("Case #%d: %d\n", i+1,result);
		}
	}
	return 0;
}
int countingSheep(int n){
	
	int arr[10]={0};
	int i=2;
	int p=0;
	int temp_n = n;
	int oldN = n;
	int currentN = n;
//	printf("TEMP N == %d",temp_n);
	
	while(true){
		n=temp_n;
		/*printf("#### IN LOOP %d\n",n);
		printf("TEMP N == %d",temp_n);
		printf("Current N == %d",currentN);
		printf("OLD N == %d",oldN); */
		currentN = temp_n;
		while(n>0){
			p=n%10;
			arr[p]++;
			n=n/10;
		}
		
		int countDigit=0;
		for(int j=0;j<10;j++)
		{
			if(arr[j]>0)
				countDigit=countDigit+1;
		//	printf("######## COUNT DIGIT ### %d\n",countDigit);
		}
		
		if(countDigit>=10)
			break;
		temp_n=oldN*i;
		i++;
	}
	return currentN;
}

