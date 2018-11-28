#include <iostream>
#include <fstream>
using namespace std;

int main(){
	ifstream fin;
	ofstream fout;
	fin.open("fin.txt");
	fout.open("fout.txt");
	int T;
    int n,m;
	fin >> T;
	for(int where=0;where<T;where++){
	   fin >> n >> m;
	   int lawn[n][m];
	   for(int a=0;a<n;a++){
	      for(int b=0;b<m;b++){
	        fin >> lawn[a][b];
		  }
	   }
	   int current,sobib=2;
	   for(int a=0;a<n;a++){
	      for(int b=0;b<m;b++){
	        current=lawn[a][b];
	        sobib=2;
	        for(int x=0;x<n;x++){
              if(current<lawn[x][b]){
                sobib--;
                break;
			  }
			}
	        for(int y=0;y<m;y++){
              if(current<lawn[a][y]){
                sobib--;
                break;
			  }
			}
			if(sobib==0){
			  fout << "Case #" << where+1 << ": NO\n";
			  break;
			}
			else sobib=2;
		  }
		  if(sobib==0) break;
	   }
	   if(sobib==0) continue;
	   else fout << "Case #" << where+1 << ": YES\n";
	}
	return 0;	
}
