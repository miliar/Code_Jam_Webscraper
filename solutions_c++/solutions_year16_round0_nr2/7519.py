#include <iostream>
#include <cmath>
#include <string>
#include <map>
using namespace std;

int flip(const string &pancakes, int idLast , int flips){
	if(idLast == -1)
		return flips;
	
	string npancakes(pancakes.size(), '+');
	int nidLast = -1, cid = 0;
	for(;cid < idLast; ++cid){
		npancakes[cid] = (pancakes.at(cid) == '+')?('-'):('+');
		if(npancakes.at(cid) == '-')
			nidLast = cid;
	}
	
	return flip(npancakes, nidLast, flips+1);
	
}

int main(){
	int t, nbFlips;
	string pancakePile;
	
	cin >> t;
	
	for(int i = 1; i <= t; ++i){
		cin >> pancakePile;
		
		int pileSize = pancakePile.size(), s;
		
		for(s = pileSize-1; s >= 0 && pancakePile.at(s) == '+' ; --s ){}
		
		nbFlips = flip(pancakePile, s, 0);
		
		  cout << "Case #" << i << ": ";
		  cout << nbFlips << endl;
		    
	}

}
