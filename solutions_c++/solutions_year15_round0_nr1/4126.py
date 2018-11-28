#include <iostream>
#include <string>
using namespace std;

int worker( int key, char* value){
    int helper = 0;
    int sum = 0;
    for(int i = 0; i<= key; i++){
        if( sum< i && value[i]-'0'>0){
            helper+= i-sum;
            sum = i ;
        }
        sum = sum+ value[i]-'0';
    }
    return helper;
}


int main(){
    int testCase;
    cin>>testCase;
    
    for(int i = 0; i< testCase ; i++){
        int indicator ;
        cin>>indicator;
        char* rank = new char[indicator+1];
        cin>>rank;
        cout<<"Case #"<<i+1<<": "<<worker(indicator, rank)<<endl;
    }

}