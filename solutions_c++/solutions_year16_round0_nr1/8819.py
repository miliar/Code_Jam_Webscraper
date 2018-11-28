#include <iostream>
#include <set>
using namespace std;
int main(){
	freopen("input.txt", "r", stdin);
	freopen("small_output.txt", "w", stdout);
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++)
	{
		long long a;
		cin >> a;
		set<int> st;
		for(int j = 1;j<=1000000; j++)
		{
			long long b = a * j;

			while(b > 9)
			{
				int d = b % 10;
				st.insert(d);
				b /= 10;
			}
			st.insert(b);
			if(st.size() == 10)
			{
				cout << "Case #" << i << ": "<< a * j <<"\n";
				break;
			}
		}
		if(st.size() < 10)
			cout << "Case #" << i << ": INSOMNIA\n";
	}
	return 0;
}