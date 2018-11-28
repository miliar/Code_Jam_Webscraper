#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

int map[100][100]={0};
int n=0;
int m=0;

bool analizeH(int a, int b){
	for(int i=0; i<m; i++){
	    if( map[a][i]<=map[a][b] )
	        continue;
		else
		    return false;
	}
	return true;
}
bool analizeV(int a, int b){
	for(int i=0; i<n; i++){
	    if( map[i][b]<=map[a][b] )
	        continue;
		else
		    return false;
	}
	return true;
}

bool Analize(){
	for(int j=0; j<n; ++j){
        for(int k=0; k<m;++k){
			if ( analizeH(j, k) || analizeV(j, k) )
	    		continue;
			else return false;
		}
	}
	return true;
}

int main(){
	int Testcases=0;
	bool output;
	std::string line;

	std::ifstream ifs ( "test.in" , std::ifstream::in );
	std::ofstream ofs ( "test.out" , std::ifstream::out );

	ifs >> Testcases;
	std::getline( ifs, line);
	for ( int i=0; i<Testcases;++i ){
		ifs>>n>>m;

		for(int j=0; j<n; ++j){
            for(int k=0; k<m;++k){
				ifs>>map[j][k];
			}
		}
		output=Analize();

		ofs<<"Case #"<<i+1<<": "<<((output)?"YES": "NO")<<std::endl;

	}

	ifs.close();
	ofs.close();

	//std::cin.get();
}
