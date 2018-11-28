#include <iostream>
#include <fstream>
#include <cstdlib>
#include <sstream>
#include <iomanip>
#include <cmath>
using namespace std;

void readArray(string line, int n, int* store);

int main()
{
    std::ifstream in("B-small-attempt0.in");
    std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
    std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

    std::ofstream out("out.txt");
    std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

    //ifstream infile("A-large-practice.in");
    //ofstream outfile;
    //outfile.open("out.txt", ofstream::out);
    //string line;

    //number of case
    //getline(infile, line);
    int ncase;
    cin >> ncase;
    //readArray(line, 1, &ncase);
    //cout << ncase;

    //system("pause");

    for(int i = 1; i<= ncase; i++){
        //getline(infile, line);
        double C, F, X;
        cin >> C >> F >> X;
        double answer;
        int fnf;
        //cout << C << ' ' << F << ' ' << X << endl;
        int nf = 0; //number of farm
        int len = max(10.0, floor(10 * ((X-C)*F - 2*C) / (C*F)));
        //cout << len << endl;
        double* time = new double [len];

        for(int nf=0; nf<len; nf++){
            time[nf] = 0;

            for(int round = 0; round <= nf; round ++){
                double top;
                if(round == nf) top = X;
                else top = C;

                double bottom = 2 + F * round;
                time[nf] += top/bottom;
            }
            //cout << nf << ' ' << time[nf] << endl;

            if(nf > 0)
                if(time[nf] >= time[nf-1]){
                    answer = time[nf-1];
                    fnf = nf-1;
                    break;
                }
        }

        //cout.precision(7);

        char c[500];
        sprintf(c, "Case #%d: %.7f\n", i, answer);
        cout << c;
        delete [] time;
        //cout << "Case #" << i << ": "  << answer << endl;
    }

    return 0;
}

//void readArray(string line, int n, int* store)
//{
//    istringstream iss(line);
//    for(int i = 0; i<n; i++){
//        iss >> store[i];
//    }
//}
