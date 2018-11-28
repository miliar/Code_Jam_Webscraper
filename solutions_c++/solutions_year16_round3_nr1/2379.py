#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main (int argc, char const* argv[])
{
	ios_base::sync_with_stdio(false);cin.tie(0);
	int t; cin>>t;
	for (int i = 0; i < t; ++i)
	{
		int n, a[28], sum = 0; cin>>n;
		for(int j = 0; j < n; ++j) {
			cin>>a[j];
			sum += a[j];
		}
		cout<<"Case #"<<(i+1)<<": ";
		while(sum > 0){
			for(int x = 0; x < n; ++x){
				if(a[x]) {
					a[x]--; 
					sum--;
				}
				else continue;
				bool f = true;
				for(int j = 0; j < n; ++j){
					double r; 
					if(sum == 0) r = 0;
					else r = (double) a[j] / sum;
					if(r > 0.5) f = false; 
				}
				if(f){
					//cout<<x<<endl;
					cout<<((char) ('A' + x));
					if(sum != 0) cout<<" ";
					break;
				}
				else {
					int y;
					for(y = x; y < n; ++y){
						f = true; 
						//cout<<sum<<" "<<x<<" "<<y<<"||";
						//for(int k = 0; k < n; ++k) cout<<a[k]<<" "; cout<<endl;
						if(a[y]) {
							a[y]--; 
							sum--;
						}
						else continue;
						for(int j = 0; j < n; ++j){
							double r;
							if(sum == 0) r = 0;
							else r = (double) a[j] / sum;
							if(r > 0.5) f = false; 
						}
						if(f){
							char xx =  ('A' + x), yy = ('A' + y);
							string soli = "" + xx + yy;
							cout<<xx<<yy;
							if(sum != 0) cout<<" ";
							break;
						}
						else {
							++a[y]; ++sum;				
						}
					}
					if(y == n) {
						++a[x]; ++sum;
					}	
				}
			}
		
		}
		cout<<"\n";
	}
	return 0;
}
//  BC
// B A BA 
