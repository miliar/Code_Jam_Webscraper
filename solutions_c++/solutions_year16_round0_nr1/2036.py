#include<bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
	
		int n;
		cin>>n;
		for (int i = 0; i < n; ++i)
		{
			int x;
			int bitset = 0;
			cin>>x;
			if(x==0){
				cout<< "Case #"<<i+1<<": INSOMNIA"<<endl;
			} else {
				for (int k = 1; ; ++k)
				{
					int y = x*k;
					while(y!=0){
						bitset = bitset|(1<<(y%10));
						// cout<<bitset<<" "<<y%10<<endl;
						y = y/10;
					}
					if(bitset==((1<<10)-1)) {
						cout<<"Case #"<<i+1<<": "<<x*k<<endl;
						break;
					}
				}
			}
		}
	return 0;
}