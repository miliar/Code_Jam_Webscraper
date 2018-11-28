#include <fstream>
#include <sstream>
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char * argv[]){
	if(argc < 2){
		cerr << "Insufficient arguments\nUsage: a <filename>";
	}
	
	char * filename = argv[1];
	ifstream ifs(filename);
	if(!ifs){
		cerr << "File open failed: " << filename << endl;
		return false;
	}
	
	ofstream ofs("out.txt");
	if(!ofs){
		cerr << "File open failed: out.txt" << endl;
		return false;
	}
	
	int T;
	ifs >> T;
	for(int t = 0; t < T; t++){
		int friends = 0, standing = 0, smax;
		string audience = "";
		
		ifs >> smax >> ws;
		ifs >> audience;
		
//		cout << "#" << (t + 1) << ": " << audience << endl;
		
		for(int shyness = 0; shyness < (smax + 1); ++shyness){
			string temp(1, audience[shyness]);
			istringstream iss(temp);
			int a;
			iss >> a;
			
//			cout << "s=" << standing << " f=" << friends;
			
			if(standing < shyness){
				friends += (shyness - standing);
				standing += (shyness - standing);
			}
			standing += a;
			
//			cout << " shyness=" << shyness << " a=" << a << " s=" << standing << " f=" << friends << endl;
		}
		cout << "Case #" << (t + 1) << ": " << friends << endl;
		ofs << "Case #" << (t + 1) << ": " << friends << endl;
	}
	return 0;
}