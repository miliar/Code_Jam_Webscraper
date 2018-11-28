#include <iostream>
using namespace std;
int main(){
    string Pancakes;
    int n;
    cin >> n;
    for(int i=0;i!=n;i++){
        cin >> Pancakes;
        int counter = 0;
        bool plusTurn = false;
        for(int j=Pancakes.size()-1;j!=-1;j--){
            if(plusTurn){
                if(Pancakes[j] == '+'){
                    counter++;
                    plusTurn = false;
                }
            }
            else{
                if(Pancakes[j] == '-'){
                    counter++;
                    plusTurn = true;
                }
            }
        }
        cout << "Case #" << i+1 << ": " << counter << endl;
    }
    return 0;
}