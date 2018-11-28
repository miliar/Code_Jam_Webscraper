using namespace std;
#include <fstream>

int cmpfunc(const void * a, const void * b)
{
	double aa = *(double*) a;
	double bb = *(double*) b;
	if (aa > bb) return 1;
	if (aa < bb) return -1;
	return 0;
	//return (int)(*(double*) a - *(double*) b);
}

int main(int argc, char * argv[])
{
	long icase = 0;
	int T = 0, N = 0;
	double * ken;
	double * naomi;
	int playingwar = 0;
	int playingdeceitful = 0;

	std::fstream infile;
	infile.open("C:\\Users\\Nacho\\Desktop\\input.in", ios_base::in);
	std::fstream outfile;
	outfile.open("C:\\Users\\Nacho\\Desktop\\output.txt", ios_base::out);

	if (infile >> T){
		while (icase < T){
			if (infile >> N){
		
				naomi = new double[N];

				for (int i = 0; i < N; i++) infile >> naomi[i];

				qsort(naomi, N, sizeof(double), cmpfunc);

				ken = new double[N];

				for (int i = 0; i < N; i++) infile >> ken[i];

				qsort(ken, N, sizeof(double), cmpfunc);

				/* PLAYING WAR */

				//int j = 0;

				/* Naomi's optimal strategy will be */

				/*for (int i = 0; i < N; i++)
				{
					while (j < N && naomi[i] > ken[j]){
						j++;
					}
					
					if (j == N) {
						playingwar = N - i;
						break;
					}

					j++; 

				}*/

				int kenlowest = 0;
				int kenhighest = N - 1;

				for (int i = N - 1; i >= 0; i--){
					if (naomi[i] > ken[kenhighest]){
						kenlowest++;
					}
					else {
						kenhighest--;
					}
				}

				playingwar = kenlowest;

				/* PLAYING DECEITFUL WAR */

				playingdeceitful = 0;

				int j = 0;

				/* Naomi's strategy will be making ken play his lowest card because he thinks none of his cards can
				win against the one Naomi has played. Naomi can only do this if her lowest card can win against ken's lowest*/

				for (int i = 0; i < N; i++){
					if (naomi[i] > ken[j]){
						playingdeceitful++;
						j++;
					}
				}


				if (icase > 0) outfile << endl;

				outfile << "Case #" << icase + 1 << ": " << playingdeceitful << " " << playingwar;

				icase++;
				continue;
			}
		}
	}
}