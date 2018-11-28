# include<iostream>
using namespace std;
int compute (int a, int b, int k) {
	int count = 0;
	for (int i = 0; i < a; i++)
		for (int j= 0; j< b; j++)
			if ((i & j ) < k)
				count++;
	return count;
}
int main () {
int a, b , k;
	int test;
	cin >> test;
	int i = 0;
	while (test --) {
		cin >> a>>b>>k;
		cout<<"Case #"<<++i <<":"<<" "<< compute(a,b,k)<<endl;;
	} 
	return 0;
}
