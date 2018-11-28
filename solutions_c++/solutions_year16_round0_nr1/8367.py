#include<iostream>

using namespace std;

int main(){
int T;
cin>>T;


for (int t = 0; t < T; t++){
int A[10];
for ( int i =0; i<10; i++)
	A[i] = 0;

long int num,digit = 0;
int rem = 0,count = 2;
bool sleep = false;
	cin>>num;
	if(num == 0)
		cout<<"Case #"<<t+1<<": INSOMNIA\n";	
	else{
	digit = num;
	while(1){
		
		while(digit > 0){
			rem = digit%10;
			//cout<<"Rem : "<<rem<<", digit: "<<digit<<"\n";
			A[rem] = 1;
			digit = digit/10;

		}

	if( A[0] == 1 && A[1] == 1 && A[2] == 1 && A[3] == 1 && A[4] == 1 && A[5] == 1 && A[6] == 1 && A[7] == 1 && A[8] == 1 && A[9] == 1 )
	{sleep = true;
	cout<<"Case #"<<t+1<<": "<<num * (count -1)<<"\n";
	break;}

	digit = num * count;
	count++;
	}
	}

}


}
