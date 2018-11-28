#include <bits/stdc++.h>
using namespace std;

long long t, n, ans;
char c;
vector<bool> cakes;

/*int blankends(){
	for(int i = 1; ; i++){
		if(cakes[cakes.size()-i]){
			return i-1;
		}
	}
}*/

int happystarts(){
	for(int i = 0; ; i++){
		if(!cakes[i]){
			return i;
		}
	}
}

int main(){
	scanf("%lld\n", &t);
	for(int tc = 0; tc < t; tc++){
		cakes.clear();
		ans = 0;
		for(n = 0; scanf("%c", &c);n++){
			if(c == '\n'){break;}
			if(c == '+'){
				cakes.push_back(true);
			} else if(c == '-'){
				cakes.push_back(false);
			} else {
				printf("ERROR\n");
			}
		}
		
		/*for(int i = 0; i < cakes.size(); i++){
			printf("%d ", (int)cakes[i]); 
		} printf("\n");*/
		
		while(!cakes.empty()){
			//printf("cakes.size() = %lu\n", cakes.size());
			while(!cakes.empty() && cakes[cakes.size()-1]){
				cakes.pop_back();
			}
			//printf("cakes.size() = %lu\n", cakes.size());
			if(cakes.empty()){break;}
			int h = happystarts();
			for(int i = 0; i < h; i++){
				cakes[i] = !cakes[i];
			} if(h){ans++;}
			
			for(int i = 0; i < cakes.size(); i++){
				cakes[i] = !cakes[i];
			} reverse(cakes.begin(), cakes.end()); ans++;
		}
		printf("Case #%d: %lld\n", tc+1, ans);
	}
}
