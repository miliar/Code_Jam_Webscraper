#include<iostream>
#include<stdio.h>
#define max 100
using namespace std;
int main(){
    int testcases,shuffledcards[4][4],cards[4][4],cnt=0,k;
    int firstturn,secondturn;
    int testcasesran=0;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("magicianout.txt","w",stdout);
    cin>>testcases;
    //cout<<testcases;

    int result[max];

    while(testcasesran < testcases){
            result[cnt]=0;
            cin>>firstturn;
            for(int i=0;i<4;i++){
                for(int j=0;j<4;j++){
                        cin>>cards[i][j];
                }
            }
            cin>>secondturn;
            for(int i=0;i<4;i++){
                for(int j=0;j<4;j++){
                        cin>>shuffledcards[i][j];
                }
            }
            for(int i=0;i<4;i++){
                for(int j=0;j<4;j++){
                       if((cards[firstturn-1][i] == shuffledcards[secondturn-1][j])){
                            result[cnt]++;
                       }
                }
            }

            if(result[cnt]==1){
                for(int i=0;i<4;i++){
                    for(int j=0;j<4;j++){
                       if((cards[firstturn-1][i] == shuffledcards[secondturn-1][j])){
                            result[cnt] = cards[firstturn-1][i];
                            //cout<<result[cnt]<<" " ;
                       }
                    }
                }
            }
            else if(result[cnt] > 1){
                result[cnt] = 17;
            }
            //cout<<result[cnt]<<" " ;
            cnt++;
            testcasesran++;
    }
    for(int i=0;i<testcases;i++){
        switch(result[i]){
        case 17:
            cout<< "Case #"<<i+1<<": Bad magician!";
            break;
        case 0:
            cout<< "Case #"<<i+1<<": Volunteer cheated!";
            break;
        default:
            cout<< "Case #"<<i+1<<": "<<result[i];
        }
        cout<<endl;
    }
return 0;


}


