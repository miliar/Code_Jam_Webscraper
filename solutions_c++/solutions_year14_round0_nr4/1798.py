#include <iostream>
#include <fstream>
#include <iomanip>
#include <list>

#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)<(b)?(b):(a)

using namespace std;

int T;
int N;
ifstream inFile;
ofstream outFile;
std::list <double> nlist;
std::list <double> klist;

int playDWar() {
	int winNaomi = 0;
	bool findAll = false;
	double drit;

	std::list <double> nlistTmp;
	std::list <double> klistTmp;

	nlistTmp.assign (nlist.begin(),nlist.end());
	klistTmp.assign (klist.begin(),klist.end());

	while(nlistTmp.size() > 0) {
		findAll = false;
		
		for (std::list<double>::reverse_iterator rit=nlistTmp.rbegin(); rit!=nlistTmp.rend(); rit) {
			drit = *rit;
			if(klistTmp.back() < drit) {
				winNaomi++;
				nlistTmp.erase(--rit.base());
				klistTmp.pop_back();
				
				if(rit == nlistTmp.rend()) findAll = true;

				break;
			} else {
				nlistTmp.pop_back();
			}
		}

		if(findAll) {
			break;
		}
	}

	return winNaomi;
}

int playWar() {
	int winNaomi = 0;
	std::list <double> nlistTmp;
	std::list <double> klistTmp;

	nlistTmp.assign (nlist.begin(),nlist.end());
	klistTmp.assign (klist.begin(),klist.end());

	// Look down in Naomi's List.
	while(nlistTmp.size() > 0) {
		if(nlistTmp.front() > klistTmp.front()) {
			winNaomi++;
			nlistTmp.pop_front();
			klistTmp.pop_back();
		} else if(nlistTmp.front() == klistTmp.front()) {
			nlistTmp.pop_front();
			klistTmp.pop_front();
		} else {
			std::list<double>::iterator findit;
			// nlistTmp.front 보다는 크고
			for (std::list<double>::iterator it=klistTmp.begin(); it!=klistTmp.end(); ++it) {
				if(nlistTmp.front() < *it) {
					findit = it;
				} else {
					break;
				}
			}			
			nlistTmp.pop_front();
			klistTmp.erase(findit);
		}
	}
	return winNaomi;
}

int compare (const void * a, const void * b)
{
	if(( *(double*)a - *(double*)b ) < 0)
		return 1;
	else
		return 0;
}

int main() {
	inFile.open("D-large.in");
	outFile.open("D-large.out");
	
	inFile >> T;
	for(int i=0;i<T;i++){		
		inFile >> N;
		nlist.clear();
		klist.clear();

		double tmp;
		for(int j=0;j<N;j++) {
			inFile >> tmp;
			nlist.push_back(tmp);
		}
		for(int j=0;j<N;j++) {
			inFile >> tmp;
			klist.push_back(tmp);
		}
		nlist.sort();
		klist.sort();
		nlist.reverse();
		klist.reverse();

		outFile << "Case #" << i+1 << ": ";
		// plyaing DWar
		outFile << playDWar() << " ";
		// playing War		
		outFile << playWar();
		outFile << endl;
	}

	return 0;
}
