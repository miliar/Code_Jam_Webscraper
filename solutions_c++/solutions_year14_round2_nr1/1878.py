#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

int main(){
	int t; scanf("%d", &t);
	for(int cas=1;cas<=t;cas++){
		int n; scanf("%d", &n);
		vector<string> v;
		for(int k=1;k<=n;k++){
			char c[200]; scanf("%s", c);
			v.push_back(string(c));
		}
		/*for(int i=0;i<n;i++){
			cout << v[i] << "\n";
		}
		return 0;*/
		bool broken = false;
		char c;
		vector<int> ks(n, 0);
		vector<int> at(n, 0);
		int ans = 0;
		bool go = true;
		while(go){
			c = v[0][at[0]];

			int avg = 0;
			for(int i=0;i<n;i++){
				ks[i] = 0;
				for(int j=at[i];j<v[i].length();j++){
					if(v[i][j] == c){
						ks[i]++;
					}else{
						break;
					}
				}
				avg += ks[i];
				at[i] += ks[i];

				if(at[i] >= v[i].length()){
					go = false;
				}

				if(ks[i] == 0){
					broken = true;
					break;
				}
			}
			if(broken) break;
			avg = round((1.0*avg)/n);
			//cout << avg << endl;
			for(int i=0;i<n;i++){
				ans += abs(avg-ks[i]);
			}

		}
		for(int i=0;i<n;i++){
			if(at[i] < v[i].length()){
				broken = true;
				break;
			}
		}
		
		if(broken){
			printf("Case #%d: Fegla Won\n", cas);
		}
		else{
			printf("Case #%d: %d\n", cas, ans);
		}
	}
}
