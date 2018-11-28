using namespace std;
#include <fstream>

int isPowerOfTwo(unsigned int n){
	int count = 0;
	unsigned int it = 1;
	while (it){
		if (n & it) count++;
		if (count == 2) return 0;
		it = it << 1;
	}
	return 1;
}

int bitPosition(unsigned int n){

	int i = 1;
	while (n >> i)
	{
		i++;
	}
	return i;

}




int main(int argc, char * argv[])
{
	long icase = 0;
	int T = 0;
	int N = 0;
	int P = 0; int Q = 0;

	std::fstream infile;
	infile.open("C:\\Users\\Nacho\\Desktop\\input.in", ios_base::in);
	std::fstream outfile;
	outfile.open("C:\\Users\\Nacho\\Desktop\\output.txt", ios_base::out);

	if (infile >> T){
		while (icase < T){

			infile >> P;
			infile >> Q;

			if (!isPowerOfTwo(Q)){

				if (icase > 0) outfile << endl;

				outfile << "Case #" << icase + 1 << ": impossible";

			}
			else
			{
				int num = P - P % 2;
				int denom = Q;

				int i = 1;

				while (P < Q / i){
					i *= 2;
				}

				if (icase > 0) outfile << endl;

				outfile << "Case #" << icase + 1 << ": " << bitPosition(i) - 1;

				//if (num){
				//	outfile << "Case #" << icase + 1 << ": " << bitPosition(denom / num)-1;
				//}
				//else
				//{
				//	outfile << "Case #" << icase + 1 << ": " << bitPosition(denom)-1;
				//}


			}



			icase++;
			continue;

		}
	}
}