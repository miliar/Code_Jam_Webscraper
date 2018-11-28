#include <iostream>

using namespace std;

int main(void){
int t,ans1,ans2,card1[4][4],card2[4][4],card[4];
int *row1,*row2;
cin>>t;
for(int n=0;n<t;n++){
    cin>>ans1;
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
        cin>>card1[i][j];
         }
    }
    cin>>ans2;
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
        cin>>card2[i][j];
        }
    }
    row1=card1[ans1-1];
    row2=card2[ans2-1];
    int cardnum=0;
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            if(row1[i]==row2[j]){
            card[cardnum]=row1[i];
            cardnum++;
            }
        }
    }
    if(cardnum==0){
    cout<<"Case #"<<n+1<<": Volunteer cheated!"<<endl;
    }
    else if(cardnum==1){
    cout<<"Case #"<<n+1<<": "<<card[0]<<endl;
    }
    else{
    cout<<"Case #"<<n+1<<": "<<"Bad magician!"<<endl;
    }
}
return 0;
}
