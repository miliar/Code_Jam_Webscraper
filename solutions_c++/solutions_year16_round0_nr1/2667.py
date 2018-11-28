#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;
bool check_if_all_found(int N, bool num[]){
	while(N > 0){
		int temp = N % 10;
		num[temp] = true;
		N = N/10;
	}
	for(int i = 0; i < 10; i++)
		if(! num[i])
			return false;
	return true;
}
int main(int argc, char const *argv[])
{
	int T = 0;
	scanf("%d", &T);
	for(int t = 0; t < T; t++){
		int N = 0;
		scanf("%d", &N);
		int i= 0;
		bool num[10] = {false};
		if(N > 0){
			while(!check_if_all_found(N*i, num))
				i++;
			printf("Case #%d: %d\n", t+1, N*i);
		}else
			printf("Case #%d: INSOMNIA\n", t+1);
	}
	return 0;
}