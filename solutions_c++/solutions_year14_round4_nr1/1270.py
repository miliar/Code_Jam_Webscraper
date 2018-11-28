#include <iostream>
#include <fstream>
#include <set>
using namespace std;

int arr[10010];
int main () 
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int TC;
	cin >> TC;
	for(int tc = 1 ; tc<=TC ; ++tc)
	{
		int N , D;
		cin >> N >> D;
		multiset<int> S;
		for (int i = 0; i < N; ++i) {
			int n;
			cin >> n;
			S.insert(n);
		}
		int cnt = 0;
		while(S.size())
		{
			cnt++;
			int d = *S.begin();
			S.erase(S.begin());
			if(S.size() == 0)continue;
			multiset<int>::iterator it = S.upper_bound(D - d);
			if(it == S.begin())continue;
			it--;
			S.erase(it);
		}
		cout << "Case #"<< tc << ": " << cnt << endl;
	}
}


