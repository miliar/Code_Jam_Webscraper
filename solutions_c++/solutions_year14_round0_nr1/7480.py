#include<iostream>
using namespace std;

int main() {
    int T, ans1, ans2, row[4][4], storedrow[4][4], anscount, card;
    cin >> T;
    for(int i=1;i<=T;++i) {
        anscount=0;
        cin >> ans1;
--ans1;
        for(int j=0;j<4;++j)
                cin >> storedrow[j][0] >> storedrow[j][1] >> storedrow[j][2] >> storedrow[j][3];
        cin >> ans2;
--ans2;
        for(int j=0;j<4;++j)
            cin >> row[j][0] >> row[j][1] >> row[j][2] >> row[j][3];

        for(int k=0;k<4;++k) {
           for(int l=0;l<4;++l) { 
                if(storedrow[ans1][k]==row[ans2][l]){
                    ++anscount;
                    card=storedrow[ans1][k];
                }
            }
        }
    if(anscount==0)
        cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
    else if(anscount==1)
        cout<<"Case #"<<i<<": "<<card<<endl;
    else
        cout<<"Case #"<<i<<": Bad magician!"<<endl;
    }
}
