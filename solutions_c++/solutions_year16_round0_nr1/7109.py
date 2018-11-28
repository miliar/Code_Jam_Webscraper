#include <iostream>

using namespace std;

int solve(int);

int main(int argc, char const *argv[])
{
	int n;
	long long int t[100];
	long long int r[100];
	
	cin>>n;
	for(int i=0;i<n;i++) {
		cin>>t[i];
		if(t[i]) r[i] = solve(t[i]);
	}

	for(int i=0;i<n;i++) {
		if(t[i] == 0) cout<<"case #"<<i+1<<": "<<"INSOMNIA"<<endl;
		else
		cout<<"case #"<<i+1<<": "<<r[i]<<endl;
	}

	/*	
	for(int i=1;i<200;i++) {
		cout<<i<<" "<<solve(i)<<endl;
	}
	*/
	

	return 0;

}

int check(int *d) {
	for(int i=0;i<10;i++)
		if(!d[i]) return 0;
	return 1;
}

int solve(int x) {

	int i; long long int n=1; long long int y;
	int digits[10];
	for(i=0;i<10;i++) digits[i] = 0;
	do {
		y = x*n++;
		int temp = y;
		do {
			digits[temp%10] = 1;
			temp /= 10;
		} while(temp);
	} while(!check(digits));
	return y;
}