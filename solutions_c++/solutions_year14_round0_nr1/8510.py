#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>


using namespace std;


int main(int argc, char* argv[])
{
	ifstream input("A-small-attempt0.in");
	//ifstream input("test.data");
    ofstream output("output.out");

    
	int cases;
	
	input >> cases;
	
	

	for(int i=1;i<=cases;i++){

		int A[4][4];
        int Anew[4][4];
		bool flag = false;
		bool bad = false;
		int answer;
	    int newanswer;
	    int index;

		output << "Case #"<<i<<": ";
		input >> answer;
		for(int x=0;x<4;x++){
			for(int y=0;y<4;y++){
				input >> A[x][y];
			}
		}

		input >> newanswer;
		for(int x=0;x<4;x++){
			for(int y=0;y<4;y++){
				input >> Anew[x][y];
			}
		}

		newanswer--;
		answer--;

		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
			if(A[answer][i] == Anew[newanswer][j] && bad == false){
				index = i;
				if(flag == false){
					flag = true;
				}
				else{
					bad = true;
				}
			}
		    }
		}

		if(bad == true)
			output << "Bad magician!";
		else if(flag == false)
			output << "Volunteer cheated!";
		else
			output << A[answer][index];
		output << endl;
	}

	input.close();
	output.close();


	return 0;
}

