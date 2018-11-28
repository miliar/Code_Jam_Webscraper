#include <iostream>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>
using namespace std;


set<int> s;

int main()
{
	long long n;
	cin >> n;
	for (long long i = 0; i<n; i++) {
		long long num;
		cin>>num;
		long long incr = num;
		while(s.size()!=10&&num!=0) {
			long long c = num%10;
			long long cc = num/10;
			while (1) {
				s.insert(c);
				c=cc%10;
				if(cc==0)
					break;
				cc/=10;

			}
			if(s.size()==10)
				break;
			num+=incr;
		}
		s.clear();

		if(num==0){
			cout<< "Case #"<<i+1<<": INSOMNIA"<<endl;
		} else {
			cout<< "Case #"<<i+1<<": " <<num<<endl;
		}
	}


	return 0;
}
