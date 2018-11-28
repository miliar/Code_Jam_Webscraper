#include <fstream>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

void AddDigits(int n, vector<int> & digits)
{
	//cout << n << "'s digits: " ;
	while (n!=0)
	{
		digits.push_back(n%10);
		//cout << n%10 << ", " ;
		n = n/10;
	}
	//cout << endl;
}

int main(int argc, char** argv)
{
	if (argc!=4)
	{
		cout << "Params: 0 inputFilePath outputFilePath \n"; 
	}

	ifstream inf;
	inf.open(argv[2]);
	ofstream outf;
	outf.open(argv[3]);

	int n=0;
	string line;
	getline(inf,line);
	n = atoi(line.c_str());
	
	for (int i=0; i<n; i++)
	{
		/*if (i%1000==0)
			cout << i << endl;*/
		getline(inf,line);
		int N = atoi(line.c_str());
		outf << "Case #" << i+1 <<": ";

		if (N==0)
			outf << "INSOMNIA\n";
		else
		{
			int ctr=1;
			set<int> seen;
			seen.clear();
			//cout << N ;
			while (seen.size()<10)
			{
				vector<int> justseen;
				AddDigits(ctr*N,justseen);
				//cout << "\n*" << ctr << ":" << ctr*N << " seen has these many digits: " << seen.size() << endl;
				for(auto itr=justseen.cbegin(); itr!=justseen.cend(); ++itr)
					seen.insert(*itr); 
				//cout << "\n*" << ctr << ":" << ctr*N << " seen has these many digits: " << seen.size() << endl;
				ctr++;
			}
			outf << (ctr-1)*N << endl;
		}			

	}	

	outf.close();
	inf.close();
}
