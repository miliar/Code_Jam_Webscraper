#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

pair<string, string> f[2000];

int main(){
	ios_base::sync_with_stdio(false);
	int z;
	cin >> z;
	
	for(int l = 1; l <= z; l++){
		
		int N;
		cin >> N;
		
		for(int i = 1;  i <= N; i++)
			cin >>f[i].first >> f[i].second;
			
		int tab[] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16};
		int maks_fake = 0;
		for(int test = 0; test <=100000;test++){
			int fake = 0;
			for(int i = 0; i < N; i++){
				
				bool is_first = false, is_second=false;
				for(int j = 0; j < i; j++){
					if(f[tab[j]].first==f[tab[i]].first)is_first=true;
					if(f[tab[j]].second==f[tab[i]].second)is_second=true;
				}
				
				if(is_first == true && is_second == true){
					fake++;
				}
			}
			maks_fake = max(maks_fake, fake);
			
			random_shuffle(tab, tab+N);
		}
		
		cout << "Case #" << l << ": ";
		cout << maks_fake;
		cout << endl;
	}
}
