#include <vector>
#include <fstream>
#include <iostream>

#define REP(i, m, n) for (int i=(int)(m); i<(int)(n); ++i)
#define p(_value) cout << " @" << #_value << ":" << _value << endl;
#define pv(_vec) { cout << " @" << #_vec << "--" << endl; REP(_vindex, 0, _vec.size()) cout << _vec[_vindex] << ", "; cout << endl; }

using namespace std;

typedef vector<int> VI;
typedef vector<vector<int> > VVI;

string kResultString[] = {"Blue", "Red", "Both", "Neither"};

void Usage(string cmdName){
    cout << "usage: " << cmdName << " <file_name>" << endl;
}

struct Trial{
    int answer[2];
    vector<vector<int> > board[2];
};

void ParseTrial(ifstream& inputFileStream, Trial& t){
    REP(i, 0, 2){
        inputFileStream >> t.answer[i];
        vector<vector<int> > vv(4, vector<int>(4));

        const int rowNum = 4, colNum = 4;
        REP(rowId, 0, rowNum){
            REP(colId, 0, colNum){
                int value; inputFileStream >> vv[rowId][colId];
                if(!inputFileStream){
                    cerr << "Read row string failed()." << endl;
                    exit(1);
                }
            }
        }
        t.board[i] = vv;
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

void OutputBoard(string annotation, const vector<vector<int> >& board){
    // Output board content.
    cout << annotation << "----" << endl;
    int rSize = board.size();
    int cSize = board[0].size();
    REP(r, 0, rSize){
        REP(c, 0, cSize){
            cout << board[r][c] << ", ";
        }
        cout << endl;
    }
}

void OutputBoard(string annotation, const vector<string>& board){
    // Output board content.
    cout << annotation << "----" << endl;
    for(string row : board){
        cout << row << endl;
    }    
}

void OutputBoards(vector<vector<string> >& boards, vector<int>& ks, string outFileName = ""){
    ofstream outputFileStream(outFileName);
    ostream& out = (outputFileStream.good()) ? outputFileStream : cout;
    
    // Ouput first line. # of testCases.
    out << boards.size() << endl;

    // Output each board info.
    for(int boardId=0; boardId<boards.size(); ++ boardId){
        int k = ks[boardId];
        vector<string>& board = boards[boardId];

        // Output board size and K.
        out << board.size() << " " << k << endl;

        // Output board content.
        for(string row : board){
            out << row << endl;
        }
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

string SolveTrial(const Trial& t){
    vector<int> cand[2];    
    REP(i, 0, 2){
        int ans =  t.answer[i];
        const VVI& b = t.board[i];
        cand[i] = b[ans-1];

//        p(ans);
//        OutputBoard(to_string(i), b);
    }
    
    int same = 0;
    int value = 0;
    REP(i, 0, 4){
        REP(j, 0, 4){
            if(cand[0][i] == cand[1][j]){
                ++same; 
                value = cand[0][i];
            }
        }
    }

//    p(same);

    if(same == 0) return "Volunteer cheated!";
    if(same >= 2) return "Bad magician!";
    return to_string(value);
}

int main(int argc, char** argv){
    string inputFileName;
    if(argc != 2){
        inputFileName = "A-small-attempt2.in";
    }else{
        inputFileName = argv[1];
    }

    vector<Trial> trials;
    ParseProblemFile(inputFileName, trials);

    vector<string> ans;
    for(Trial t : trials){
        ans.push_back(SolveTrial(t));
    }
    
    OutputResult(ans);

    return 0;
}

