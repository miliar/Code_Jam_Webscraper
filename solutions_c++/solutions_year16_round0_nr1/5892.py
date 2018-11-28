#include <bits/stdc++.h>

using namespace std;

int ti[10];

int done(){
	return (ti[0] && ti[1]&& ti[2] && ti[3]&& ti[4]&& ti[5]&& ti[6]&& ti[7]&& ti[8]&& ti[9]);
}

int main()
{
	int t;
	cin>>t;
	for (int count=0; count<t; count++){
		printf("Case #%d: ", count+1);
		unsigned long long n;
		cin>>n;
		if (n==0) cout<<"INSOMNIA"<<endl;
		else{
			memset(ti, 0, sizeof(int) * 10);
			unsigned long long cur = n;
			while (!done()){
				unsigned long long aux = cur;
				while (aux>0){
					ti[aux%10]++;
					aux/=10;
				}
				cur += n;
			}

			cout<<cur - n<<endl;
		}
	}

	return 0;
}