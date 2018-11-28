#include <iostream>
#include <fstream>
#include <string>
#include <unistd.h>
using namespace std;


/** ******************
 *  PROBLEM
 ** ******************/

class Field {
  public:
    Field(int n, int m) {
        this->n = n;
        this->m = m;
        field = new int[n*m];
    }

    ~Field() { delete [] field;}

    void setPosition(int n, int m, int h) {
        field[(n*this->m)+m] = h;
    }

    int getPosition(int n, int m) {
        return field[(n*this->m)+m];
    }

    bool cut(int minH, int maxH) {
        int testN = minH;
        bool finish = false;
        while ((testN <= maxH) && (!finish)) {
            // Search in the field the lowest value
            int npos, mpos;
            npos = mpos = -1;
            int lowestValue = maxH;
            bool found = false;

            // Find the lowestValue position
            for (int i=0; (i!=n) && (!found); i++) {
                for (int j=0; (j!=m) && (!found); j++) {
                    int value = getPosition(i,j);
                    if (value == testN) {
                        npos = i;
                        mpos = j;
                        found = true;
                    } else if ((value < lowestValue) && (value > testN)) {
                        lowestValue = value;
                    }
                }
            }

            // Found
            if (found) {
                if (!cutPoint(npos, mpos)) return false;
            } else {
                if (testN == lowestValue) {
                    finish = true;
                } else {
                    testN = lowestValue;
                }
            }
        }
        return true;
    }

    void print() {
        cout << "FIELD:" << endl;
        for (int i=0; i!=n; i++) {
            cout << "| ";
            int im = i*m;
            for (int j=0; j!=m; j++) {
                cout << field[im+j] << " ";
            }
            cout << "|" << endl;
        }
    }

  private:
    bool cutPoint(int npos, int mpos) {
        int h = getPosition(npos, mpos);
        bool nposible, mpossible;
        nposible = mpossible = true;

        // try horizontal
        for (int i=0; i!=m; i++) {
            if (getPosition(npos, i) > h) {
                nposible = false;
            }
        }
        if (nposible) {
            deleteRow(npos);
            return true;
        }

        // try vertical
        for (int i=0; i!=n; i++) {
            if (getPosition(i,mpos) > h) {
                mpossible = false;
            }
        }
        if (mpossible) {
            deleteCol(mpos);
            return true;
        }

        // nothing to do here
        return false;
    }

    void deleteRow(int x) {
        for (int i=0; i!=m; i++) {
            setPosition(x,i,-1);
        }
    }
    void deleteCol(int x) {
        for (int i=0; i!=n; i++) {
            setPosition(i,x,-1);
        }
    }


    int* field;
    int n,m,maxH;
};


string solveProblem(ifstream& file) {
    int n, m, h;
    file >> n >> m;

    // setup
    Field *goal = new Field(n, m);
    for(int i=0; i!=n; i++) {
        for(int j=0; j!=m; j++) {
            file >> h;
            goal->setPosition(i,j,h);
        }
    }

    // calculate
    bool result = goal->cut(1,100);
    delete goal;

    //send result
    if (result)
        return "YES";
    else
        return "NO";
}


/** ******************
 *  MAIN PROGRAM
 ** ******************/

int main()
{
    string line;
    ifstream myFile;
    myFile.open("test.txt");
    if (myFile.is_open()) {
        // N Test Cases
        int T;
        myFile >> T;
        for (int caseN  = 0; caseN != T; caseN++) {
            cout << "Case #" << caseN+1 << ": ";
            cout << solveProblem(myFile) << endl;
        }
    } else {
        cout << "Unable to read file." << endl;
    }
    myFile.close();
    return 0;
}

