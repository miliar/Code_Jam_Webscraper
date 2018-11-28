#include <bits/stdc++.h>



using namespace std;

typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef queue<int> qi;
typedef queue<ii> qii;
typedef long long ll;

bitset<10> bs;
bool check(int num){
	if(num == 0) bs.set(num);
	while(num!=0){
		int reg = num%10;
		bs.set(reg);
		num /=10;
	}
	if(bs.all())
		return true;

	return false;
}
int main()
{
	int T;
	cin>>T;
	int CT = T;
	while(T--){
		int N;
		cin>>N;
		bs.reset();
		cout<<"Case #"<<(CT-T)<<": ";
		if(N == 0) {
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		for (int i = 1; ; ++i)
		{
			if(check(N*i))
			{
				cout<<(N*i)<<endl;
				break;
			}
		}
	}
	return 0;
}