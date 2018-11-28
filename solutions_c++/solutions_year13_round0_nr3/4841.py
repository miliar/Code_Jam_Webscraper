#include <iostream>
#include <vector>

using namespace std;

typedef unsigned long long bg;

vector<bg> sqp{1,4,9,121,484,10201,12321,14641,40804,44944,
    1002001,1234321,4008004,100020001,102030201,
    104060401,121242121,123454321,125686521,400080004,
    404090404,10000200001,10221412201,12102420121,
    12345654321,40000800004};

bg A, B;

void read(){
	cin >> A >> B;
}

bg determine(){
	auto a = lower_bound(sqp.begin(), sqp.end(), A);
	if(*a < A) a++;
	auto b = lower_bound(a, sqp.end(), B);
	if(*b > B) b--;
	return b-a+1;
}

int main(int argc, char** argv){
	int T;
	cin >> T;
	for(int n=1;n<=T;n++){
		read();
		cout<<"Case #"<< n <<": " << determine() << endl;
	}
	return 0;
}