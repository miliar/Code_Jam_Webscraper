#include<iostream>

using namespace std;

int main(){

    int first[4][4],second[4][4];
    int row1,row2;

    int t;
    cin>>t;
    for(int i=1;i<=t;i++){
        cin>>row1;
        for(int j=0;j<4;j++)
            for(int k=0;k<4;k++)
                cin>>first[j][k];
        cin>>row2;
        for(int j=0;j<4;j++)
            for(int k=0;k<4;k++)
                cin>>second[j][k];
        int count = 0;
        int value;
        for(int j=0;j<4;j++){
            for(int k=0;k<4;k++){
                if(first[row1-1][j] == second[row2-1][k]){
                    count++;
                    value = first[row1 - 1][j];
                }
            }
        }
        if(count == 0)
            cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
        else if(count == 1)
            cout<<"Case #"<<i<<": "<<value<<endl;
        else
            cout<<"Case #"<<i<<": Bad magician!"<<endl;
    }

    return 0;
}
