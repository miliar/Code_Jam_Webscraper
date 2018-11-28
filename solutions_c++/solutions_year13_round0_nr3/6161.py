#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;

class FairAndSquare {
  private:
    int t, a[100], b[100], output[100];
  public:
    void readFromFile(char* fileName) {
        ifstream in;
        in.open(fileName);
        in >> t;
        for(int i=0; i<t; i++) in >> a[i] >> b[i];
        in.close();
    }

    void writeToFile(char* fileName) {
        ofstream out;
        out.open(fileName);
        for(int i=0; i<t; i++) out << "Case #" << i+1 << ": " << output[i] << endl;
        out.close();
    }

    int reverseInt(int num) {
        int inv = 0;
        while (num>0)
        {
            inv = inv * 10 + (num%10);
            num = num / 10;
        }
        return inv;
    }

    void compute() { for(int k=0; k<t; k++) {
	int cont = 0;
        for(int i=a[k]; i<=b[k]; i++) {
            if(i-reverseInt(i) != 0) continue;
            int s=(int)sqrt(i);
            if(s*s != i) continue;
            if(s-reverseInt(s) != 0) continue;
            cont++;
        }
        output[k] = cont;
    }}
};
int main() {
    FairAndSquare a;
    cout << "Reading input file..." << endl;
    a.readFromFile((char*)"C-small-attempt0.in");
    cout << "computing solution input file..." << endl;
    a.compute();
    cout << "Writing output file..." << endl;
    a.writeToFile((char*)"C-small-attempt.out");
    return 0;
}
