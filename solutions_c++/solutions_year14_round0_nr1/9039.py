#include <iostream>
#include <string>
#include <fstream>

using namespace std;

void solve();
void response(int,int,int,int,int,int,int,int,int);

int main(){
    solve();
    return 0;
}

void solve(){
    //Variables
    int ans1,ans2,n;
    int a[4][4],b[4][4];

    //Input
    cin>>n;
    for(int i = 1;i<n+1;i++){
        cin>>ans1;
        for(int j = 0;j<4;j++){
            cin>>a[j][0]>>a[j][1]>>a[j][2]>>a[j][3];
        }
        cin>>ans2;
        for(int j = 0;j<4;j++){
            cin>>b[j][0]>>b[j][1]>>b[j][2]>>b[j][3];
        }
        response(a[ans1-1][0],a[ans1-1][1],a[ans1-1][2],a[ans1-1][3],b[ans2-1][0],b[ans2-1][1],b[ans2-1][2],b[ans2-1][3],i);
    }
}

void response(int ra1,int ra2,int ra3,int ra4,int rb1,int rb2,int rb3,int rb4,int caseN){
    int a[4]={ra1,ra2,ra3,ra4},b[4]={rb1,rb2,rb3,rb4};
    int corrects=0,answer=0;
    //Solving rows
    for(int i = 0;i<4;i++){
        for(int j = 0;j<4;j++){
            if(a[i]==b[j]){
                corrects++;
                answer=a[i];
            }
        }
    }
    ofstream output;
    output.open("output.txt",ios_base::app);
    output<<"Case #"<<caseN<<": ";
    if(corrects==1){
        output<<answer<<endl;
    }else if(corrects>1){
        output<<"Bad magician!"<<endl;
    }else{
        output<<"Volunteer cheated!"<<endl;
    }
    //printing answer/response to input
}

