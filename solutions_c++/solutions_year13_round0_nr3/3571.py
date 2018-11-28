#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

int caseNum;
unsigned long long mmin;
unsigned long long mmax;
long long value[10000];
int list_max;

int main(){
	int print_num;
	cin >> caseNum;

	list_max = 0;
	memset(value, 0, sizeof(int)*10000);
	unsigned long long for_max = 1;
	for(int i = 0; i < 14; i++){
		for_max = for_max * 10;
	}

	int count = 0;
	int temp = 1;
	long long temp1 = 0;
	long long temp2 = 0;
	long long temp3 = 1;
	int temp4 = 0;
	bool is;
	while(temp1 <= for_max){
		temp3 = 1;
		temp2 = 0;
		is = false;
		while(1){
			temp4 = (int)(temp%(temp3*10))/temp3;
			if(temp4 == 0){
				if(temp2 == temp){
					is = true;
				}
				break;
			}
			temp2 = (temp2*10) + temp4;
			temp3 *= 10;
		}

		if(is){
			temp3 = 1;
			temp2 = 0;
			temp1 = temp * temp;
			while(1){
				temp4 = (int)(temp1%(temp3*10))/temp3;
				if(temp4 == 0){
					if(temp2 == temp1){
						value[count] = temp2;
						count++;
					}
					break;
				}
				temp2 = (temp2*10) + temp4;
				temp3 *= 10;
			}
		}
		++temp;
	}

	for(int i = 1; i <= caseNum; ++i){
		count = 0;
		scanf("%llu %llu", &mmin, &mmax);
		for(int k = 0; k < 10000; k++){
			if(mmin > value[k]) continue;
			if(mmax < value[k]) break;
			count++;
		}
		printf("Case #%d: %d\n", i, count);
	}


	return 0;
}