#include<stdio.h>
#include<set>
#include<iostream>

using namespace std;

int main(){
	int test_case=0;
	cin>>test_case;

	for(int i=0;i<test_case;i++){
		int s_num =0;
		cin >> s_num;
		std::set<int> count;
		int w_num=s_num;
		int n=1;
		if(s_num==0){
			cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		}
			else{
		while(count.size()<11){
			int temp = w_num;
			while(w_num!=0){
				count.insert(w_num%10);
				w_num=w_num/10;
			}
			if(count.size()==10){
				cout<<"Case #"<<i+1<<": "<<temp<<endl;

				break;
			}else{
				n=n+1;
				w_num= n*s_num;
			}

		}
	}
	}
	return 0;
}
