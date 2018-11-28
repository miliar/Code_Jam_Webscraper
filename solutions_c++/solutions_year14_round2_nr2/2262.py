#include <iostream>
#include <fstream>
#include <map>
using namespace std;
int main(){
	ofstream ofs("output.txt"); ifstream ifs("B-small-attempt1.in");
	int T; ifs >> T ;
	for(int i=1;i<=T;++i){
		long A,B,K; ifs >> A >> B >> K ;
		long cnt=0;
		for(int j=0;j<A;++j){
			for(int k=0;k<B;++k){
				long tmp=0;
				int tmp_j=j, tmp_k=k;
				string str="";
				while(tmp_j>0 && tmp_k>0){
					if(tmp_j%2==1 && tmp_k%2==1) str+='1'; else str+='0';
					tmp_j>>=1, tmp_k>>=1;
				}
				for(int l=str.size()-1;l>=0;--l){
					char ch=str[l];
					tmp=tmp*2+(ch-'0');
				}
				if(tmp<K) cnt++;
			}
		}
		ofs << "Case #" << i << ": " << cnt << '\n' ;
	}
}