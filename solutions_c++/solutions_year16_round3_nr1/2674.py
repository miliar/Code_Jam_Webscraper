#include <bits/stdc++.h>
typedef long long ll;

using namespace std;

int main(int argc, char const *argv[]){

	int t;
	cin >> t;

	for (int i = 0; i < t; ++i)
	{
		int n;
		cin >> n;
		int tp;
		vector<int> p;
		string plan = "";
		int sum = 0;
		for (int j = 0; j < n; ++j)
		{
			cin >> tp;
			p.push_back(tp);
			sum += tp;
		}

		if(n == 2){
			while(p[0]!=0 || p[1] != 0){
				if(p[0] > p[1])
				{
					for (int j = 0; j < p[0] - p[1]; ++j)
					{
						plan += (char)(0 + 'A');
					}
					p[0] -= (p[0] - p[1]);
				}
				else if(p[0] < p[1])
				{
					for (int j = 0; j < p[1] - p[0]; ++j)
					{
						plan += (char)(1 + 'A');
					}
					p[1] -= (p[1] - p[0]);
				}
				else if(p[0] == p[1]){
					plan += (char)(0 + 'A');
					plan += (char)(1 + 'A');
					p[0] -= 1;
					p[1] -= 1;					
				}
				plan += " ";
			}
		}
		else{
			while(sum != 0){

				int maxidx = 0;
				for (int j = 1; j < p.size(); ++j)
				{
					if(p[j] > p[maxidx]){
						maxidx = j;
					}
				}

				p[maxidx] -= 1;
				sum-=1;
				plan += (char)(maxidx + 'A');

				if(sum > 0){
					int maxidx2 = 0;
					for (int j = 1; j < p.size(); ++j)
					{
						if(p[j] > p[maxidx2]){
							maxidx2 = j;
						}
					}
					if(sum - 1 != 1){
						p[maxidx2] -= 1;
						sum-=1;
						plan += (char)(maxidx2 + 'A');
					}
				}

				plan += " ";
			}
		}
		
		cout << "Case #" << (i + 1) << ": " << plan << "\n";	
	}

	return 0;
}