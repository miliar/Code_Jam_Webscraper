#include<iostream>

using namespace std;

void update(long long x, int* arr){
	while(x>0){
		arr[x%10] = 1;
		x/=10;
	}
}

bool check(int*x){
	if(x[0] == 1 && x[1] == 1 && x[2] == 1 && x[3] == 1 && x[4] == 1 && x[5] == 1 && x[6] == 1 && x[7] == 1 && x[8] == 1 && x[9] == 1) return true;
	return false;
}

int main(){
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		long long n;
		cin>>n;
		int x[10] = {0};
		cout<<"Case #"<<i<<": ";
		for(long long mul=1; mul<1000000; mul++){
			update(n*mul, x);
			if(check(x)){
				cout<<mul*n<<endl;
				break;
			}
		}
		if(!check(x)){
			cout<<"INSOMNIA\n";
		}
	}
	
	return 0;
}
