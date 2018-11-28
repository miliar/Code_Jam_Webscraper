#include <iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;
    int cse[t][2][4][4];
    int a[t][2];
    for(int noc=0;noc<t;noc++){
        for(int x=0;x<2;x++){
            cin>>a[noc][x];
            for(int i=0;i<4;i++)
                for(int j=0;j<4;j++)
                    cin>>cse[noc][x][i][j];
        }
    }
    int found[t],choice[t];
    for(int s=0;s<t;s++){
        found[s]=0;
        for(int y=0;y<4;y++){
            for(int z=0;z<4;z++){
                if(cse[s][0][a[s][0]-1][y]==cse[s][1][a[s][1]-1][z]){
                    if(found[s]==0){
                        found[s]=1;
                        choice[s]=cse[s][0][a[s][0]-1][y];
                    } else {
                        found[s]=2;
                    }
                }
            }
        }
        if(found[s]==0){
            cout<<"Case #"<<s+1<<": Volunteer cheated!"<<endl;
        } else if(found[s]==1){
            cout<<"Case #"<<s+1<<": "<<choice[s]<<endl;
        } else if(found[s]==2){
            cout<<"Case #"<<s+1<<": bad magician!"<<endl;
        }
    }
    return 0;
}
