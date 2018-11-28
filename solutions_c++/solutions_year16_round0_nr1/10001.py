#include <iostream>
#include<set>
#include <fstream>
using namespace std;
int main(int argc, char* argv[]){
  	ifstream myfile (argv[1]);
  	if (myfile.is_open()){
		string line;
		int i = 1;
		int T = -1;
    		while ( getline (myfile,line) ){
			if(T == -1){
				T = stoi(line);
			}else{
				int n = stoi(line);
				set<int> num;
				set<int> cs;
		
				int nn = n; 
				while(true){
					if(num.count(nn) > 0){
						cout << "Case #"<< i <<": " << "INSOMNIA" << endl;
						break;
					}else{
						num.insert(nn);
						int nnn = nn;
						while(nnn > 0){
							cs.insert(nnn%10);
							nnn /= 10;
						}
						if(cs.size() == 10){
							cout << "Case #"<< i <<": " << nn << endl;
							break;
						}
					}
					nn += n;
				}
				i++;
			}
    		}
	}
    	myfile.close();
}
