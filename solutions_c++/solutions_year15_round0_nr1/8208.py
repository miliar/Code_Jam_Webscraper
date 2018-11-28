#include <iostream>
#include <string>

using namespace std;

void run(int icase,  int smax, const string& squeue){

	const char *p_squeue = squeue.c_str();
	int slen = (int) squeue.size();
	int ns0 = p_squeue[0] - '0';
	int nstanding = ns0;
	int nshort = 0;
	for (int i = 1; i < slen; ++i){
		int nsi = p_squeue[i] - '0';
		if (nstanding + nshort < i)
			nshort += i - (nstanding + nshort);
		nstanding += nsi;
	}

	cout << "Case #" << icase + 1 << ": " << nshort << endl;

}

int main(int argc, char* argv[])
{
	int ncase;
	cin >> ncase;
	for (int icase = 0; icase < ncase; ++icase){
		int smax;
		string squeue;
		cin >> smax >> squeue;
		run(icase, smax, squeue);
	}

	return 0;
}

