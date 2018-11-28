#include <iostream>
#include <vector>
using namespace std;

main(){
	int T;
	cin>>T;

	for(int t=0;t<T;t++){

		string in;
		cin>>in;
		vector<char> stack(in.size(),0);
		int check=0;
		for(int i=0;i<in.size();i++){
			if(in[i]=='-') check=1;
			//stack.push_back(in[i]);
			stack[in.size()-i-1]=in[i];
		}

		if(check==0) cout<<"Case #"<<t+1<<": "<<"0\n";
		else{
			int flip_cnt=0;
			for(int i=stack.size()-1;i>=0;i--){
					int j;
					for(j=i;j>=0 && stack[j]==stack[i];j--){
					}
					if((j+1)>0 && stack[j+1]=='+'){
						flip_cnt++;
					}else if(stack[j+1]=='-'){
						flip_cnt++;
					}
					i=j+1;
			}
			cout<<"Case #"<<t+1<<": "<<flip_cnt<<"\n";
		}
	}
}