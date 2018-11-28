#include <iostream>
#include <fstream>
#include <string>
#include <stack>
#include <algorithm>

using namespace std;


int main(){
	ofstream myfile;
	myfile.open("output.txt");

	ifstream myReadFile;
	myReadFile.open("A-large.in");

	int t, m;

	

	myReadFile >> t;

	for (int i = 1; i < t + 1; i++) {
		int n[10] = { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };

		myfile << "Case #" << i << ": ";

		string m;
		myReadFile >> m;
		
		while (m.find("Z") != std::string::npos){

			m = m.erase(m.find("Z"), 1);
			m = m.erase(m.find("E"), 1);
			m = m.erase(m.find("R"), 1);
			m = m.erase(m.find("O"), 1);
			n[0] = n[0]++;
		}

		/*while (m.find("O") != std::string::npos && m.find("N") != std::string::npos && m.find("E") != std::string::npos){

			m = m.erase(m.find("N"), 1);
			m = m.erase(m.find("E"), 1);
			m = m.erase(m.find("O"), 1);
			myfile << "1";
		}*/

		while (m.find("T") != std::string::npos && m.find("W") != std::string::npos && m.find("O") != std::string::npos){

			m = m.erase(m.find("T"), 1);
			m = m.erase(m.find("W"), 1);
			m = m.erase(m.find("O"), 1);
			//myfile << "2";
			n[2] = n[2]++;
		}

		/*while (m.find("E") != std::string::npos && m.find("T") != std::string::npos && m.find("R") != std::string::npos && m.find("H") != std::string::npos){
			string s = m;
			s = s.erase(m.find("E"), 1);
			if (s.find("E") != std::string::npos){

			}
			else{
				break;
			}

			m = m.erase(m.find("T"), 1);
			m = m.erase(m.find("H"), 1);
			m = m.erase(m.find("R"), 1);
			m = m.erase(m.find("E"), 1);
			m = m.erase(m.find("E"), 1);
			myfile << "3";
		}*/

		while (m.find("F") != std::string::npos && m.find("O") != std::string::npos && m.find("U") != std::string::npos && m.find("R") != std::string::npos){

			m = m.erase(m.find("F"), 1);
			m = m.erase(m.find("O"), 1);
			m = m.erase(m.find("U"), 1);
			m = m.erase(m.find("R"), 1);
			/*myfile << "4";*/
			n[4] = n[4]++;
		}

		while (m.find("F") != std::string::npos && m.find("I") != std::string::npos && m.find("V") != std::string::npos && m.find("E") != std::string::npos){

			m = m.erase(m.find("F"), 1);
			m = m.erase(m.find("I"), 1);
			m = m.erase(m.find("V"), 1);
			m = m.erase(m.find("E"), 1);

			/*myfile << "5";*/
			n[5] = n[5]++;
		}

		while (m.find("S") != std::string::npos && m.find("I") != std::string::npos && m.find("X") != std::string::npos){

			m = m.erase(m.find("S"), 1);
			m = m.erase(m.find("I"), 1);
			m = m.erase(m.find("X"), 1);
			
			n[6] = n[6]++;
		}

		while (m.find("S") != std::string::npos && m.find("E") != std::string::npos && m.find("V") != std::string::npos && m.find("N") != std::string::npos){
			string s = m;
			s = s.erase(m.find("E"), 1);
			if (s.find("E") != std::string::npos){

			}
			else{
				break;
			}

			m = m.erase(m.find("S"), 1);
			m = m.erase(m.find("E"), 1);
			m = m.erase(m.find("V"), 1);
			m = m.erase(m.find("E"), 1);
			m = m.erase(m.find("N"), 1);
			n[7] = n[7]++;
		}


		while (m.find("E") != std::string::npos && m.find("I") != std::string::npos && m.find("G") != std::string::npos && m.find("H") != std::string::npos && m.find("T") != std::string::npos){

			m = m.erase(m.find("E"), 1);
			m = m.erase(m.find("I"), 1);
			m = m.erase(m.find("G"), 1);
			m = m.erase(m.find("H"), 1);
			m = m.erase(m.find("T"), 1);
			n[8] = n[8]++;
		}



		while (m.find("N") != std::string::npos && m.find("I") != std::string::npos && m.find("E") != std::string::npos){
			string s = m;
			s = s.erase(m.find("N"), 1);
			if (s.find("N") != std::string::npos){

			}
			else{
				break;
			}

			m = m.erase(m.find("N"), 1);
			m = m.erase(m.find("I"), 1);
			m = m.erase(m.find("N"), 1);
			m = m.erase(m.find("E"), 1);
			n[9] = n[9]++;
		}

		while (m.find("O") != std::string::npos && m.find("N") != std::string::npos && m.find("E") != std::string::npos){
			
			m = m.erase(m.find("O"), 1);
			m = m.erase(m.find("N"), 1);
			m = m.erase(m.find("E"), 1);

			n[1] = n[1]++;
		
		}

		while (m.find("T") != std::string::npos){

			m = m.erase(m.find("T"), 1);
			m = m.erase(m.find("H"), 1);
			m = m.erase(m.find("R"), 1);
			m = m.erase(m.find("E"), 1);
			m = m.erase(m.find("E"), 1);

			n[3] = n[3]++;

		}

		for (int j = 0; j < 10; j++){
			for (int k = 0; k < n[j]; k++){
				myfile << j;
			}
		}
		

		myfile << endl;

	}
	

		system("pause");
}
