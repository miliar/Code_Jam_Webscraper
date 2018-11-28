#include<iostream>
#include<set>

using namespace std;
int main(){
    set<int> first;
    int firstAns, secAns, t, tmp, count, magic;
    cin >> t;
    for (int k=1; k<=t; k++){
        cin >> firstAns;
        count = 0;
        first.clear();
        for(int i=1; i<=4; i++){
            if (i == firstAns){
                for(int j =0; j<4; j++){
                    cin >> tmp;
                    first.insert(tmp);
                }
            
            }
            else{
                for(int j=0; j<4; j++)
                    cin >> tmp;
            }
        }
        cin >> secAns;        
        for(int i=1; i<=4; i++){
            if (i == secAns){
                for(int j =0; j<4; j++){
                    cin >> tmp;
                    if (first.find(tmp) != first.end()){
                        count++;
                        magic = tmp;
                    }
                }
                
            }
            else{
                for(int j=0; j<4; j++)
                    cin >> tmp;
            }

        }
       switch(count){
        case 0: 
            cout << "Case #"<<k<<": "<<"Volunteer cheated!" <<endl;
            break;
        case 1:
            cout << "Case #"<<k<<": "<< magic << endl; 
            break;
        default:
            cout << "Case #"<<k<<": "<<"Bad magician!" << endl;
            break;
       }
    }
    return 0;


}
