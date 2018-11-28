//codejam 2016 Revenge of the Pancakes
#include <iostream>
#include <string>
using namespace std;

int main(){
    int testCase;
    cin>>testCase;
    for (int i=0; i<testCase; i++){
        string pancakes;
        cin>>pancakes;
        int jmlPancakes = pancakes.length();
        int jmlAction = 0;
        for (int j=jmlPancakes-1; j>=0; j--){
            if ((pancakes[j]=='-')&&(jmlAction%2==0)){
                jmlAction+=1;
            } else if ((pancakes[j]=='+')&&(jmlAction%2==1)){
                jmlAction+=1;
            }
        }
        cout<<"Case #"<<i+1<<": "<<jmlAction<<endl;
    }
}
