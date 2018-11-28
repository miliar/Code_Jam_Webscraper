#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <set>
#include <sstream>
#include <iterator>

using namespace std;

void addSet(set<int> &nset, long long num)
{
    int n;
    while(num!=0){
        n = num%10;
        num /= 10;
        cout << "insert " << n << endl;
        nset.insert(n);
    }
}

int main()
{
    ifstream infile("large.in");
    ofstream outfile("large.txt");
    string line;
    int count;

    // read number of instances
    getline(infile,line);
    count = atoi(line.c_str());
    cout << "T = " << count << endl;
    int N;
    long long newN;
    //streamstring ss;
    set<int> numset;
    //vector<string> productPrice;

    for (int i=0; i<count; i++)
    {
        numset.clear();
        //read buget for each case
        getline(infile, line);
        N = atoi(line.c_str());
        cout << endl << "N = " << N << endl;
        addSet(numset, N);
        if (numset.size()>=10) {
                outfile << "Case #" << i+1 <<": " << newN << endl;
                cout << "Case #" << i <<": " << newN << endl;
                continue;
        }

        for(int m=2;;m++) {
            newN = m*N;
            if (newN==N){
                outfile << "Case #" << i+1 <<": INSOMNIA" << endl;
                cout << "Case #" << count <<": INSOMNIA" << endl;
                break;
            }
            cout << "newN = " << N << "*" << m << "=" << newN << endl;

            addSet(numset, newN);
            if (numset.size()>=10) {
                outfile << "Case #" << i+1 <<": " << newN << endl;
                cout << "Case #" << count <<": " << newN << endl;
                break;
            }
        }
    }

    infile.close();
    outfile.close();
    return 0;
}



