#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;
ifstream fin("D-small-attempt0.in");
ofstream fout("answer.txt");
int main(){
	int T;
	fin>>T;
	for(int t=1;t<=T;t++){
        fout<<"Case #"<<t<<": ";
        int k,c,s;
        fin>>k>>c>>s;
        fout<<1;
        for(int i=2;i<=s;i++){
            long long ans=i;
            for(int j=1;j<c;j++){
                ans=(ans-1)*k+i;
                if(ans<=0){
                    cout<<"error"<<endl;
                }
            }
            fout<<" "<<ans;
        }
        fout<<endl;
	}
	return 0;
}
