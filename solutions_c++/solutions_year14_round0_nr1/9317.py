
#include <iostream>
#include <string.h>
#include <vector>
using namespace std;

int main(){
    int NumberOfCases=0;
    int NumOfRow1, NumOfRow2;
    int arrangment1[4], arrangment2[4];
    int dummy;

    
    cin>>NumberOfCases;
    for(int i=0;i<NumberOfCases;i++){
        cin>>NumOfRow1;
        for(int col1=0;col1<4;col1++){
            for(int row1=0;row1<4;row1++){
                if(col1==NumOfRow1-1){
                    cin>>arrangment1[row1];}
                else{
                    cin>>dummy;
                }}}
        cin>>NumOfRow2;
        for(int col2=0;col2<4;col2++){
            for(int row2=0;row2<4;row2++){
                if(col2==NumOfRow2-1){
                    cin>>arrangment2[row2];}
                else{
                    cin>>dummy;
                }}}
        
        int check1=0;
        
        while(arrangment1[check1%4]!=arrangment2[check1/4]&&check1<16){
                check1++;}
        int found1=check1;
        cout<<"Case #"<<i+1<<": ";
        if(check1==16){
            cout<<"Volunteer cheated!";
        }
        else{
            check1++;
            while(arrangment1[check1%4]!=arrangment2[check1/4]&&check1<16)
                check1++;
            if(check1==16){
                cout<<arrangment2[found1/4];
            }
            else{
                cout<<"Bad magician!";
            }
        }
        cout<<endl;
    }  }
