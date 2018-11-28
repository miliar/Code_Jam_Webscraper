#include <iostream>
#include<string>
#include<algorithm>

using namespace std;

int main(){

	FILE *read=fopen("B.in","r");
	FILE *write=fopen("B_answer.txt","w");

	int t;
	fscanf(read,"%d",&t);

	for(int i=0;i<t;i++){

		char pancake[101];
		fscanf(read,"%s",&pancake);

		char current=pancake[0];
		int count=1;
		for(int j=1;j<strlen(pancake);j++){
			if(pancake[j]!=current){
				count++;
				current=pancake[j];
			}
		}

		if(pancake[strlen(pancake)-1]=='+')count--;

		fprintf(write,"Case #%d: %d\n",i+1,count);
		

	}

	fclose(read);
	fclose(write);


	return 0;
}