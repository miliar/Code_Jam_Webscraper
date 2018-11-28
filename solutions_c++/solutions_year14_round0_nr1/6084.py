#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;
int main(){
    ifstream cin("A-small-attempt0.in");
    ofstream cout("out.out");
    int T,apple = 1;
    cin>>T;
    while(T--){
        int a1,a2;
        int a[4][4],b[4][4],c[17];
        memset(c,0,sizeof(c));
        cin>>a1;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                cin>>a[i][j];
            }
        }
        for(int i=0;i<4;i++){
            c[a[a1-1][i]] = 1;
        }
        cin>>a2;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                cin>>b[i][j];
            }
        }
        int count = 0 , mag = 0;
        for(int i =0;i<4;i++){
            if(1 == c[b[a2-1][i]]){
                count ++;
                mag = b[a2-1][i];
            }
        }
        cout<<"Case #"<<apple++<<": ";
        if(0 == count) cout<<"Volunteer cheated!"<<endl;
        else if(1 == count) cout<< mag<<endl;
        else cout<<"Bad magician!"<<endl;

    }
    return 0;
}
