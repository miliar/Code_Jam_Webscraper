#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int wins(int*a){
    for(int i=0;i<4;i++){
        if(((a[i]+a[4+i]+a[8+i]+a[12+i])==4)||((a[i]+a[4+i]+a[8+i]+a[12+i])==13)||
           ((a[4*i]+a[4*i+1]+a[4*i+2]+a[4*i+3])==4)||((a[4*i]+a[4*i+1]+a[4*i+2]+a[4*i+3])==13)){
            return 1;
           }
         else if(((a[i]+a[4+i]+a[8+i]+a[12+i])==0)||((a[i]+a[4+i]+a[8+i]+a[12+i])==10)||
           ((a[4*i]+a[4*i+1]+a[4*i+2]+a[4*i+3])==0)||((a[4*i]+a[4*i+1]+a[4*i+2]+a[4*i+3])==10)){
           return 0;
           }
    }
    if(((a[0]+a[5]+a[10]+a[15])==4)||((a[0]+a[5]+a[10]+a[15])==13))
        return 1;
    else if(((a[0]+a[5]+a[10]+a[15])==0)||((a[0]+a[5]+a[10]+a[15])==10))
        return 0;
    else if(((a[3]+a[6]+a[9]+a[12])==4)||((a[3]+a[6]+a[9]+a[12])==13))
        return 1;
    else if(((a[3]+a[6]+a[9]+a[12])==0)||((a[3]+a[6]+a[9]+a[12])==10))
        return 0;
    else return 2;
}

bool allfilled(int*a){
    for(int i=0;i<16;i++){
        if(a[i]==20){
            return false;
        }
    }
    return true;
}

int main(){
    ifstream input("A-large.in");
    ofstream output("A-large.out");
    int cases;
    input>>cases;
    string line;
    getline(input,line);
    for(int i=0;i<cases;i++){
        int a[16];
        for(int j=0;j<4;j++){
            getline(input,line);
            for(int k=0;k<4;k++){
                if(line[k]=='O')
                    a[j*4+k]=0;
                else if(line[k]=='X')
                    a[j*4+k]=1;
                else if(line[k]=='T')
                    a[j*4+k]=10;
                else a[j*4+k]=20;
            }
        }
        int n=wins(a);
        if(n==0)
            output<<"Case #"<<(i+1)<<": "<<"O won"<<endl;
        else if(n==1)
            output<<"Case #"<<(i+1)<<": "<<"X won"<<endl;
        else if((allfilled(a))&&(n==2))
            output<<"Case #"<<(i+1)<<": "<<"Draw"<<endl;
        else output<<"Case #"<<(i+1)<<": "<<"Game has not completed"<<endl;
        getline(input,line);
    }
    input.close();
    return 0;
}
