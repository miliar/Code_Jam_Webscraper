#include<iostream>
using namespace std;
#include<cstdio>
int main(){
    int t,index=1;
    cin>>t;
    while(t--){
        int r_no1,r_no2,square_grid1[4][4],square_grid2[4][4],flag=0,matched_card;
        cin>>r_no1;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>square_grid1[i][j];
        cin>>r_no2;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>square_grid2[i][j];

        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                if(square_grid1[r_no1-1][i]==square_grid2[r_no2-1][j]){
                    if(flag==0){
                        flag=1;
                        matched_card=square_grid1[r_no1-1][i];
                    }
                    else{
                        flag=2;
                    }
                }
            }
        }
        if(flag==1)
            cout<<"Case #"<<index<<":"<<" "<<matched_card<<endl;
        else if(flag==2)
            cout<<"Case #"<<index<<":"<<" "<<"Bad magician!"<<endl;
        else if(flag==0)
            cout<<"Case #"<<index<<":"<<" "<<"Volunteer cheated!"<<endl;

            index++;
        }
       return 0;
    }


