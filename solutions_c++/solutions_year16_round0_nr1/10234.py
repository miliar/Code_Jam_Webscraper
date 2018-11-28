#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;

int t,d,cero,count,y;
char num[1000000];
int ans;
bool is_cero,is_one,is_two,is_three,is_four,is_five,is_six,is_seven,is_eight,is_nine = false;
char another[1000000];

int findNmb(char x[], int n) { 
	
	int i = atoi(num);
	i*=n+1;
	if(count == 10){
		return i;
	}
	return findNmb(another,n+1); 			
}

int main(int argc, char *argv[]) {
	cin >> t;
	for(int i = 1; i <= t; i++) {
		cin >> num;
		cero = atoi(num);
		if(cero == 0) {
			cout << "Case #" << i << ": INSOMNIA" << endl;
		}
		else{
			is_cero = is_one=is_two=is_three=is_four=is_five=is_six=is_seven=is_eight=is_nine = false;
			ans =count= 0;
			y = 1;
			while(count != 10){
				ans= atoi(num);
				ans*=y;
				y++;
				itoa (ans,another,10);
				for(int z = 0; z < strlen(another); z++){
					d = another[z]-'0';
					switch(d){
						case 0:
							if(!is_cero){
								is_cero = true;
								count++;
							}
							break;
						case 1:
							if(!is_one){
								is_one = true;
								count++;
							}
							break;
						case 2:
							if(!is_two){
								is_two = true;
								count++;
							}
							break;
						case 3:
							if(!is_three){
								is_three = true;
								count++;
							}
							break;
						case 4:
							if(!is_four){
								is_four = true;
								count++;
							}
							break;
						case 5:
							if(!is_five){
								is_five = true;
								count++;
							} 
							break;
						case 6:
							if(!is_six){
								is_six = true;
								count++;
							}
							break;
						case 7:
							if(!is_seven){
								is_seven = true;
								count++;
							}
							break;
						case 8:
							if(!is_eight){
								is_eight = true;
								count++;
							}
							break;
						case 9:
							if(!is_nine){
								is_nine = true;
								count++;
							}
							break;
					}
					
				}
						
			}
			cout <<"Case #" << i <<": "<< ans<< endl;
		}	

	}
	return 0;
}
