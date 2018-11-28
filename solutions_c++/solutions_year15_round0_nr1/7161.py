#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>

using namespace std;

int main(int argc, char const *argv[])
{
	
	string line;
	ifstream myfile ("A-large.in");
	ofstream outfile ("A-large.out");


	if (myfile.is_open())
	{
		
		while(! myfile.eof()){

			getline(myfile, line);

			int numTest;
			numTest = atoi(line.c_str());


			for (int j = 0; j < numTest; ++j){

				int tamanho;

				myfile >> tamanho;

				char s[tamanho + 1];

				myfile >> s;


				int S[tamanho + 1];
				int sentados = 0;


				for (int i = 0; i < tamanho+1; i++)
				{
					S[i] = s[i] - '0';
					sentados+= S[i];

				}

				int emPe = 0;
				int amigos = 0;

				for (int i = 0; i <= tamanho; i++)
				{
					if ( i <= emPe )
					{
						emPe += S[i];

						// cout << "ak : " << emPe << endl;

					
					}else{
						amigos++;
						emPe++;
						emPe += S[i];

						// cout << "akkk : " << emPe << endl;


					}
				}


				outfile << "Case #" << j+1 << ": " << amigos << endl;
				// cout << "empe #" << j+1 << ": " << emPe << endl;

			}


			
		}
		

	}
	else{
	}


	myfile.close();
	outfile.close();


	return 0;
}