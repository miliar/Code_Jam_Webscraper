#include <iostream>
#include <set>

using namespace std;

int main(){
	int t;cin>>t;
	for(int i=0;i<t;i++){
		int n;cin >> n;
		set<int> d;
		if(n==0){ cout << "Case #"<<i+1<<": INSOMNIA"<<endl;continue;}
		int k = 0;
		while(d.size()<10){
			k++;
			int m = n*k;
			do {
				int digit = m % 10;
				d.insert(digit);
				m /= 10;
			} while (m > 0);
		}
		
		cout << "Case #"<<i+1<<": "<<k*n<<endl;
	}
	return 0;
}
