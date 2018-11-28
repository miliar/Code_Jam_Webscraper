#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>

using namespace std;
#define SMALL
//#define LARGE

int main(){
    FILE *fp, *fpout;
    int T,N,M;
    
#ifdef SMALL    
    freopen("B-small-0.in", "rt", stdin);
    freopen("B-small-0.out", "wt", stdout);
#endif    

#ifdef LARGE    
    freopen("B-large-0.in", "rt", stdin);
    freopen("B-large-0.out", "wt", stdout);
#endif    

    cin >> T;

    for(int cur= 0; cur < T; cur ++){
    	    cin >> N >> M;
	    bool case_possible = true;
    	    char arr[N][M];
	    //cout << " N: " << N << " M: " << M << endl;
	    for(int i= 0;i< N; i++){
		for(int j=0;j< M; j++){
			cin >> arr[i][j];
		}
	    }
	    
	    for(int i= 0;i< N; i++){
		for(int j=0;j< M; j++){
			int big_r = 0, big_c = 0;
			//cout << "i: " << i << " j: " << j << endl;

			// Check the bigger number on row wise 
			// I row and J column : Row will remain same  
			char refrence = arr[i][j];
			for(int l = 0; l< M; l++){
				if(l == j)
					continue;
				if(arr[i][l] > refrence){
					//cout << " arr[i][l]: " << arr[i][l] << endl;
					//cout << " reference: " << refrence << endl;
					big_r = 1;
				}
			}

			// Check the bigger number on column wise
			// I row and J column : Column will remain same  
			for(int l = 0; l< N; l++){
				if(l == i)
					continue;
				if(arr[l][j] > refrence){
					//cout << " arr[l][j]: " << arr[l][j] << endl;
					//cout << " reference: " << refrence << endl;
					big_c = 1;
				}
			}
			if(big_r == 1 && big_c == 1)
			{
				case_possible = false;
			}
		}
	    }
	if(case_possible)
		cout << "Case #" << cur+1 << ": YES" << endl;
	else
		cout << "Case #" << cur+1 << ": NO" << endl;
	    
    }
    
    return 0;
}

