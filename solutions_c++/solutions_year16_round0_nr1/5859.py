#include <iostream>
#include <algorithm>
#include <set>
using namespace std;
inline void check(long long n, set<int>& cnt)
{
	while(n > 0)
	{
		cnt.insert(n % 10);
		n /= 10;
	}
}
long long work(long long n,int numbers)
{
	set<int> cnt;
	cnt.clear();
	long long tot = 0;
	for (int i = 1;i <= numbers;i ++)
	{
		tot += n;
		check(tot, cnt);
//		cout << "size:" << cnt.size() << endl;
		if (cnt.size() == 10)
		{
			return tot;
		}
	}	
	return -1;
}

int main(){
	int T;
	long long n;
	cin >> T;
	for (int cas = 1;cas <= T;cas ++)
	{
		cin >> n;
		long long ret = work(n, 10000000);
		if (ret == -1){
			cout << "Case #" << cas << ": INSOMNIA" << endl;
		}else {
			cout << "Case #" << cas << ": " << ret << endl;
		}
	}
	return 0;
}

