#include<iostream>
#include<algorithm>

using namespace std;

int main(){
    int cases;
    cin>>cases;
    int countcase=0;
    while(cases--){
        countcase++;
        int a,b,i,j;
        cin>>a;
        int mat[4][4];
        int matt[4][4];
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                cin>>mat[i][j];
            }
        }
        cin>>b;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                cin>>matt[i][j];
            }
        }
        int temp,counter=0,value;
        for(i=0;i<4;i++){
            temp=mat[a-1][i];
            for(j=0;j<4;j++){
                if(temp==matt[b-1][j]){
                    counter++;
                    value=temp;
                }
            }
        }
        if(counter==0){
            cout<<"Case #"<<countcase<<": Volunteer cheated!\n";
            
        }
        else if(counter>1){
            cout<<"Case #"<<countcase<<": Bad magician!\n";
        }
        else if(counter==1){
            cout<<"Case #"<<countcase<<": "<<value<<endl;
        }
    }
}
