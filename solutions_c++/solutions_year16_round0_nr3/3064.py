#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>
#include <cmath>
// #include <time.h>
using namespace std;

unsigned long judge(int *coin,int digit, int base){
	unsigned long num = 0;
	for (int i = 0;i<digit;i++)
		num += coin[i]*pow(base,i);
	for (unsigned long  i = 2; i < 3000 ;i++ )
		if (num%i == 0){
			return i;
		}
	return 0;
}


int main(){
	ifstream ii("C-small-attempt.in");
	ofstream oo("oss.out");
	int T;
	ii >> T;
	int digit;
	int num;

	for (int i = 0;i < T;i++){
		ii >> digit;
		ii >> num;
	}
	
	int *coin = new int [digit];
	unsigned long *sum = new unsigned long [num];
	int i;
	coin[0] = 1;
	coin[digit-1] = 1; 
	for (i = 1;i<digit-1;i++)
		coin[i] = 0;
	oo << "Case #1:" << endl;
	// srand (time(NULL));

	int count = 0;
		// int flip = rand()%(digit-2)+1;
		
		// if (coin[flip])
		// 	coin[flip] = 0;
		// else coin[flip] = 1;

		for (int x = 1;x<digit-1;x++){
			coin[x] = 1;
			for (int y = 1;y < x;y++){
				coin[y] = 1;
				for (int z = 1;z<y;z++){
					if (count == num)
						exit(0);
					unsigned long divd[9] = {0,0,0,0,0,0,0,0,0};
					coin[z] = 1;
					int j;
					for (j =2;j<11;j++){
						divd[j-2] = judge(coin,digit,j);
						if (divd[j-2] == 0)
							break;
					}
					if (j == 11){
						unsigned long temp = 0;
						int i;
						for (i = 0;i<digit;i++){
							temp += coin[i] * pow(10,i);
						}
						for (i = 0;i<count;i++)
							if (temp == sum[i]){
								// cout << "same\n" << count << endl;
								break;
							}
						if (i == count){
							count++;
							sum[count] = temp;
							oo << temp << " ";	
							for (int i = 0;i<8;i++)
								oo << divd[i] << " ";
							oo << divd[8] << endl;
						}
					}
					coin[z] = 0;
				}
				coin[y] = 0;
			}
			coin[x]=0;
		}

}

