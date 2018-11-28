#include<bits/stdc++.h>
using namespace std;

int main()
{
	long long t;
	cin >> t;
	long long it = 1;
	while(it <= t)
	{
		map<long long,bool> mp;
		long long n;
		cin >> n;
		if(n == 0){
			cout << "Case #" << it << ": INSOMNIA" << endl;
			++it;
			continue;
		}
		long long add = n;
		while(1){
			long long flag = 0;
			for(long long i=0 ;i <= 9;i++){
				if(!mp[i]) flag = 1;
			}
			
			if(!flag) break;
			
			long long n1 = n;
			while(n1>0){
				mp[n1%10] = true;
				n1 = n1/10;
			}
			n += add;
		}
		n -= add;
		cout << "Case #" << it << ": " << n << endl; 
		it++;
	}
	return 0;
}
