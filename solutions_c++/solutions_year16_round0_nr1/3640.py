#include<iostream>

using namespace std;
const int MN=20;
int mark[MN];
void markdg(unsigned long long x){
	if(x==0){
		mark[0]=1;
	}else{
		while(x>0){
			mark[x%10]=1;
			x/=10;
		}
	}
}
bool checkmark(){
	for(int i=0;i<10;i++)
		if(mark[i]==0){
			return 0;
		}
	return 1;
}
int main(){
	int T;
	cin>>T;
	for(int i=0;i<T;i++){
		for(int i=0;i<10;i++){
			mark[i]=0;
		}
		unsigned long long N;
		cin>>N;
		if(N==0){
			cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		}else{
			int con=1;
			markdg(N);
			int zerocon=0;
			while(!checkmark()){
				con++;
				markdg(N*con);
			}
			cerr<<"N="<<N<<endl;
			cout<<"Case #"<<i+1<<": "<<N*con;
			cout<<endl;
		}
	}
}


			
		
