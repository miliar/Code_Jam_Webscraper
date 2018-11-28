#include <iostream>
#include <string>
#include <cstring>
using namespace std;
int T;
int N;
int M;
int lawn[100][100];
int map[100][100];
void output(bool tmp, int num);
void check(int caseNum){
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            int flag = 0;
            for(int k=0;k<N;k++){
                if(lawn[k][j]>lawn[i][j]){
                    flag++;
                    break;
                }
            }
            for(int k=0;k<M;k++){
                if(lawn[i][k]>lawn[i][j]){
                    flag++;
                    break;
                }
            }
            if(flag==2){
                output(false, caseNum);
                return;
            }
        }
    }
    output(true, caseNum);
    return;
}

    /*int diff = 0;
    for(int j=0;j<M;j++){
        if(lawn[0][j]==2) diff = 1;
        if(lawn[0][j]==1){
            if(!diff){
                for(int k=j;k<M;k++){
                    if(lawn[0][k]==2){
                        diff = 1;
                        break;
                    }
                }
            }
            int isAll = 1;
            for(int i=0;i<N;i++){
                if(lawn[i][j]==2&&diff){
                    output(false, caseNum);
                    return;
                }
                if(lawn[i][j]==2){
                    isAll = 0;
                    break;
                }
            }
            if(isAll){
                for(int i=0;i<N;i++){
                    lawn[i][j] = 3;
                }
            }
        }
    }
    diff = 0;
    for(int i=0;i<N;i++){
        if(lawn[i][0]==2) diff = 1;
        else{
            if(!diff){
                for(int k=i;k<N;k++){
                    if(lawn[k][0]==2){
                        diff = 1;
                        break;
                    }
                }
            }
            int isAll = 1;
            for(int j=0;j<M;j++){
                if(lawn[i][j]==2&&diff){
                    output(false, caseNum);
                    return;
                }
                else if(lawn[i][j]==2){
                    isAll = 0;
                    break;
                }
            }
            if(isAll){
                for(int k=0;k<M;k++){
                    lawn[i][k] = 3;
                }
            }
        }
    }
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            if(lawn[i][j]==1){
                output(false, caseNum);
                return;
            }
        }
    }
    output(true, caseNum);
    return;*/
void output(bool tmp, int num){
   /* if(num==76){
        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                cout<<lawn[i][j];
            }
            cout<<endl;
        }
    }*/
    if(tmp){
        cout<<"Case #"<<num<<": YES"<<endl;
    }
    else{
        cout<<"Case #"<<num<<": NO"<<endl;
    }
}
int main(){
    cin>>T;
    for(int i=0;i<T;i++){
        cin>>N;
        cin>>M;
        for(int j=0;j<N;j++){
            for(int k=0;k<M;k++){
                cin>>lawn[j][k];
              //  cout<<lawn[j][k];
            }
           // cout<<endl;
        }
        check(i+1);
    }
}
