#include <vector>
#include <fstream>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <math.h>
#include <float.h>

#define REP(i, m, n) for (int i=(int)(m); i<(int)(n); ++i)
#define p(_value) cout << " @" << #_value << ":" << _value << endl;
#define pv(_vec) { cout << " @" << #_vec << "--" << endl; REP(_vindex, 0, _vec.size()) cout << _vec[_vindex] << ", "; cout << endl; }

using namespace std;

typedef vector<int> VI;
typedef vector<vector<int> > VVI;

#define MYDEBUG 1

struct Trial{
    double c, x, f;
};

void ParseTrial(ifstream& inputFileStream, Trial& t){
    
    inputFileStream >> t.c >> t.f >> t.x;
    if(!inputFileStream){
        cerr << "Read row string failed()." << endl;
        exit(1);
    }
}

void ParseProblemFile(string inputFileName, vector<Trial>& trials){
    // Open input file.
    ifstream inputFileStream(inputFileName, ios::in);
    if(!inputFileStream){
        cerr << "can not open file (" << inputFileName << ")." << endl;
        exit(1);
    }

    // Read the number of test case.
    int testCaseNum;
    inputFileStream >> testCaseNum;

    // Read all the input
    REP(testCaseId, 0, testCaseNum){
        Trial t;
        ParseTrial(inputFileStream, t);
        trials.push_back(t);
    }
}

void OutputResult(ostream& out, int caseNum, string s){
    out << "Case #" << caseNum << ":" << " " << s << endl;
}

void OutputResult(vector<string> ans){
    int i=0;
    for(string s : ans){
        OutputResult(std::cout, ++i, s);
    }
}

string to_string_with_precision(double value){
    ostringstream oss;
    oss << setprecision(7) << fixed << value;
    return oss.str();
}

string SolveTrial(const Trial& t){

    int maxPattern = ceil(t.x/t.c);
    double minTime = DBL_MAX -1;
    
    bool isDown = false;
    for(int p=0; p<maxPattern; ++p){
        double c = t.c, f=t.f, x=t.x;
        double rate = 2.0l;
        double time = 0.0l;

        for(int i=0; i<=p; ++i){
            if(i==p){
                time += x/rate;
            }else{
                time += c/rate;
                rate += f;
            }
        }

        if(minTime > time){
            minTime = time;
        }else{
#if MYDEBUG
            cout << "break!" << endl;
#endif
            // Once time value increases, it never goes down.
            break;
        }
    }

    return to_string_with_precision(minTime);
}

int main(int argc, char** argv){
    string inputFileName;
    if(argc != 2){
        inputFileName = "B-large.in";
    }else{
        inputFileName = argv[1];
    }

    vector<Trial> trials;
    ParseProblemFile(inputFileName, trials);

    vector<string> ans;
    for(Trial t : trials){
#if MYDEBUG
        static int m = 0;
        cout << ++m << endl;
#endif

        ans.push_back(SolveTrial(t));
    }
    
    OutputResult(ans);

    return 0;
}

