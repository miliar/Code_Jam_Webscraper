#include<iostream>
#include<fstream>

using namespace std;

class Bullseye {
  private:
    long long t, in_r[6000], in_t[6000], out[6000];
  public:
    void readFromFile(char* fileName) {
        ifstream fin;
        fin.open(fileName);
        fin >> t;
        for(int i=0; i<t; i++) fin >> in_r[i] >> in_t[i];
        fin.close();
    }

    void writeToFile(char* fileName) {
        ofstream fout;
        fout.open(fileName);
        for(int i=0; i<t; i++) fout << "Case #" << i+1 << ": " << out[i] << endl;
        fout.close();
    }

    void compute() {
	for(int i=0; i<t; i++) {
	    out[i]=0;
	    long long r=in_r[i], t=in_t[i];
	    while(true) {
		t=t-(r+r+1);
		if(t<0) break;
		out[i]++;
		r+=2;
	    }
	}
    }
};
int main(int argc, char* argv[]) {
    Bullseye s;
    cout << "Reading input file..." << endl;
    s.readFromFile(argv[1]);
    cout << "computing solution input file..." << endl;
    s.compute();
    cout << "Writing output file..." << endl;
    s.writeToFile(argv[2]);
    return 0;
}
