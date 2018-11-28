#include<iostream>
#include<fstream>
using namespace std;

int main(){

    ofstream cout("outputLarge.out");
    ifstream cin("A-large.in");

    int t=0;
    cin >> t;
    for(int j=0 ; j<t ; j++){

        int n=0;
        string crowd ="";
        int result=0,sum=0;

        cin >> n;
        cin >> crowd;
        for(int i=0 ; i<crowd.size() ; i++){
            int val = crowd[i]-'0';
            if(sum >= i){
                sum += val;
            }
            else{
                result += i-sum;
                sum += (i-sum)+val;
            }
        }
        cout << "Case #" << j+1 <<": " << result << endl;
    }

}
