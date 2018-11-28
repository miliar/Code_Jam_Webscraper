#include <cassert>
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>


using namespace std;


const string BM = "Bad magician!";
const string VC = "Volunteer cheated!";

int caseNum = 0;

int main(int argc, const char * argv[])
{
    ifstream fis("A-small-attempt1.in.txt");
    ofstream fos("output.txt");
    string line;
    
    int T = 0;
    fis >> T;
    while (T--) {
        unordered_set<int> set;
        vector<int> answers;
        
        int Q = 2;
        while (Q--) {
            int R = 0;
            fis >> R;
            
            int A[16];
            int i = 0;
            for (; i < 16; i++) {
                fis >> A[i];
            }
            
            i = (R-1) *4;
            for (; i < (R * 4); i++) {
                int card = A[i];
                auto ret = set.emplace(A[i]);
                if (!ret.second) answers.emplace_back(card);
            }
        }
        
        if (set.size() == 8) {
            assert(answers.size() == 0);
            fos<< "Case #" << ++caseNum << ": " << VC << endl;
        } else if (answers.size() == 1) {
            assert(set.size() == 7);
            fos<< "Case #" << ++caseNum << ": " << answers[0] << endl;
       } else {
           assert(set.size() <=7);
           assert(answers.size() >=2);
           fos<< "Case #" << ++caseNum << ": " << BM << endl;
       }
    }

    return 0;
}
