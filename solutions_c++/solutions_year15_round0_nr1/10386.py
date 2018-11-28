#include <iostream>
#include <fstream>
using namespace std;

int main(){
    ofstream myfile;
    myfile.open ("answer.out");
    int n;
    cin>>n;
    for(int i = 0; i < n; i++){
        int maxShyness; cin >> maxShyness;
        string peopleList; cin >> peopleList;
        int neededPeople = 0; int nPeople = 0;
        for(int j=0; j<=maxShyness; j++){
            int peopleCount = (peopleList[j]-48);
            if (j>nPeople && peopleCount>0){
                neededPeople+=j-nPeople;
                nPeople+=neededPeople;
            }
            nPeople += peopleCount;
        }
        myfile<<"Case #"<<i+1<<": "<<neededPeople<<endl;
    }
    myfile.close();
    return 0;
}
