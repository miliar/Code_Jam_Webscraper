#include <iostream>
#include <fstream>
using namespace std;


int main (){
    ifstream in("Bl.in");
    ofstream out("loutput.txt");
    int testcases;
    in >> testcases;
    int testcasses = testcases;
    char duifagwbecrawenfhds=in.get();
    while (testcasses -->0){
        char pan[1000];
        int i=0;
        do{
            pan[i]=in.get();
            i++;
        } while(pan[i-1]!='\n');
        i=1;
        int resultaat=0;
        while(true){
            if(pan[i]=='\n')break;
            if(pan[i]!=pan[i-1])resultaat++;
            i++;
        }
        resultaat+=(pan[i-1]=='-');
        out<<"Case #"<<testcases-testcasses<<": "<<resultaat<<endl;
    }
    return 0;
}
