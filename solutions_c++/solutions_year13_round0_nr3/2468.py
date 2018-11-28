#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#define MAX 1.0e14

using namespace std;

bool palin(unsigned long long);
int main(int argc, const char * argv[])
{
    ifstream fin;
    ofstream fout;
    fin.open("C-large-1.in");
    fout.open("C-large-1.out");
    
    vector<unsigned long long> sq;
    unsigned long long i = 1;
    unsigned long long squared;
    do{
        squared = i * i;
        if(palin(squared) && palin(i))
            sq.push_back(squared);
        i++;
    } while(squared < MAX);

    int T;
    unsigned long long A, B;
    fin >> T;
    for(int n = 1; n <= T; n++){
        fin >> A >> B;
        long cnt = count_if(sq.begin(), sq.end(), [A, B](unsigned long long elem){
                                                    return elem >= A && elem <= B;
                                                    });
        fout << "Case #" << n << ": " << cnt << endl;
    }
    
    
    fout.close();
    fin.close();
    return 0;
}

bool palin(unsigned long long sqaured){
    string s = to_string(sqaured);
    string::iterator it;

    while(!s.empty()){
        it = s.end();
        if(s.size() == 1)
            break;
        else if(*(s.begin()) != *(--it))
            return false;
        else{
            s.erase(it);
            s.erase(s.begin());
        }
    }
    return true;
}

