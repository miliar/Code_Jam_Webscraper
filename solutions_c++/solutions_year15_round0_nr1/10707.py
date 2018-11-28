#include <iostream>
#include <fstream>
using namespace std;
int sumto(string str,int n){
    int s = 0;
    for(int i=0;i<n;i++) s += (str[i] - '0');
    return s;
}
int main(){
    int T; cin >> T;
    ofstream ofile ("a.sol");
    for(int t=0;t<T;t++){
        int level; cin >> level;
        string people;
        cin >> people;
        int needs = 0;
        for(int i=1;i<level+1;i++){
            if(people[i] != '0' && i > sumto(people,i)){
                needs += i - sumto(people,i);
                people[0] += i - sumto(people,i);
            }
        }
        cout << needs << endl;
        ofile << "Case #" << t+1 << ": " << needs << endl;
    }
}
