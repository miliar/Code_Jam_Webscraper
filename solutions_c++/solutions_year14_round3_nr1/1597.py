#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#define eps 1.0e-100
using namespace std;

int main() {
	string basePath = "/Users/litiantian/Desktop/Conan/temp/data/2014_1C";
	string baseName = "A-large";
	string inFile = basePath + "/" + baseName + ".in";
	string outFile = basePath + "/" + baseName + "-out.txt";
	ifstream ifs(inFile.c_str(), ifstream::in);
	ofstream ofs(outFile.c_str(), ofstream::out);

	int numTest(0), idxTest(1);
	ifs >> numTest;

	while(idxTest <= numTest) {
		int minGen(0);
		string frac;
		ifs >> frac;

		std::size_t pos = frac.find('/');
		string strP = frac.substr(0, pos);
		string strQ = frac.substr(pos+1, frac.length());
        //long int P = std::stoi(strP);
        //long int Q = std::stoi(strQ);
        double P = atof(strP.c_str());
        double Q = atof(strQ.c_str());
        double tmpR = double(P)/double(Q);
        long int tmpQ = (long int)(Q);

        if (tmpQ % 2 == 0) {
            double tmp(0.5);
            vector<int> tmpV;
            int k = 1;

            while(k <= 40) {
                int d = tmpR/tmp;
                tmpR -= double(d)*tmp;
                if (d)
                    tmpV.push_back(k);

                if (tmpR < eps)
                    break;

                tmp *= 0.5;
                k++;
            }

            if (k <= 40 && !tmpV.empty())
                minGen = tmpV[0];
        }

		if (minGen)
			ofs << "Case #" << idxTest << ": " << minGen << endl;
		else
			ofs << "Case #" << idxTest << ": " << "impossible" << endl;

		++idxTest;
	}

	ifs.close();
	ofs.close();
	getchar();
	return 0;
}
