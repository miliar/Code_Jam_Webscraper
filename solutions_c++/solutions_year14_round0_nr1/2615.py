//abstract
#include<iostream>
#include<cstdio>
using namespace std;

int main(){
    int first_config[4][4]={0};
    int second_config[4][4]={0};
    int t=0;
    freopen("1.in", "r", stdin) ;
    freopen("1.out", "w", stdout) ;
    cin>>t;
    int row_in_first=0;
    int row_in_second=0;
    for(int i=1;i<=t;i++){
        cin>>row_in_first;
        for(int j=0;j<4;j++){
            for(int k=0;k<4;k++){
                cin>>first_config[j][k];
            }
        }
        cin>>row_in_second;
        for(int j=0;j<4;j++){
            for(int k=0;k<4;k++){
                cin>>second_config[j][k];
            }
        }
        int no_of_matches=0;
        int match=0;
        for(int j=0;j<=3;j++){
            for(int k=0;k<=3;k++){
            if(first_config[row_in_first-1][j]==second_config[row_in_second-1][k]){
                no_of_matches++;
                match=first_config[row_in_first-1][j];}
            }
        }
        cout<<"Case #"<<i<<": "; 
        if(no_of_matches==1){cout<<match<<"\n";}
        else if(no_of_matches==0){cout<<"Volunteer cheated!\n";}
        else {cout<<"Bad magician!\n";}
    }
}
