#include<iostream>
#include<fstream>
#include<string>
#include<sstream>

using namespace std;


int f(string line){
    istringstream sin(line);
    int smax; string audi;
    sin>>smax>>audi;
    if(smax == 0){
        return 0;
    }

    int need = 0;

    int sum = 0;
    for(int i = 0; i < smax + 1 ; i ++){
        int t = audi[i] - '0';
        if(t == 0){
            continue;
        }


        if(i > 0){
            if(sum < i){
                int cn = i - sum;
                need += cn;
                sum += cn;
                
            }
        } 

        sum += t ;

    }
    return need;

}
int main(){
    ifstream cin("A-large.in");
    int t;
    cin >> t;
    string line;
    getline(cin,line);
    for(int i =0 ; i < t; i++){
        getline(cin, line);
        int res = f(line);
        cout << "Case #"<<i+1<<": "<<res<<"\n";
    }

}
