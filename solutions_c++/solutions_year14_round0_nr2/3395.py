using namespace std;
#include <fstream>

/* SMALL INPUT SOLUTION */
/*
double TimeForNFarm(int N, double C, double F){
	if (N == 0) return 0;
	return TimeForNFarm(N - 1, C, F) + C / (2 + (N - 1) * F);
}

int main(int argc, char * argv[])
{
	long icase = 0;
	int T = 0;
	double C = 0, F = 0, X = 0;

	std::fstream infile;
	infile.open("C:\\Users\\Nacho\\Desktop\\input.in", ios_base::in);
	std::fstream outfile;
	outfile.open("C:\\Users\\Nacho\\Desktop\\output.txt", ios_base::out);

	if (infile >> T){
		while (icase < T){
			if (infile >> C){
				if (infile >> F){
					if (infile >> X){

						int N = 0;
						double TwithN = X / 2;
						double TnextN = C/2 + X/(2+F);
						
						while (TnextN < TwithN){
							N++;
							TwithN = TnextN;
							TnextN = TimeForNFarm(N + 1, C, F) + X / (2 + (N+1)*F);
						}
						
						if (icase > 0) outfile << endl;

						outfile << "Case #" << icase + 1 << ": " << TwithN;
						
						icase++;
						continue;
					}
				}
			}
		}
	}
}
*/

/* LARGE INPUT SOLUTION  */

int main(int argc, char * argv[])
{
	long icase = 0;
	int T = 0;
	double C = 0, F = 0, X = 0;

	std::fstream infile;
	infile.open("C:\\Users\\Nacho\\Desktop\\input.in", ios_base::in);
	std::fstream outfile;
	outfile.open("C:\\Users\\Nacho\\Desktop\\output.txt", ios_base::out);
	outfile.setf(std::ios::fixed, std::ios::floatfield);
	outfile.precision(7);

	if (infile >> T){
		while (icase < T){
			if (infile >> C){
				if (infile >> F){
					if (infile >> X){

						double aux = (X - C) / C - 2 / F;
						int N = ceil(aux);
						if (N < 0) N = 0;
						int count = N;

						double TimeForNFarm = 0;

						while (count)
						{
							count--;
							TimeForNFarm += C / (2 + count*F);
						}

						double total = TimeForNFarm + X / (2 + N * F);

						if (icase > 0) outfile << endl;
						
						outfile << "Case #" << icase + 1 << ": " << total;

						icase++;
						continue;
					}
				}
			}
		}
	}
}