#include<stdio.h>

#define E 69
#define Z 90
#define R 82
#define O 79
#define N 78
#define W 87
#define F 70
#define U 85
#define I 73
#define V 86
#define S 83
#define X 88
#define G 71
#define H 72
#define T 84

int main(){
	
	char str[2001];
	int t , i , j , index;
	scanf("%d",&t);
	for(i=1; i<=t; i++){
		
		scanf("%s",str);

		int arr[91] = {0};
	
		for(j=0; str[j]!='\0'; j++){
		   arr[str[j]]++;
		}
	
	    int ans[10]={0};	
		
		//checking for zero
			ans[0] = arr['Z'];
		   while(arr['Z']!=0){
		   	  arr['Z']--;
		   	  arr['E']--;
		   	  arr['R']--;
		   	  arr['O']--;
		   }	
	
		
		//checking for two

			ans[2] = arr['W'];
			while(arr['W']!=0){
				arr['T']--;
				arr['W']--;
				arr['O']--;
			}
	
		
	    //checking for four

			ans[4] = arr['U'];
			while(arr['U']!=0){
				arr['F']--;
				arr['O']--;
				arr['U']--;
				arr['R']--;
			}

		 //checking for eight

			ans[8] = arr['G'];
			while(arr['G']!=0){
				arr['E']--;
				arr['I']--;
				arr['G']--;
				arr['H']--;
				arr['T']--;
			}
			
		 //checking for six
			ans[6] = arr['X'];
			while(arr['X']!=0){
				arr['S']--;
				arr['I']--;
				arr['X']--;
			}
			
		 //checking for three
	
			ans[3] = arr['T'];
			while(arr['T']!=0){
				arr['T']--;
				arr['H']--;
				arr['R']--;
				arr['E']--;
				arr['E']--;
			}
		
		 //checking for five
	
			ans[5] = arr['F'];
			while(arr['F']!=0){
				arr['F']--;
				arr['I']--;
				arr['V']--;
				arr['E']--;
			}
		
		 //checking for seven

			ans[7] = arr['V'];
			while(arr['V']!=0){
				arr['S']--;
				arr['E']--;
				arr['V']--;
				arr['E']--;
				arr['N']--;
			}
		
		
	  //checking for nine
	
			ans[9] = arr['I'];
			while(arr['I']!=0){
				arr['N']--;
				arr['I']--;
				arr['N']--;
				arr['E']--;
			}
		//checking for one
		   ans[1] = arr['O'];
		   while(arr['O']!=0){
		   	arr['O']--;
		   	arr['N']--;
		   	arr['E']--;
		   }
		
		printf("CASE #%d: ",i);
		
		for(int k=0; k<10; k++){
			while(ans[k]){
				printf("%d",k);
				ans[k]--;
			}
		}
		printf("\n");
	}
	return 0;
}
