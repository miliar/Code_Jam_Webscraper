#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
FILE *in = fopen("D-large.in","r");
FILE *out= fopen("output.txt","w");
int main()
{
	int T,N;
	fscanf(in, "%d", &T);
	for(int testCase = 1; testCase <= T; testCase++){
		fscanf(in, "%d", &N);
		vector<double> na, ken;
		na.resize(N, 0);
		ken.resize(N, 0);
		for(int i = 0; i < N; i++){
			fscanf(in, "%lf", &na[i]);
		}
		for(int i = 0; i < N; i++){
			fscanf(in, "%lf", &ken[i]);
		}
		sort(na.begin(), na.end());
		sort(ken.begin(), ken.end());
		int k=0, ans=0;
		for(int i = 0; i < N; i++){
			if(na[i] > ken[k]){
				ans++;
				k++;
			}
		}
		fprintf(out, "Case #%d: %d ", testCase, ans);
		ans = k = 0;
		for(int i = 0; i < N; i++){
			int j;
			for(j = 0; j < N; j++){
				if(ken[j] > 0 && ken[j] > na[i]){
					ken[j] = -1;
					break;
				}
			}
			if(j == N){
				for(int j = 0; j < N; j++){
					if(ken[j] > 0){
						ans++;
						ken[j] = -1;
						break;
					}
				}
			}
		}
		fprintf(out, "%d\n", ans);
	}
	return 0;
}