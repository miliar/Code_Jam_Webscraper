#include<stdio.h>      
#include<stdlib.h>      
#include<math.h>  
#include <iostream>
#include <string>
using namespace std;
	
typedef struct name
{
   char name[100]; // 100 character array
}name;


int main() { 
	
	int T,i,j,k,number,n,m,N,M;
	scanf("%d",&T);
	
	name strings[100];

	char temp;
	
	for (i=1; i<=T; i++)
	{
		scanf("%d", &N);
		int length[N];
		for (j=0;j<N;j++){
			scanf("%s",strings[j].name);
			length[j] = (int) strlen(strings[j].name);
		}
		
		int result = 0;
		int iter_strings[N]; //current 
		for (j=0;j<N;j++) iter_strings[j]=0;
		int count[N];
		int flag=0;
		int flag_stop=0;
		while (true){
			temp = strings[0].name[iter_strings[0]]; 
			int iter[N];
			for (j=0; j< N ;j++) iter[j]=iter_strings[j];
			for (j=0; j<N;j++) {
				while ((iter[j]<length[j]) && (strings[j].name[iter[j]]==temp)) iter[j] ++; 
				count[j] = iter[j] - iter_strings[j]; //how many letters;
			}
			for (j=0;j<N;j++) {
				if (count[j]==0) flag = -1;
			}
			if (flag == -1) break;
			int sum=0;
			for (j=0;j<N;j++){
				sum= sum + count[j];
			}
			int average = round((1.0*sum)/N);
			printf("anerage = %d\n", average);
			for (j=0;j<N;j++) result = result + (std::abs(count[j]-average));
			int count_end=0;
			for (j=0;j<N;j++){
				if (iter[j]==length[j]) count_end++;
			}
			if (count_end == N) break;
			if (count_end>0){flag = -1; break;}
			for (j=0;j<N;j++) iter_strings[j]=iter[j];
		}
	
		printf("Case #%d: ",i);
		if (flag == -1) printf("Fegla Won\n");
		else printf("%d\n",result);
	}
	
	return 0;
}

