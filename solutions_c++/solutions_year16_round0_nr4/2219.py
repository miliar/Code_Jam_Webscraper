#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int T;
	vector<vector<long long> > result;
	cin>>T;
	result.resize(T);
	for(int i=0;i<T;i++) {
		int K, C, S, temp=0;
		cin>>K>>C>>S;
		if(C*S<K)
			continue;
		for(int j=0;j<S && temp<K;j++) {
			long long num=1;
			for(int k=0;k<C;k++) {
				num=(num-1LL)*K+(temp==K ? 1LL:++temp);
			}
			result[i].push_back(num);
		}
	}
	for(int i=0;i<T;i++) {
		cout<<"Case #"<<i+1<<":";
		for(int j=0;j<result[i].size();j++)
			cout<<' '<<result[i][j];
		if(result[i].size()==0)
			cout<<"IMPOSSIBLE";
		cout<<endl;
	}
    return 0;
}