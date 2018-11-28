using namespace std;
#include <fstream>
#include <string>

int main(int argc, char * argv[])
{
	long icase = 0;
	int T = 0, line = 0, skip = 0;
	int count = 0, guess = 0;
	int aux = 0;
	int * card = new int[4];
	string foo;

	std::fstream infile;
	infile.open("C:\\Users\\Nacho\\Desktop\\input.in", ios_base::in);
	std::fstream outfile;
	outfile.open("C:\\Users\\Nacho\\Desktop\\output.txt", ios_base::out);

	if (infile >> T){
		while (icase < T){
			if (infile >> line){
				
				skip = line - 1;
				
				while (skip){
					if (infile.peek() == '\n') infile.get();
					getline(infile, foo);
					skip--;
				}

				for (int i = 0; i < 4; i++) infile >> card[i];

				skip = 4 - line;

				while (skip > 0){
					if (infile.peek() == '\n') infile.get();
					getline(infile, foo);
					skip--;
				}

				if (infile >> line){
					skip = line - 1;

					while (skip){
						if (infile.peek() == '\n') infile.get();
						getline(infile, foo);
						skip--;
					}

					count = 0;

					for (int i = 0; i < 4; i++){
						infile >> aux;
						for (int j = 0; j < 4; j++){
							if (card[j] == aux){
								count++;
								guess = aux;
							}
						}
					}

					skip = 4 - line;

					while (skip > 0){
						if (infile.peek() == '\n') infile.get();
						getline(infile, foo);
						skip--;
					}

					if (icase > 0) outfile << endl;

					if (count == 0){
						outfile << "Case #" << icase + 1 << ": Volunteer cheated!";
					}
					else if (count == 1) {
						outfile << "Case #" << icase + 1 << ": " << guess;
					} 
					else {
						outfile << "Case #" << icase + 1 << ": Bad magician!";
					}

					icase++;
					continue;
				}
			}
		}
	}
}