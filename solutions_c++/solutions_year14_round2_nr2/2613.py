/*	Google Code Jam - 2014 - Round 1B
 */

#include <iostream>
#include <string>

using namespace std;

void process(unsigned long A, unsigned long B, unsigned long K)
{
	unsigned long i, j, k;
	unsigned long count=0;
	for (i=0 ; i<A ; i++) 
		for (j=0 ; j<B ; j++) {
			if ((i & j) < K)
				count++;
		}
	
	cout<<count<<endl;
	return;
}

int main()
{
	unsigned long n, i, j, k, A, B, K;
	int a, b;
	
	cin>>n;
	for (i=1 ; i<=n ; i++) {
		cin>>A>>B>>K;
		cout<<"Case #"<<i<<": ";
		process(A, B, K);
	}
	return 0;
}
