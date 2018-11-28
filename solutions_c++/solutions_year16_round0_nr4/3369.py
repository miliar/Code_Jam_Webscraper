#include <iostream>
#include <cstring>
#include <cmath>
#include <fstream>
int a,b,c;
using namespace std;

int main(){
    ifstream fcin;
    ofstream fout;
    fcin.open("D-small-attempt2.in");
    fout.open("D.out");
    
    int testCase;
    fcin>>testCase;
    //cin>>testCase;
    for(int i=0;i<testCase;i++){
        //cin>>a>>b>>c;
        fcin>>a>>b>>c;
        long long int ans=1;
        long long int increase=1;
        long long int plus=1;
        for(int k=1;k<b;k++){
            plus*=a;
            increase=increase+plus;
        }
        //fout<<ans<<' ';
        fout<<"Case #"<<i+1<<": ";

        if(a==1){
            //cout<<1<<endl;
            fout<<1<<endl;
        }
        else{
        for(int j=0;j<c;j++){
            
            if(j!=a-1)
                fout<<ans<<' ';
            
            else{
                fout<<ans<<' '<<endl;
            }
            ans+=increase;
            //fout<<ans<<' ';
        }
    }
    }
    return 0;
}