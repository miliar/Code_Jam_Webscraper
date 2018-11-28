#include <fstream>
#include <vector>
#include <map>
#include <math.h>
using namespace std;

long toBase(const string& bin, int base, int power);
// convert binary string to a base
long toBase(const string& bin, int base) {
    return toBase(bin, base, 0);
}

long toBase(const string& bin, int base, int power) {
    if (bin.empty())
        return 0;
    
    return atoi(&bin.back()) * pow(base, power) + toBase(bin.substr(0, bin.size()-1), base, power+1);
}

long getDivisor(long n) {
    if (n % 2 == 0)
        return 2;
    
    for (long i = 3; i*i < n; i += 2)
        if (n % i == 0)
            return i;
    
    return -1;
}

void combine(string curr, int n, map<string, vector<long>>& bins, int numBins) {
    // found some valid bins
    if (bins.size() == numBins)
        return;
    
    // finished constructing a binary
    if (n == 0) {
        string bin = "1" + curr + "1";
        for (int i = 2; i <= 10; ++i) {
            long converted = toBase(bin, i);
            
            long div = getDivisor(converted);
            // detected a prime, erase this binary from bins and return
            if (div == -1) {
                bins.erase(bin);
                return;
            }
            
            // store base represenation of this number
            bins[bin].push_back(div);
        }
        
        return;
    }

    combine(curr + '0', n-1, bins, numBins);
    combine(curr + '1', n-1, bins, numBins);
}

void findBins(map<string, vector<long>>& bins, int N, int J) {
    // N-2 b/c 1 is prepended and appended to the binary string
    combine("", N-2, bins, J);
}

void readInput(const string& inFile, const string& outFile) {
    ifstream in(inFile.c_str());
    if (!in)
        throw exception();
    
    FILE* pFile = fopen(outFile.c_str(), "w");
    if (!pFile)
        throw exception();
    
    int T, N, J;
    in >> T >> N >> J;
    
    map<string, vector<long>> bins;
    findBins(bins, N, J);
    
    // output
    fprintf(pFile, "Case #1:\n");
    for (auto itr = bins.begin(); itr != bins.end(); ++itr) {
        fprintf(pFile, "%s", itr->first.c_str());
        for (int i : itr->second)
                fprintf(pFile, " %i", i);
        fprintf(pFile, "\n");
    }
}


int main(int argc, const char * argv[]) {
    readInput("/Users/elvirakalviste/Desktop/CodeJam2016/CodeJam2016/c_small.in",
              "/Users/elvirakalviste/Desktop/CodeJam2016/CodeJam2016/c_small.out");
    
    return 0;
}
