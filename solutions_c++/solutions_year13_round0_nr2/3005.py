#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

class Lawn {
	private:
		vector<char> heights;
		int width;
		int height;
	public:
		Lawn(int N, int M): heights(N*M), width(M), height(N){
		}
		
		void setHeight(int n, int m, char value){
			heights[n*width+m] = value;
		}
		
		char getHeight(int n, int m){
			return heights[n*width+m];
		}
};

int main(){
	int T;
	scanf("%d", &T);
	for(int t=0; t<T; t++){
		int N, M;
		scanf("%d %d", &N, &M);
		Lawn targetLawn(N, M);
		for(int n = 0; n<N; n++){
			for(int m = 0; m<M; m++){
				int value;
				scanf("%d", &value);
				targetLawn.setHeight(n, m, value);
			}
		}
		bool canMakePattern = true;
		
		Lawn lawn(N, M);
		for(int n=0; n<N; n++){
			for(int m=0; m<M; m++){
				//can we get the desired height without fuckin up?
				char target = targetLawn.getHeight(n,m);
				bool rowok = true;
				bool colok = true;
				for(int i=0; i<M; i++){
					char target2 = targetLawn.getHeight(n,i);
					if(target2>target){
						rowok = false;
						break;
					}
				}
				if(rowok){
					continue;
				}
				for(int i=0; i<N; i++){
					char target2 = targetLawn.getHeight(i,m);
					if(target2>target){
						colok = false;
						break;
					}
				}
				if(!rowok && !colok){
					canMakePattern = false;
					break;
				}
			}
			if(canMakePattern == false){
				break;
			}
		}
		
		printf("Case #%d: ", t+1);
		
		if(canMakePattern){
			printf("YES");
		} else {
			printf("NO");
		}
		
		printf("\n");
		
	}
}
