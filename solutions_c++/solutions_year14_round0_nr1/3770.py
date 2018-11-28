#include<iostream>
#include<fstream>
#include<cstdio>
#include<cstring>
using namespace std;
int main(){
    int a[10000];
    ifstream input;
    ofstream output;
    input.open("A-small-attempt1.in");
    output.open("output.out");
//    while(!input.eof()){
        int t,g1,g2,i,j,k,val,flag=1,flag2=1,u,v;
        string ans;
        int b[5][5],c[5][5];
        input>>t;
        for(int x=1;x<=t;x++){
                int count=0;
            input>>g1;
            for(j=1;j<=4;j++)
            for(k=1;k<=4;k++){
                input>>b[j][k];
            }
            input>>g2;
            for(j=1;j<=4;j++)
            for(k=1;k<=4;k++){
                input>>c[j][k];
            }
            for(j=1;j<=4;j++)
            for(k=1;k<=4;k++){
                if(b[g1][j]==c[g2][k]){
                    val=b[g1][j];
                    count++;
                }
            }
            if(count==1){
                output<<"Case #"<<x<<": "<<val<<endl;
            }
            else{ if(count>1){
                ans="Bad magician!";
            }
            else{
                ans="Volunteer cheated!";
            }
            output<<"Case #"<<x<<": "<<ans<<endl;
            }
        }
//    }
    input.close();
    output.close();
    return 0;
}
