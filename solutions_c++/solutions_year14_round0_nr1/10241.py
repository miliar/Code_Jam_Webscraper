#include <fstream>
//#include <iostream>
using namespace std;
ifstream cin;
ofstream cout;
bool taken[15];
int main()
{
    cin.open ("a-small.in");
    cout.open ("a-small.out");
    int t;
    cin>>t;
    int f,s;
    int board[4][4];
    int board2[4][4];
    for (int i=1;i<=t;i++) {
        cin>>f;
        for (int o=0;o<4;o++)
        for (int j=0;j<4;j++)
        cin>>board[o][j];
        cin>>s;
        for (int o=0;o<4;o++)
        for (int j=0;j<4;j++)
        cin>>board2[o][j];
        int n=0;
        int num;
        cout<<"Case #"<<i<<": ";
        for (int j=0;j<4;j++)
        for (int o=0;o<4;o++){
        if (board[f-1][j]==board2[s-1][o]) {
            if (taken[board[f-1][j]-1]) continue;
            num=board[f-1][j];
            taken[num-1]=true;
            n++;
        }
    }
    for (int j=0;j<16;j++) taken[j]=false;
    if (n==1) cout<<num;
    if (n>1) cout<<"Bad magician!";
    if (n==0) cout<<"Volunteer cheated!";
    cout<<endl;
    }
   return 0;
}
