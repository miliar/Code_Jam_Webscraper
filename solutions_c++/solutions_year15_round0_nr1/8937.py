#include <iostream>
#include <fstream>
using namespace std;
ifstream fin("A-large.in");
ofstream fout("A-large.out");
main() {
	int t;
	int n;
	int sum;
	int shy[1005];
	int ans;
	char c;
	while (fin>>t){
		for (int z = 1; z <= t; ++z)
		{
			sum=0;
			ans=0;
			fin>>n;
			for (int i = 0; i <= n; ++i)
			{
				fin>>c;
				shy[i]=int(c)-'0';
			}
			for (int i = 0; i <= n; ++i)
			{
				if (i>sum){
					ans+=(i-sum);
					sum=i;
				}
				sum+=shy[i];
			}
			fout<<"Case #"<<z<<": "<<ans<<endl;
		}
	}
}