#include<iostream>
#include<stdio.h>
#include<string.h>

using namespace std;

int main(){

    int T;
    int first[4][4], second[4][4], a, b, test, ans;

    cin>>T;

    for(int z=0; z<T; z++){
        cin>>a;
        for(int x=0; x<4; x++){
            for(int y=0; y<4; y++){
                cin>>first[x][y];
            }
        }
        cin>>b;
        for(int x=0; x<4; x++){
            for(int y=0; y<4; y++){
                cin>>second[x][y];
            }
        }
        a=a-1;
        b=b-1;
        test=0;
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                if(first[a][i]==second[b][j]){
                    ans=first[a][i];
                    test++;
                }
            }
        }
        if(test==1){
            cout<<"Case #"<<z+1<<": "<<ans<<endl;
        }
        else if(test==0){
            cout<<"Case #"<<z+1<<": Volunteer cheated!"<<endl;
        }
        else{
            cout<<"Case #"<<z+1<<": Bad magician!"<<endl;
        }
    }

    return 0;
}
