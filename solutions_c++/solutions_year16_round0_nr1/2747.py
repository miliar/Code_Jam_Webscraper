#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char *argv[]) {
	int t;
	cin>>t;
	for(int i=1;i<=t;i++) {
		vector<bool> numbers(10,0);
		cout<<"Case #"<<i<<": ";
		int n;
		cin>>n;
		if(n==0)
			cout<<"INSOMNIA"<<endl;
		else{
			bool all=false;
			int j=0;
			while(!all){
				j++;
				int number=j*n;
				while(number)
				{
					numbers[number%10]=1;
					number/=10;
				}
				all=1;
				for(int k=0;k<numbers.size();k++)
					all&=numbers[k];
			}
			cout<<j*n<<endl;
		}
	}
	return 0;
}

