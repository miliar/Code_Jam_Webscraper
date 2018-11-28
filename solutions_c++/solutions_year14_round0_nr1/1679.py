#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <unordered_map>

using namespace std;
int main(int argc, char const *argv[])
{
	ifstream infile("A-small-attempt0.in");
	ofstream outfile("magic.ot");
	int N = 0;
	infile >> N;

    for(int i = 0; i < N; ++i){
    	vector<int> cards(4,0);
    	int frow = 0;
    	infile >> frow;
    	int temp  = 0;
    	for(int j = 0; j<4; ++j){
    	    for(int k = 0; k < 4; ++k)
    		    if(j == frow-1)
                   infile >> cards[k];
    		    else
    			   infile >> temp;
    	}
    	int srow = 0;
    	infile >> srow;
    	int count = 0;
    	int seletCard = 0;
    	for(int j = 0; j < 4; ++j){
    		for(int k = 0; k < 4; ++k){
    			infile >> temp;
    			if (j == srow-1){
    				if(find(cards.begin(),cards.end(), temp) != cards.end()){
    					count ++;
    					seletCard = temp;
    				}
    			}
    		}
    	}
    	outfile << "Case #" << i + 1 << ": ";
    	cout << "Case #" << i + 1 << ": ";
    	if (count > 1)
    		outfile << "Bad magician!";
        else if(count == 1)
        	outfile << seletCard;
        else
        	outfile << "Volunteer cheated!";

        if(i != N-1)
        	outfile << "\n";
    }

    infile.close();
    outfile.close();
	return 0;
}