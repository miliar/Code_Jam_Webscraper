#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

vector<string> results;
int Arr[100000];
int N = 0;
int sum = 0;
map<int,int> m;

struct testcase{

    int id;
    int N;
};

void swapAt(int idx){

    int num_idx = Arr[idx];
    Arr[idx] = Arr[idx+1];
    Arr[idx+1] = num_idx;
}

std::string trim(std::string const& str){

    if(str.empty())
        return str;

    std::size_t firstScan = str.find_first_not_of(' ');
    std::size_t first = firstScan == std::string::npos ? str.length() : firstScan;
    std::size_t last = str.find_last_not_of(' ');

    return str.substr(first, last-first+1);
}

void printResult(int round, string res){

    cout << "Case #" << round << ": " << res << endl;
}

int findMax(){

    int min = 0;
    int idx = -1;

    for(int i = 0; i < N; i++){

        if(Arr[i]>min){

            min = Arr[i];
            idx = i;
        }
    }

    return idx;
}

void solveTestcase(testcase &tc){

    N = tc.N;

    vector<string> instructions;

    while(sum != 0){

        int idx = findMax();
        char c = idx+'0'+17;
        Arr[idx] = Arr[idx]-1;

        if(sum>2){

            if(!instructions.empty() && instructions[instructions.size()-1].size() == 1)
                instructions[instructions.size()-1] += c;
            else{

                string instr_step;
                instr_step += c;

                instructions.push_back(instr_step);
            }

        }else if(sum == 2){

            string instr_step;
            instr_step += c;

            instructions.push_back(instr_step);

        }else
            instructions[instructions.size()-1] += c;


        sum--;
    }




    string instr;
    for(int i = 0; i < instructions.size(); i++){

        instr += instructions[i] + ' ';
    }

    instr = instr.substr(0,instr.find_last_not_of(' ')+1);

    results.push_back(instr);
}


void getInput(){

    string line;

    int a_size = 0;
    int N = 0;
    testcase tc;

//    ifstream myfile ("A-small-attempt.in");
    ifstream myfile ("A-large-attempt.in");

    if (myfile.is_open())
    {
        while ( getline (myfile,line) )
        {
            if (line.empty()) {

                break;
            }

            if (line.empty()) {

                break;
            }

            if(!a_size){

                a_size = stoi(line);

            }else if(N == 0){

                N = stoi(line);
                tc.N = N;

            }else {

                // Decompose statement into multiple values
                int previdx = 0;
                int idx = line.find(' ');
                int c = 0;
                if(idx == string::npos){

                    Arr[c++] = stoul(line.substr(previdx));

                }else{

                    while( idx != std::string::npos ) {

                        Arr[c++] = stoul(line.substr(previdx,idx));
                        sum += Arr[c-1];

                        previdx = idx + 1;

                        idx = line.find(' ',previdx);
                    }

                    Arr[c++] = stoul(line.substr(previdx));
                    sum += Arr[c-1];

                    int s = sum;

                    solveTestcase(tc);

                    N = 0;

                    if(a_size == results.size())
                        break;
                }
            }
        }

        myfile.close();
    }
}

int main() {

    std::ofstream out("Problem1.out");
    std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

    getInput();

    for(int k = 0; k < results.size(); k++)
        printResult(k+1,results[k]);

    return 0;
}
