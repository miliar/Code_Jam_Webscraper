#include <iostream>

using namespace std;




int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio(0);
	int T;
	cin>>T;
	for(int t = 1; t<=T; ++t){
		bool seen[11];
		for (int i = 0; i < 11; ++i)
		{
			seen[i]=false;
		}
		int n;
		cin>>n;
		if(n==0){
			cout<<"CASE #"<<t<<": INSOMNIA\n";
			continue;
		}
		int k=1;
		while(1){
			long long int temp = (long long int)k * (long long int)n;
			while(temp>0){
				seen[temp%10]=1;
				temp/=10;
			}
			bool comp=true;
			for (int i = 0; i < 10; ++i)
			{
				if(!seen[i]){

					comp=false;
					break;
				}
			}
			if(comp)
				break;
			++k;
		}
		cout<<"CASE #"<<t<<": "<<(long long int)k * (long long int)n<<"\n";


	}
	return 0;
}