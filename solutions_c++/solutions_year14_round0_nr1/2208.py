#include<string>
#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
    int T, h, i, j, k, answer, arrange, bingoTime,bingoNum;
    cin>>T; 
    int card[4][4],select[2][4];
    for(i = 0; i < T;i++){
        answer = 0;
        
        for(h = 0; h < 2; h++)
        {
        cin>>arrange;
            for(j = 0; j < 4; j++)
            {
                for(k = 0; k < 4; k++)
                {
                    cin>> card[j][k];
                }
                if(j == arrange - 1){
                    for(k = 0; k < 4; k++)
                    {
                        select[h][k] = card[j][k];
                    }
                }
                    
            } 
        }

        bingoTime = 0;
        for(j = 0; j < 4; j++){
        for(k = 0; k < 4; k++)
            {
                if(select[0][j] == select[1][k]){
                    bingoNum = select[0][j];
                    bingoTime ++;
                }
            }
        }

        cout<<"Case #"<<i+1<<": ";
        if(bingoTime == 1){
            cout<<bingoNum;    
        }else if(bingoTime > 1){
            cout<<"Bad magician!";
        }else{
            cout<<"Volunteer cheated!";
        }
        cout<<endl;
    }
    return 0;
}
