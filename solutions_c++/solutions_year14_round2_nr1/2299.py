using namespace std;
#include <fstream>


int difference(int a, int b){
	if (a >= b) return a - b;
	return b - a;
}

int main(int argc, char * argv[])
{
	long icase = 0;
	int T, N, L = 0;

	std::fstream infile;
	infile.open("C:\\Users\\Nacho\\Desktop\\input.in", ios_base::in);
	std::fstream outfile;
	outfile.open("C:\\Users\\Nacho\\Desktop\\output.txt", ios_base::out);

	if (infile >> T){
		while (icase < T){
			if (infile >> N){
				
				if (N = 2){
					char * str1 = new char[101];
					char * str2 = new char[101];
					if (infile.peek() == '\n') infile.get();
					infile.getline(str1, 101);
					if (infile.peek() == '\n') infile.get();
					infile.getline(str2, 101);

					int i = 0;
					int j = 0;

					int deletes = 0;

					int FeglaWon = 0;

					while (str1[i] != '\0'){

						if (str1[i] != str2[j]){
							FeglaWon = 1;
							break;

						}

						char aux = str1[i];
						int count1 = 0;
						int count2 = 0;

						while (str1[i] == aux){
							count1++;
							i++;
						}

						while (str2[j] == aux){
							count2++;
							j++;
						}

						deletes += difference(count1, count2);

					}

					if (FeglaWon){
						if (icase > 0) outfile << endl;
						outfile << "Case #" << icase + 1 << ": Fegla Won";
					}
					else if (str2[j] != '\0'){
						if (icase > 0) outfile << endl;
						outfile << "Case #" << icase + 1 << ": Fegla Won";
					}
					else
					{
						if (icase > 0) outfile << endl;
						outfile << "Case #" << icase + 1 << ": " << deletes;
					}


				}

				

				//if (icase > 0) outfile << endl;


				//outfile << "Case #" << icase + 1 << ": NOT POSSIBLE";



				icase++;
				continue;
					
			}
		}
	}
}