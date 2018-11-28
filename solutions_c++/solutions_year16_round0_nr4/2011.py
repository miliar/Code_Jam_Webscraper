#include <iostream>


using namespace std;


int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio(0);
	cin.tie();
	int T;
	cin>>T;
	for(int t=0; t<T; ++t){
		cout<<"Case #"<<t+1<<":";
		long long int k, c, s;
		cin>>k>>c>>s;
		long long int minimum = k/c;
		if(k%c)
			minimum++;
		if(s<minimum){
			cout<<" IMPOSSIBLE\n";
			continue;
		}

		long long int p=0;

		for(int i=0; i<minimum; ++i){
			long long int pos = ++p;
			//cout<<pos<<" ";
			for(int j=1; j<c; ++j){
				if(p<k)
					++p;
				pos = (pos-1)*k + p;
				//cout<<pos<<" ";
			}
			cout<<" "<<pos;
		}



		cout<<"\n";
	}



	return 0;
}