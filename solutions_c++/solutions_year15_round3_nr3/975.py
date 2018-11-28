#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);

using namespace std;
std::vector<int> v;
bool getBit(int n,int i){
	return n>>i & 1 !=0;
}
int main() {
	int T;
	cin>>T;
	for (int cas = 1; cas <=T ; ++cas)
	{
		int C, D, V;
		cin>>C>>D>>V;
		v.clear();
		for (int i = 0; i < D; ++i)
		{
			int x;cin>>x;
			v.push_back(x);
		}
		// cout<<"Hi\n";
		int y=0;
		while(1){
			sort(v.begin(), v.end());
			int n=v.size();
			std::vector<bool> canMake(V+1,0);
			for (int mask = 0;  mask< (1<<n) ; ++mask)
			{
				int val=0;
				for (int i = 0; i < n; ++i)
				{
					if(getBit(mask,i))
						val+=v[i];
				}
				// cout<<"val "<<val<<endl;
				canMake[val]=1;
			}
			bool check=1;
			for (int i = 1; i <=V ; ++i)
			{
				if(canMake[i]==0) check=0;
			}
			if(check)
				break;
			for (int i = 1; i <=V ; ++i)
			{
				if(!canMake[i]){
					y++;
					v.push_back(i);
					break;
				}
			}
		}
		cout<<"Case #"<<cas<<": "<<y<<endl;
	}
	return 0;
}