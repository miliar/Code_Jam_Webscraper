#include <iostream>
#include <cstdlib>
#include <cstdio>
typedef long long int64;
using namespace std;

bool flags[10];

int getDigits(int64 n){
	while(n>0){
		flags[n%10] = true;
		n /= 10;
	}
	int ans = 0;
	for(int i=0; i<10; i++)
		if(flags[i])
			ans++;
	return ans;
}

int main()
{
	freopen("D:\\A-large.in", "r", stdin);
	freopen("D:\\output.txt", "w",  stdout);
	int t;
	int64 N;
	cin>>t;

	for(int j=1; j<=t; j++){
		cout<<"Case #"<<j<<": ";
		cin>>N;
		if(N==0){
			cout<<"INSOMNIA\n";
			continue;
		}

		for(int i=0; i<10; i++)
			flags[i] = false;
		int used = 0;
		int i;

		for(i=1; i<1001; i++){
			used = getDigits(N*i);
			if(used==10)
				break;
		}
		cout<<N*i<<endl;
	}
}
