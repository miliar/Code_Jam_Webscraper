#include <iostream>
#include <fstream>
#include <vector>
#include <string>

#include <stdlib.h>

using namespace std;

vector<int> tokenize(const string& str) {
    string next;
    vector<int> result;

    // For each character in the string
    for (string::const_iterator it = str.begin(); it != str.end(); it++) {
        // If we've hit the terminal character
        if (*it == ' ') {
            // If we have some characters accumulated
            if (!next.empty()) {
                // Add them to the result vector
                result.push_back(atoi(next.c_str()));
                next.clear();
            }
        } else {
            // Accumulate the next character into the sequence
            next += *it;
        }
    }
    if (!next.empty())
         result.push_back(atoi(next.c_str()));
    return result;
}
                           
int main(int argc, char **argv){
	
	if(argc == 2){

		ifstream input (argv[1]);
		
		if(input.is_open()){

			ofstream output("output");
			string line;

			getline(input, line);
			int nbTest = atoi(line.c_str());


			for(int i = 0 ; i < nbTest ; i++){

				int nbGoodRep = 0;
				int goodRep = -1;

				getline(input, line);
				int choosenRow1 = atoi(line.c_str());

				vector<int> vec1;
				for(int j = 1 ; j <= 4 ; j++){
					getline(input, line);
					if(j == choosenRow1)
						vec1 = tokenize(line);
				}


				getline(input, line);
				int choosenRow2 = atoi(line.c_str());

				vector<int> vec2;
				for(int j = 1 ; j <= 4 ; j++){
					getline(input, line);
					if(j == choosenRow2)
						vec2 = tokenize(line);
				}


				for(int j = 0 ; j < 4 ; j++){
					int actuelleVal = vec2[j];

					for(int k = 0 ; k < 4 ; k++){
						if(actuelleVal == vec1[k]){

							nbGoodRep++;
							goodRep = actuelleVal;
							cout << goodRep << endl;
						}
					}
				}

				if(nbGoodRep > 1)
					output << "Case #" << (i+1) << ": Bad magician!" << endl;
				else if (nbGoodRep == 0)
					output << "Case #" << (i+1) << ": Volunteer cheated!" << endl;
				else
					output << "Case #" << (i+1) << ": " << goodRep << endl;
			}


    		

			output.close();
    	}
		input.close();

	}else{
		cout << "./main_trick name_file" << endl;
	}
	return 0;
}