#include<iostream>
#include<fstream>

using namespace std;

int main(){
	ifstream i("D.txt");
	ofstream o;
	o.open("Dout.txt");
	
	int T, K, C, S, t;
	i>>T;
	for(int cnt=0; cnt<T; cnt++){
		i>>K>>C>>S;
		
		if(S==K){
		
			o<<"Case #"<<cnt+1<<": ";
			for(int s=1; s<=S; s++){
				o<<s<<" ";
			}
			o<<endl;
		}else{
			
			
		}
	}	
	
	i.close();
	o.close();
	return 0;
}
