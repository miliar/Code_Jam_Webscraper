#include <iostream>
#include <cstring>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;
/*******


********/

int main(void){

    //ifstream fin("A-large.in");
    ifstream fin("A-small-attempt1.in");
    //ifstream fin("case.txt");
    ofstream fout("A_small.out");
    int T;
    string st;
    getline(fin,st);
    stringstream ss(st);
    ss >> T;

    //cout << T << endl;
    for(int t = 0 ; t < T ; t++){
        int num = 0;
        //int n;
        int p,q;
        bool pos = false;
        string line,ps="",qs="";
        fin >> line;
        bool change = false;
        for(int i = 0 ; i < line.length(); i++){
            if(line[i] == '/'){
                change = true;
                continue;
            }
            else{
                if(change){
                    qs += line[i];
                }
                else
                    ps += line[i];
            }
        }
        ss.str(ps);
        ss.clear();
        ss >> p;

        ss.str(qs);
        ss.clear();
        ss >> q;

        //cout << ps << " " << qs << " " << endl;
        cout << p << " " << q << " " << endl;

        int pow[] ={512,256,128,64,32,16,8,4,2};
        for(int i = 0 ; i < 9 ; i++){
            if(q == pow[i]){
                pos = true;
                break;
            }
        }
        if(q == 1)
            pos = true;
        if(pos){
            for(int i = 0 ; i < 40 ; i++){
                p = p*2;
                if(p >= q){
                    num = i+1;
                    break;
                }
            }
        }

        if(pos){
            fout << "Case #" << t+1 << ": " << num << "\n";
            cout << "Case #" << t+1 << ": " << num << "\n";
        }
        else{
            fout << "Case #" << t+1 << ": " << "impossible\n";
            cout << "Case #" << t+1 << ": " << "impossible\n";
        }



    }

    fin.close();
    fout.close();

    return 0;
}

