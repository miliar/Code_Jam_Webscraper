#include <fstream>
#include <iostream>
using namespace std;
int main(){
    int T;
    ifstream in("inputs.txt");
    ofstream out("output.txt");
    in >> T;
    for(int i=0;i<T;i++){
        int a1, a2;
        int a[4][4];
        int b[4][4];
        in >>a1;
        for(int j=0;j<4;j++){
            for( int k=0;k<4;k++){
                in>>a[j][k];
            }
        }
        in >>a2;
        for(int j=0;j<4;j++){
            for (int k=0;k<4;k++){
                in>>b[j][k];
            }
        }
        int count=0;
        int answer;
        for(int j=0;j<4;j++){
            for(int k=0;k<4;k++){
                if(a[a1-1][j]==b[a2-1][k]){
                    count++;
                    answer=a[a1-1][j];
                }
            }
        }
        out<<"Case #"<< i+1<<": ";
        if(count==0){
            out<<"Volunteer cheated!"<<endl;
        }
        if(count==1){
            out<<answer<<endl;
        }
        if(count>1){
            out<<"Bad magician!"<<endl;
        }
    }
}
