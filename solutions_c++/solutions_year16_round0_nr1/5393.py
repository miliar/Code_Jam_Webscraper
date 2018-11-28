#include <iostream>
#include <vector>
//#include <map>
#include <string>
#include <algorithm>
using namespace std;

bool map[10];

void clear(){
    for(int i =0; i<10; i++)
        map[i] = false;
}
bool sleeped(){
    for(int i=0; i<10; i++)
        if(!map[i]) return false;
    return true;
}
void set(int i){
    if(!map[i]) map[i] = true;
}

int main(){
    int NN;
    cin >> NN;
    for(int nn = 1; nn <= NN; nn++){
        int N;
        cin >> N;
        if(N == 0) {
            cout << "Case #" << nn << ": INSOMNIA" << endl;
            continue;
        }
        
        clear();
        int cnt = 1;
        int tmp = N;
        while(true){
            //tmp = N * cnt;
            //cout << "tmp:" << tmp << endl;
            string str = to_string(tmp);
            for(auto c: str)
                set(c-'0');
                
            if(sleeped()) break;
            tmp += N;
        }
        cout << "Case #" << nn << ": " << tmp << endl;
    }
    return 0;
}