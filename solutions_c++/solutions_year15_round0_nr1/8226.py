#include<stdio.h>
#include<fstream>
#include<iostream>
using namespace std;
void main(){

	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small.out", "w", stdout);

	int test;
	cin >> test;
	int count = 1;
	int stress;
	char person[1005] = {0};
	int invite=0;
	int value = 0,value1=0;
	bool flag;
	while (count<=test){
		invite = 0;
		value = 0;
		cin >> stress >>person; 

		for (int i = 0; person[i] != '\0'; i++){
			flag = false;
			value1 = person[i]-'0';
			value += value1 ;
			//value1 = person[i + 1] - '0';
			if (person[i] == '0' && value<=i){
				invite=invite+1;
				flag = true;
				
			}
			if (flag == true)
			{
				value++;

			}
		}
		cout << "Case #" << count << ": " << invite<<"\n";
		
		
		//cout << person<<"\n";


		count++;
	}




}