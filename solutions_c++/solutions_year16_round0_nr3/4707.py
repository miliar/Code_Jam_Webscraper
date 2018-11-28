#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;


int divs[10];
int count;

bool prime(long long int num){
    int lim = sqrt(num);
    for(int i=2;i<=lim;i++)
	if(num % i == 0){
	    divs[count++] = i;
	    return 0;
	}
    return 1;
}

long long int base(int num, int b){
    long long int res = 0;
    long long int m = 1;
    while(num){
	res += (num & 1) * m;
	num >>=1;
	m *= b;
    }
    return res;
}

bool good(int k){
    count = 0;
    for(int i=2;i<=10;i++)
	if(prime(base(k,i))) return 0;
    return 1;
}

void print(){
    for(int i=0;i<9;i++)
	cout << " " << divs[i];
    cout << endl;
}

void binprint(int num){
    if(!num) return;
    binprint(num >> 1);
    cout << (num & 1);
}

int main(){
    int T;
    cin >> T;
    for(int i=1;i<=T;i++){
	int N,J;
	cin >> N >> J;
	int num = 1 + (1 << (N-1));
	int count = 0;
	cout << "Case #1:" << endl;
	while(count < J){
	    if(good(num)) {
		binprint(num);
		print();
		count++;
	    }
	    num+=2;
	}
    }
    return 0;
}

