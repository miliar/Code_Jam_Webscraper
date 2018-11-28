#if 0
#define _GLIBCXX_DEBUG
const bool dbg = true;
#else
#define NDEBUG
const bool dbg = false;
#endif

#include <cstdlib>
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cmath>
#include <cassert>
#include <list>

using namespace std;

void getInputFile(int argc, char* argv[], ifstream &inputFile)
{
	if (argc != 2) {
		cerr << "Require one argument (input file); exiting ...\n";
		exit(1);
	}
	string filename = argv[1];
	inputFile.exceptions(ifstream::failbit);
	inputFile.open(filename.c_str());
}

void getOutputFile(int argc, char* argv[], ofstream &outputFile)
{
	string filename = argv[1];
	unsigned dotIndex = filename.find_last_of('.');
	if (dotIndex != string::npos)
		filename.erase(dotIndex);
	filename += ".out";
	outputFile.exceptions(ofstream::failbit);
	outputFile.open(filename.c_str());
}

typedef long long ll;

struct Record {
	ll in, out, num;
	Record(ll o, ll e, ll n) : in(o), out(e), num(n) { };
	Record() : in(0), out(0), num(0) { };
};

bool firstLess(const Record& x, const Record& y) { return x.in < y.in; }

void processCase(istream& inputFile, ostream& outputFile)
{
	const ll mod = 1000002013;
	ll numStops, numPairs;
	inputFile >> numStops >> numPairs;
	vector<Record> rec(numPairs);
	for (ll i=0; i<numPairs; ++i) inputFile >> rec[i].in >> rec[i].out >> rec[i].num;

	ll origCost = 0;
	for (ll i=0; i<numPairs; ++i) {
		ll dist = rec[i].out - rec[i].in;
		ll costpp = (dist * (2*numStops-dist+1) / 2) % mod;
		ll cost = (rec[i].num * costpp) % mod;
		origCost = (origCost + cost) % mod;
	}
	if (dbg) cout << "origCost = " << origCost << "\n";

	sort(rec.begin(), rec.end(), firstLess);
	int i=0;
	while (i < numPairs) {
		int j = i+1;
		while (j < numPairs) {
			if (dbg) cout << "comparing " << rec[i].in << " " << rec[i].out << " " << rec[i].num
					<< " with " << rec[j].in << " " << rec[j].out << " " << rec[j].num << "\n";
			if (rec[j].in > rec[i].in && rec[j].in <= rec[i].out && rec[j].out > rec[i].out) {
				if (rec[i].num == rec[j].num) {
					ll outj = rec[j].out;
					rec[j].out = rec[i].out;
					rec[i].out = outj;
				} else if (rec[i].num < rec[j].num) {
					rec.insert(rec.begin()+j+1, Record(rec[j].in, rec[i].out, rec[i].num));
					rec[i].out = rec[j].out;
					rec[j].num -= rec[i].num;
					++numPairs;
				} else {
					rec.insert(rec.begin()+i+1, Record(rec[i].in, rec[j].out, rec[j].num));
					rec[i].num -= rec[j+1].num;
					rec[j+1].out = rec[i].out;
					++numPairs;
				}
				if (dbg) {
					for (int k=0; k<numPairs; ++k) cout << rec[k].in << " " << rec[k].out << " " << rec[k].num << "\n";
					cout << "\n";
				}
			}
			++j;
		}
		++i;
	}

	ll newCost = 0;
	for (ll i=0; i<numPairs; ++i) {
		ll dist = rec[i].out - rec[i].in;
		ll costpp = (dist * (2*numStops-dist+1) / 2) % mod;
		ll cost = (rec[i].num * costpp) % mod;
		newCost = (newCost + cost) % mod;
	}
	if (dbg) cout << "newCost = " << newCost << "\n";

	ll diffCost = (origCost - newCost) % mod;
	if (diffCost < 0) diffCost += mod;
	outputFile << diffCost;
}

int main(int argc, char *argv[])
{
	ifstream inputFile;
	getInputFile(argc, argv, inputFile);
	ofstream outputFile;
	getOutputFile(argc, argv, outputFile);

	int numCases;
	inputFile >> numCases >> ws;
	for (int caseIndex = 0; caseIndex < numCases; ++caseIndex) {
		outputFile << "Case #" << caseIndex+1 << ": ";
		cout << "Case #" << caseIndex+1 << "\n";
		processCase(inputFile, outputFile);
		outputFile << "\n";
	}
}


