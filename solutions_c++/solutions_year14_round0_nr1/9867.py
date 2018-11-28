#include<iostream>
#include<stdio.h>
#include<fstream>
using namespace std;
int main(){
    int T;
    int now=1;
    int card1[4][4],card2[4][4];
    freopen("A-small-attempt1.in", "r", stdin);
    cin>>T;
    ofstream file;
    file.open("output.txt");
    while(T--){
        int a1,a2;
        cin>>a1;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>card1[i][j];
        cin>>a2;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>card2[i][j];
        int sum=0;
        int ans;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                if(card1[a1-1][i]==card2[a2-1][j]){
                    sum++;
                    ans=card1[a1-1][i];
                }
        switch(sum){
        case 0:
            file<<"Case #"<<now<<": Volunteer cheated!\n";
            break;
        case 1:
            file<<"Case #"<<now<<": "<<ans<<"\n";
            break;
        default:
            file<<"Case #"<<now<<": Bad magician!\n";
            break;
        }
        now++;
    }
}
