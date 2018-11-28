#include <iostream>

using namespace std;

int main(){
    int t, a1, a2, temp, c, n;
    cin>>t;
    int cards1[4] = {0,0,0,0};
    int cards2[4] = {0,0,0,0};
    for(int k=1; k<=t; k++){
        c=0;
        cin>>a1;
        for(int i = 0; i<16; i++){
            cin>>temp;
            if (i >= (a1-1)*4 && i<a1*4){
                cards1[i-(a1-1)*4] = temp;
            }
        }        

        cin>>a2;
        for(int i = 0; i<16; i++){
            cin>>temp;
            if (i >= (a2-1)*4 && i<a2*4){
                cards2[i-(a2-1)*4] = temp;
            }
        }        

        for(int i = 0 ; i<4; i++){
            for(int j = 0 ; j<4; j++){
                if (cards1[i] == cards2[j]){
                    c++;
                    n = cards1[i];
                }   
            }
        }
        if (c == 1){
            cout<<"Case #"<<k << ": "<<n <<"\n";
        }
        else if(c == 0){
            cout<<"Case #"<<k << ": Volunteer cheated!" <<"\n";
        }
        else{
            cout<<"Case #"<<k << ": Bad magician!"<<"\n";
        }

    }
    return 0;
}
