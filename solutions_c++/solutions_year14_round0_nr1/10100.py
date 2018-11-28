#include<iostream>

using namespace std;

int main(){
    int no_cases;
    cin>>no_cases;
    for(int p = 1; p <= no_cases; p++){
        int row1, row2, matched;
        bool present[17];
        for(int i = 0; i < 17; i++){
            present[i]=false;
        }
        cin>>row1;
        row1--;
        int temp;
        for(int i=0; i < 4; i++) {
            for(int j = 0; j < 4; j++) {
                cin>>temp;
                if(i==row1){
                    //cout<< temp<<"w";
                    present[temp]=true;
                }
            }
        }

        cin>>row2;
        row2--;
        int counter = 0;
        for(int i=0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                cin>>temp;
                if(i==row2){
                //cout<< temp<<"w";
                    if(present[temp]){
                        matched = temp;
                        counter++;


                        //cout<<temp<<" matched\n";
                    }
                }
            }
        }
        if(counter==0){
            cout<<"Case #"<<p<<": Volunteer cheated!\n";
        }
        else if(counter==1){
            cout<<"Case #"<<p<<": "<<matched<<endl;
        }
        else{
            cout<<"Case #"<<p<<": Bad magician!\n";
        }
    }
}
