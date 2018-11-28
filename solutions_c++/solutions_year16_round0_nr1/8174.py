#include <iostream>
#include <cstring>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	int i=0;
	while(i++<t){
		long n;
		cin>>n;
		bool hash[10];
		memset(hash,0,sizeof(hash));
		int count = 0;
		long int num = n,d = n;
		int rem;
		n=0;
		while(count<10){
			n += num;
			//cout<<"n="<<n<<endl;
			d = n;
			if(d==0){
				cout<<"Case #"<<i<<": INSOMNIA"<<endl;
				break;
			}
			while(d!=0){
				rem = d%10;
				if(!hash[rem]){
					hash[rem]=true;
					count++;
				}
				d = d/10;
			}//inner while
		}//outer while

		if(count == 10){
			cout<<"Case #"<<i<<": "<<n<<endl;
		}

	}
	return 0;
}
