#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>


class basicAnalizer{
private:
	std::ifstream* ifs;
	
	int firstAnswer, secondAnswer;
	int firstDeck[16], secondDeck[16];
	
	void readData(){
		*ifs >> firstAnswer;
		*ifs >> firstDeck[0] >> firstDeck[1] >> firstDeck[2] >> firstDeck[3];
		*ifs >> firstDeck[4] >> firstDeck[5] >> firstDeck[6] >> firstDeck[7];
		*ifs >> firstDeck[8] >> firstDeck[9] >> firstDeck[10] >> firstDeck[11];
		*ifs >> firstDeck[12] >> firstDeck[13] >> firstDeck[14] >> firstDeck[15];
		*ifs >> secondAnswer;
		*ifs >> secondDeck[0] >> secondDeck[1] >> secondDeck[2] >> secondDeck[3];
		*ifs >> secondDeck[4] >> secondDeck[5] >> secondDeck[6] >> secondDeck[7];
		*ifs >> secondDeck[8] >> secondDeck[9] >> secondDeck[10] >> secondDeck[11];
		*ifs >> secondDeck[12] >> secondDeck[13] >> secondDeck[14] >> secondDeck[15];
	}
public:
	basicAnalizer(std::ifstream *ifs):ifs(ifs){ readData();}
	int doWork(){
		int o[4];
		int o2[4];
		firstAnswer--;
		secondAnswer--;
		o[0] = firstDeck[ (firstAnswer<<2) ];
		o[1] = firstDeck[ (firstAnswer<<2) + 1 ];
		o[2] = firstDeck[ (firstAnswer<<2) + 2 ];
		o[3] = firstDeck[ (firstAnswer<<2) + 3 ];
		
		secondDeck[ secondAnswer<<2 ];
		o2[0] = secondDeck[ (secondAnswer<<2) ];
		o2[1] = secondDeck[ (secondAnswer<<2) + 1 ];
		o2[2] = secondDeck[ (secondAnswer<<2) + 2 ];
		o2[3] = secondDeck[ (secondAnswer<<2) + 3 ];
		
		std::cout<<o[0]<<" "<<o[1]<<" "<<o[2]<<" "<<o[3]<<" "<<std::endl;
		std::cout<<o2[0]<<" "<<o2[1]<<" "<<o2[2]<<" "<<o2[3]<<" "<<std::endl;
		
		int counter=0, value;
		for (int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				if( o[i]==o2[j] ){
					counter++;
					value=o[i];
					break;
				}
			}
		}
		if (counter>1) return -1;
		if (counter==1 ) return value;
		return 0;
	}
};

int main(){
	int r=0;
	int Testcases=0;
	std::string line;

	std::ifstream ifs ( "test.in" , std::ifstream::in );
	std::ofstream ofs ( "test.out" , std::ifstream::out );
	
	ifs >> Testcases;
	std::getline( ifs, line);
	for ( int i=0; i<Testcases;++i ){
		basicAnalizer analizer( &ifs );
		
		r=analizer.doWork();
		
		if (r==0)
			ofs<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<std::endl;
		else if( r==-1 )
			ofs<<"Case #"<<i+1<<": "<<"Bad Magician!"<<std::endl;
		else
			ofs<<"Case #"<<i+1<<": "<<r<<std::endl;
	}

	ifs.close();
	ofs.close();

	//std::cin.get();
}
