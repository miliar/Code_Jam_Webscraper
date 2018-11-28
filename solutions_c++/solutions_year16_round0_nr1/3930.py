#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;



int main (int argc, const char * argv[]) {
    fstream fout;
    fout.open("sol.txt", ios::out);
    ifstream fin;
    fin.open(argv[1],ios::in|ios::binary);
    string word;
    //input by file
    if (fin.is_open()){//file opened
        fin>>word;
        int case_num = stoi(word);//how many cases
        for (int i = 0; i < case_num; i++) {
            fin>>word;
            int num = stoi(word);//begin num
            if (num == 0) {
                fout<<"Case #"<<i + 1<<": ";
                fout<<"INSOMNIA"<<endl;
                continue;
            }
            vector<bool> r(10,false);
            int temp = num;
            for (int j = 2; ; j++) {
                while (temp != 0) {
                    r[temp%10] = true;
                    temp = temp/10;
                }
                if (r[0] && r[1] && r[2] && r[3] && r[4] && r[5] && r[6] && r[7] && r[8] && r[9]) {//all true
                    fout<<"Case #"<<i + 1<<": ";
                    fout<<num * (j-1)<<endl;
                    break;
                }
                else{
                    temp = num * j;
                }
            }
        }
    }
    else{
        cout<<"opend fail"<<endl;
    }
    
    
    return 0;
}