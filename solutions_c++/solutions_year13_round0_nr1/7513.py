#include<iostream>
#include<cstdlib>
using namespace std;
bool check(char s[4][4],char c){
    if((s[0][0]=='T'||s[0][0]==c)&&(s[1][1]=='T'||s[1][1]==c)&&(s[2][2]=='T'||s[2][2]==c)&&(s[3][3]=='T'||s[3][3]==c))return true;
    else if((s[3][0]=='T'||s[3][0]==c)&&(s[2][1]=='T'||s[2][1]==c)&&(s[1][2]=='T'||s[1][2]==c)&&(s[0][3]=='T'||s[0][3]==c))return true;
    else if((s[0][1]=='T'||s[0][1]==c)&&(s[0][2]=='T'||s[0][2]==c)&&(s[0][3]=='T'||s[0][3]==c)&&(s[0][0]=='T'||s[0][0]==c))return true;
    else if((s[1][1]=='T'||s[1][1]==c)&&(s[1][2]=='T'||s[1][2]==c)&&(s[1][3]=='T'||s[1][3]==c)&&(s[1][0]=='T'||s[1][0]==c))return true;
    else if((s[2][1]=='T'||s[2][1]==c)&&(s[2][2]=='T'||s[2][2]==c)&&(s[2][3]=='T'||s[2][3]==c)&&(s[2][0]=='T'||s[2][0]==c))return true;
    else if((s[3][1]=='T'||s[3][1]==c)&&(s[3][2]=='T'||s[3][2]==c)&&(s[3][3]=='T'||s[3][3]==c)&&(s[3][0]=='T'||s[3][0]==c))return true;
    else if((s[1][0]=='T'||s[1][0]==c)&&(s[2][0]=='T'||s[2][0]==c)&&(s[3][0]=='T'||s[3][0]==c)&&(s[0][0]=='T'||s[0][0]==c))return true;
    else if((s[1][1]=='T'||s[1][1]==c)&&(s[2][1]=='T'||s[2][1]==c)&&(s[3][1]=='T'||s[3][1]==c)&&(s[0][1]=='T'||s[0][1]==c))return true;
    else if((s[1][2]=='T'||s[1][2]==c)&&(s[2][2]=='T'||s[2][2]==c)&&(s[3][2]=='T'||s[3][2]==c)&&(s[0][2]=='T'||s[0][2]==c))return true;
    else if((s[1][3]=='T'||s[1][3]==c)&&(s[2][3]=='T'||s[2][3]==c)&&(s[3][3]=='T'||s[3][3]==c)&&(s[0][3]=='T'||s[0][3]==c))return true;
    return false;
}
int main()
{
    int t,t1=1;
    cin>>t;
    while(t1!=t+1){

        char stps[4][4];int flag=0;
        for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){cin>>stps[i][j];if(stps[i][j]=='.' && flag != 1)flag=1;}}
        cout<<"Case #"<<t1<<":";
        if(check(stps,'O'))cout<<" O won"<<endl;
        else if(check(stps,'X'))cout<<" X won"<<endl;
        else if(flag == 1)cout<<" Game has not completed"<<endl;
        else cout<<" Draw"<<endl;
        t1++;
    }
    return 0;
}
