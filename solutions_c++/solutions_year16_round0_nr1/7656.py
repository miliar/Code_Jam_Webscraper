#include <istream>
#include <iostream>
#include <vector>
using namespace std;

void calculate(int t){
    int N;
    cin >> N;
    
    vector<bool> arr(10, false);
    int count = 0;
    int out = N;
    while(N){
        int p = out;
        while(p){
            if(!arr[p%10]){
                count++;
                if(count == 10)
                    break;
                arr[p%10] = true;
            }
            p = p/10;
        }
        if(count == 10)
            break;
        out += N;
    }
    if(N == 0)
        cout << "Case #" << t+1 << ": INSOMNIA" << endl;
    else
        cout << "Case #" << t+1 << ": " << out << endl;
}

int main(){
    int T;
    cin>>T;
    for(int t = 0; t < T; t++){
        calculate(t);
    }
}