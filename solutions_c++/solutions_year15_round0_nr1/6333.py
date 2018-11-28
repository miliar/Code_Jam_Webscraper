#include <iostream>
#include <string>
using namespace std;

int main(){
    int t;
    cin >> t;
    for(int i=0;i<t;i++){
        string s;
        cin >> s;
        cin >> s;
        string::iterator sit;
        int shyness=0;
        int sum=0;
        int invite=0;
        for(sit=s.begin();sit!=s.end();sit++){
            if(shyness>sum){
                invite=invite+shyness-sum;
                sum=sum+shyness-sum;
            }
            sum=sum+((*sit)-'0');
            shyness++;
        }
        cout << "Case #" << i+1 << ": " << invite << endl;
    }
}
