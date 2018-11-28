#include <iostream>

using namespace std;
int allNegative=0;

int allpositive(string &cakes){
    int positive=0,negative=0;
    for (int i = 0; i < cakes.length(); i++) {
        if(cakes[i]=='+')
            positive++;
        else if(cakes[i]=='-')
            negative++;
        if(negative!=0 && positive!=0)
                return 0;
    }
    if(negative==cakes.length()){
        allNegative=1;
        return 0;
    }
    return 1;

}

void flipThem(string &cakes){
    for(int i=0;i<cakes.length()-1;i++){
        if(cakes[i]!=cakes[i+1]){
            while(i>=0){
                cakes[i]=cakes[i+1];
                i--;
            }
            return;
        }
    }
}

void answer(int index){
    allNegative=0;
    int flips=0;
    string cakes;
    getline(cin,cakes);
    while(!allpositive(cakes)){
        flips++;
        if(allNegative)
            break;
        flipThem(cakes);
    }
    cout<<"Case #"<<index<<": "<<flips<<endl;
}

int main(int argc, char const *argv[]) {

    int t;
    cin>>t;
    cin.ignore();
    for(int i=1;i<=t;i++)
        answer(i);
    return 0;
}
