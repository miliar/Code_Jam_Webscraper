#include<iostream>
#include <fstream>
#include<vector>
using namespace std;

ifstream fin("a1.in");
ofstream fout("a1.out");

int main(){
    int n;
    fin>>n;
    for(int i=0;i<n;i++){
        int x;
        fin>>x;
        bool done=false;
        vector<bool> ary(10,false);
        for(int k=1;k<=10000000;k++){
            long long temp=x*k;
            while(temp!=0){
                ary[temp%10]=true;
                temp/=10;
            }
            for(int j=0;j<10;j++){
                if(ary[j]==false)
                    break;
                else if(j==9){
                    fout<<"Case #"<<i+1<<": "<<k*x<<endl;
                    done=true;
                }
            }
            if(done)
                break;
        }
        if(!done){
            fout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
        }
    }
}
