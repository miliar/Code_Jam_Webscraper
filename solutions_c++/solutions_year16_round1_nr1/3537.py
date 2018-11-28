#include <iostream>

using namespace std;

int main() {
	int test;
	cin>>test;
	for(int t=1; t<=test; t++) {
		string q,a;
		cin>>q;

		a = q[0];
		for (int i = 1; i < (q.size()); ++i)
		{
			if(q[i]>='A' && q[i]<='Z') {
				if(q[i]>=a[0])
					a = q[i] + a;
				else
					a = a + q[i];
			}
		}

		cout<<"Case #"<<t<<": "<<a<<endl;
	}
	return 0;
}