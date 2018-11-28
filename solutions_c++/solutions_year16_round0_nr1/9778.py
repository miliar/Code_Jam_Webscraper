#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char ** argv){
    int nTest;

    ifstream inFile;
    ofstream outFile;

    inFile.open(argv[1]);
    outFile.open(argv[2]);

    inFile >> nTest;
    
    vector<int> Arr;

    Arr.resize(10);

    for(int idx = 0 ; nTest > idx ; idx++){
	int cu;

	long long result;

	for(int ai = 0 ; 10 > ai ; ai++){
	    Arr[ai] = 1;
	}


	inFile >> cu;

	if(0 == cu){
	    outFile << "Case #" << idx+1 <<": INSOMNIA" << endl;
	}else{
	    long long num = 1ll;

	    int sum;
	    do{
		long long value = static_cast<long long>(cu) * num;
		result	= value;

		vector<int> valueT;

		valueT.clear();

		while(value > 0){
		    valueT.push_back(value %10);
		    value /= 10;
		}

		sum = 0;

		for(int ai = 0 ; 10 > ai ; ai++){
		    if(1 == Arr[ai]){
			if(valueT.end() != find(valueT.begin(), valueT.end(), ai)){
			    Arr[ai] = 0;
			}else{
			    sum++;
			}
		    }
		}
		num++;
	    }while(0 < sum);

	    outFile << "Case #" << idx+1 <<": " << result << endl;
	}
    }

    inFile.close();
    outFile.close();

    return 0;
}
