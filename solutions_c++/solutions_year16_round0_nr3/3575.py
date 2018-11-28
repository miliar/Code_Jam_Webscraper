#include<iostream>
#include<math.h>
using namespace std;
//header file from :  http://askubuntu.com/questions/481807/how-to-install-g-in-ubuntu-14-04

unsigned long primechecker(unsigned long num){
	for (unsigned long i = 2; i < sqrt(num); i++) {
		if(num%i == 0)
			return i;
	}
	return 0;

}
int main(int argc, char *argv[])
{
    unsigned long T;
	cin>>T;
	unsigned long N;
	cin>>N;
	unsigned long J;
	cin>>J;
	unsigned long a = (unsigned long)(pow(2,N-1) + 1);
	unsigned long b = (unsigned long)(pow(2,N) - 1);
	//cout<<a;
	//cout<<" "<<b<<endl;
	unsigned long n1 = 0,counter = 0,r = 0;
	unsigned long x = 0;
	unsigned long array[9] = {0,0,0,0,0,0,0,0};
	unsigned long prime[9] = {0,0,0,0,0,0,0,0};
	unsigned long trial = 0;
	cout<<"Case #1:"<<endl;

	for (unsigned long i = a; i <= b; i+=2) {
		if(n1 == J)
			break;
		array[0] = 0;
		array[1] = 0;
		array[2] = 0;
		array[3] = 0;
		array[4] = 0;
		array[5] = 0;
		array[6] = 0;
		array[7] = 0;
		array[8] = 0;
		x = i;
		counter = -1;
		while(x>0) {
			++counter;
			r = x%2;
			array[0] = array[0] + (unsigned long)(r*pow(2,counter));
			array[1] = array[1] + (unsigned long)(r*pow(3,counter));
			array[2] = array[2] + (unsigned long)(r*pow(4,counter));
			array[3] = array[3] + (unsigned long)(r*pow(5,counter));
			array[4] = array[4] + (unsigned long)(r*pow(6,counter));
			array[5] = array[5] + (unsigned long)(r*pow(7,counter));
			array[6] = array[6] + (unsigned long)(r*pow(8,counter));
			array[7] = array[7] + (unsigned long)(r*pow(9,counter));
			array[8] = array[8] + (unsigned long)(r*pow(10,counter));
			x = x/2;			
		}
		trial = primechecker(array[0]); 
		if(trial == 0)
			continue;
		else
			prime[0] = trial;
		trial = primechecker(array[1]); 
		if(trial == 0)
			continue;
		else
			prime[1] = trial;
		trial = primechecker(array[2]); 
		if(trial == 0)
			continue;
		else
			prime[2] = trial;
		trial = primechecker(array[3]); 
		if(trial == 0)
			continue;
		else
			prime[3] = trial;
		trial = primechecker(array[4]); 
		if(trial == 0)
			continue;
		else
			prime[4] = trial;
		trial = primechecker(array[5]); 
		if(trial == 0)
			continue;
		else
			prime[5] = trial;
		trial = primechecker(array[6]); 
		if(trial == 0)
			continue;
		else
			prime[6] = trial;
		trial = primechecker(array[7]); 
		if(trial == 0)
			continue;
		else
			prime[7] = trial;
		trial = primechecker(array[8]); 
		if(trial == 0)
			continue;
		else{
			prime[8] = trial;
			++n1;
			//cout<<"*"<<i<<"\n";
			cout<<array[8]<<" "<<prime[0]<<" "<<prime[1]<<" "<<prime[2]<<" "<<prime[3]<<" "<<prime[4]<<" "<<prime[5]<<" "<<prime[6]<<" "<<prime[7]<<" "<<prime[8]<<endl;
 		}
			
	}

	
}
