#include<stdio.h>
#include<stdlib.h>

using namespace std;
#include<vector>
#include<algorithm>

vector<double> Naomi;
vector<double> Ken;

int main(int argc, char* argv[]){
    FILE *fin;
    fin = fopen(argv[1], "r");

    int T, N, win_d, win_o, woodind_n, woodind_k;
    double wood_weight;
    fscanf(fin, " %d ", &T);
    for(int tc=0; tc<T; ++tc){
	Naomi.clear();
	Ken.clear();

	fscanf(fin, " %d ", &N);
	for(int wood=0; wood<N; ++wood){
	    fscanf(fin, " %lf ", &wood_weight);
	    Naomi.push_back(wood_weight);
	}
	for(int wood=0; wood<N; ++wood){
	    fscanf(fin, " %lf ", &wood_weight);
	    Ken.push_back(wood_weight);
	}

	sort(Naomi.begin(), Naomi.end());
	sort(Ken.begin(), Ken.end());

/*
	for(int wood=0; wood<N; ++wood)	printf("%f ", Naomi[wood]);
	printf("\n");
	for(int wood=0; wood<N; ++wood)	printf("%f ", Ken[wood]);
	printf("\n");
*/

	win_o = 0;
	woodind_k = 0;
	for(woodind_n=0; woodind_n<N; ++woodind_n){
	    for(; woodind_k<N; ++woodind_k){
		if(Ken[woodind_k] > Naomi[woodind_n]){
		    break;
		}
	    }
	    if(woodind_n == N-1){
		win_o = woodind_k - woodind_n;
	    }else if(woodind_k == N){
		win_o = N - woodind_n;
		break;
	    }
	    ++woodind_k;
	}

	win_d = 0;
	woodind_n = woodind_k = 0;
	for(; woodind_n<N && woodind_k<N; ){
	    if(Naomi[woodind_n] > Ken[woodind_k]){
		++win_d;
		++woodind_n;
		++woodind_k;
	    }else{
		++woodind_n;
	    }
	}

	printf("Case #%d: %d %d\n", tc+1, win_d, win_o);
    }
    fclose(fin);

    return 0;
}
