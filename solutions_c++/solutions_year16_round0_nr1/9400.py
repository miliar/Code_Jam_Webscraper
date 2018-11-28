#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

void print(int digs){
    cout << "digs: ";
    vector<int> v;
    while(digs){
        if(digs % 2){
            v.push_back(1);
        }
        else{
            v.push_back(0);
        }
        digs = digs>>1;
    }
    for(int i = v.size()-1; i>=0; i--){
        cout << v[i];
    }
    cout << endl;
}
void addDigs(int &digs, int N){
    while(N){
        digs = digs | (1 << ((N % 10)));
        N = N/10;

    }
}



int main(){
    int T;
    cin >> T;
    int CN = 0;
    while(T--){
        ++CN;
        int N;
        cin >> N;
        N = abs(N);
        if(N==0){
            cout << "Case #" << CN << ": INSOMNIA" << endl;
        }
        else{
            int digs = 0;
            int i = 1;
            int nextN;
            while(digs != (1 << 10)-1){
                nextN = N*i;
                addDigs(digs, nextN);
                i++;
            }
            cout << "Case #" << CN << ": "<< nextN << endl;
        }
    }
}
