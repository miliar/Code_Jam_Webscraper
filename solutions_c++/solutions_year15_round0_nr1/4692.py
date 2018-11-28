#include <iostream>
#include <fstream>
#include <string>
using namespace std;


int main(){
    FILE  * input;
    string line;
    int space;
    int Smax;
    int sum=0;
    int req=0;
    int cur=0;
    ifstream myfile("A-large.in");
    ofstream myout("result");
    getline(myfile,line);
    int testNums=stoi(line);
    for(int i=1;i<=testNums;i++){
        getline(myfile,line);
        space=line.find_first_of(" ");
        Smax=stoi(line.substr(0,space));
        req=0;
        sum=0;
        sum=stoi((line.substr(space+1,1)));
        for(int j=1;j<=Smax;j++){
            cur=stoi(line.substr(space+1+j,1));
            if(j>sum){
                req+=j-sum;
                sum=j+cur;
            }
            else{
                sum+=cur;
            }
        }
        myout<<"Case #"<<i<<": "<<req<<endl;
    }    
    return 0;
}
