#include <iostream>
#include <vector>
using namespace std;

int main(){
	int cases;
	cin>>cases;
	for(int t=0;t<cases;t++){
		vector<int> a;
		int a_num;
		cin>>a_num;
		for(int i=0;i<16;i++){
			int k;
			cin>>k;
			a.push_back(k);
		}
		vector<int> b;
		int b_num;
		cin>>b_num;
		for(int i=0;i<16;i++){
			int k;
			cin>>k;
			b.push_back(k);
		}
		vector<int> first;
		for(int i=(a_num-1)*4;i<a_num*4;i++){
			first.push_back(a[i]);
		}
		int count=0;
		int number=0;
		for(int i=(b_num-1)*4;i<b_num*4;i++){
			for(int j=0;j<4;j++){
				if(b[i]==first[j]){
					count++;
					number = first[j];
				}
			}
		}
		cout<<"Case #"<<t+1<<": ";
		if(count ==1){
			cout<<number<<endl;
		}
		else if(count ==0){
			cout<<"Volunteer cheated!"<<endl;
		}
		else{
			cout<<"Bad magician!"<<endl;
		}
	}
	return 0;
}
	
