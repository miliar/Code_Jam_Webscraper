#include <iostream>
#include <vector>
using namespace std;

bool isConsonant(char c){
	return (!(c=='a' || c=='e' || c=='i' || c=='o' || c=='u'));
}

int main() {
	int N,n,x;
	string s;

	cin >> N;
	for (int I=0;I<N;++I){
		cin >> s >> n;
		int l = s.length();
		vector<int> c(l,0);
		int count = 0;

		for (int i=0;i<l;++i){
			if (isConsonant(s[i]))
				count++;
			else
				count = 0;
			c[i] = count;
		}

		vector<int> a(l,l);
		int last = l;
		for (int i=l-n;i>=0;--i){
			if (c[i+n-1]>=n)
				last = i+n-1;
			a[i] = last;
		}

		x = 0;
		for (int i=0;i<l;++i)
			x += (l-a[i]);

		cout << "Case #" << I+1 << ": " << x << endl;
	}
	return 0;
}
