//i deleted the start of the entry to make it work, sorry!
#include <fstream>
#include <iostream>

using namespace std;

int main(){

    int cases,goal,peopleRequired=0,current=0,surplus=0,counter=0,caseNo=1;
    char ch;
    fstream fin("small.txt", fstream::in);
    ofstream myfile;
    myfile.open ("out.txt");
    while (fin >> noskipws >> ch) {
        //cout << ch << endl;
        if (counter == 0){
            cases = ch - '0';
        }
        if (counter == 2){
            goal = ch - '0';
        }
        if (counter > 3){
            if ((ch - '0') == 0){
                if (surplus == 0){
                    peopleRequired += 1;
                }
                else{
                    surplus--;
                }
            }
            else if ((ch - '0') > 1){
                surplus+=(ch - '0')-1;
            }
        }
        if (counter == goal + 4){
            myfile << "Case #" << caseNo << ": " << peopleRequired  << endl;
            caseNo++;
            counter = 0;
            peopleRequired = 0;
            surplus = 0;
            current =0;
            goal = 0;
            int cases,goal,peopleRequired=0,current=0,surplus=0,counter=0,caseNo=1;
        }
        counter++;
    }
    cout << counter << endl;
    return 0;
}
