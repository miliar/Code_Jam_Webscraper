#include<iostream>
using namespace std;
int map[105][105];
int ma[105];
int m,n;
bool check1(){
    for(int i=0;i<m;i++){
        //int min=map[i][0];
        for(int j=0;j<n;j++){
            if(map[i][j]<ma[i]){
                for(int z=0;z<m;z++){
                    if(map[z][j]>map[i][j])return false;
                }
            }
        }
    }
    return true;
}

int main(){
    int t;
    cin>>t;
    for(int z=1;z<=t;z++){
        cin>>m>>n;
        for(int i=0;i<m;i++){
            ma[i]=0;
            for(int j=0;j<n;j++){
                cin>>map[i][j];
                if(ma[i]<map[i][j])ma[i]=map[i][j];
            }
        }
        if(check1())cout<<"Case #"<<z<<": YES"<<endl;
        else cout<<"Case #"<<z<<": NO"<<endl;
    }
}
