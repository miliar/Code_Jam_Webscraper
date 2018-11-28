#include <iostream>

using namespace std;

int main(){

freopen("A-small-attempt0.in","r",stdin);
freopen("A.out","w",stdout);

int grid[4][4][2];
int rows[2];
int t=0;
cin>>t;

for(int test = 0;test<t;test++){

int i,j,k;


for(k=0;k<2;k++){
        cin>>rows[k];
		rows[k]--;
    for(i=0;i<4;i++){
        for(j=0;j<4;j++){
            cin>>grid[i][j][k];
        }
    }
}

int common = 0;
int com = 0;

for(i=0;i<4;i++){
    for(j=0;j<4;j++){
        if(grid[rows[0]][i][0]==grid[rows[1]][j][1]){
            common++;
            com = grid[rows[0]][i][0];
            break;
        }
    }
}
if(common==1){
    cout<<"Case #"<<test+1<<": "<<com<<endl;
}else if(common==0){
    cout<<"Case #"<<test+1<<": Volunteer cheated!"<<endl;
}else {
    cout<<"Case #"<<test+1<<": Bad magician!"<<endl;
}

}

}
