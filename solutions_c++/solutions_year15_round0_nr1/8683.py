#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main(){
    ifstream fin("a.in");
    ofstream fout ("a.out");
    int nott;fin>>nott;
    for(int t=1;t<=nott;t++){
        int smax;fin>>smax;
        string datastr;fin>>datastr;
        int num[smax+1];
        for(int i=0;i<=smax;i++){
            num[i]=datastr[i]-'0';
        }
        int co=0,ino=0;
        for(int i=0;i<=smax;i++){
            if(num[i]==0)continue;
            if(co<i){
                ino+=i-co;
                co+=i-co;
            }
            co+=num[i];
        }
        fout<<"Case #"<<t<<": "<<ino<<endl;

    }
}
