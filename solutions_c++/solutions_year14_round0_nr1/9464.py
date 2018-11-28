#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int iter_num, m, n, a1[8];
    ifstream f2("e:\\A-small-attempt3.in");
	int res[100] = {0}, signal[100] = {0};
	f2>>iter_num;
	int p[16];
	for(int iter = 0; iter < iter_num; iter++){
		f2>>m;
        for(int i = 0; i < 4; i++){
        
	    	for(int j = 0; j < 4; j++){
        		f2>>p[i*4 + j];
        		if(i == m - 1){
        			a1[j] = p[i*4 + j];
        		}
        	}
        }
        f2>>n;
        for(int i = 0; i < 4; i++){
	    	for(int j = 0; j < 4; j++){
        		f2>>p[i*4 + j];
        		if(i == n - 1){
        			a1[j+4] = p[i*4 + j];
        		}
        	}
        }
        for(int i = 0; i < 4; i++){
	    	for(int j = 0; j < 4; j++){
        		if(a1[i] == a1[4 + j]){
        			res[iter] = a1[i];
        			signal[iter]++;
        		}
        	}
        }
    }
    ofstream f1("e:\\output.txt");
    for(int iter = 1; iter <= iter_num ; iter++){
    	if(signal[iter - 1] == 1){
    		f1<<"Case #"<<iter<<": "<<res[iter - 1]<<endl;
    	}
    	if(signal[iter - 1] == 0){
    		f1<<"Case #"<<iter<<": "<<"Volunteer cheated!"<<endl;
    	}
    	if(signal[iter - 1] > 1){
    		f1<<"Case #"<<iter<<": "<<"Bad magician!"<<endl;
    	}
    	
    }
	return 0;
}

