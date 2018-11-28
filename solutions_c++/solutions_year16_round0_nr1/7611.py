#include<bits/stdc++.h>
using namespace std;
#define ull unsigned long long

void solve(bool arr[],ull n){
	int tmp;
	while(n!=0){
		tmp = n%10;
		arr[tmp]=true;
		n = n/10; 
	}
}

int main() {
	ios_base::sync_with_stdio(0);
	//freopen("in.txt","r",stdin);
	
	int tt,cc=1;
	cin>>tt;
	while(cc<=tt){
		unsigned long long num;
		bool digits[10];
		for(int i=0; i<10; i++)
		   digits[i] = false;
		 
		cin>>num;
		//cout<<"NUM "<<num<<endl;
		if(num==0){
			cout<<"Case #"<<cc<<": INSOMNIA\n";
		}
		else{
			int mul = 1;
			bool done=false;
			
			ull tmp_num;
			while(!done){
				tmp_num = mul*num;
				solve(digits,tmp_num);
				done = true;
				//cout<<"Exporing for : "<<tmp_num<<endl;
				
				for(int i=0; i<10; i++){
					if(digits[i]==false){
						done = false;
						break;
					}
				}
				
				mul++;
				
			}
			cout<<"Case #"<<cc<<": "<<tmp_num<<"\n";
		}
		cc++;
	}
	return 0;
	
}
