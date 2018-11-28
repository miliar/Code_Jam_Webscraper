#include<cstdlib>
#include<cstdio>
#include<iostream>
#include<vector>
using namespace std;

int main(){
	int nc, caso, a,b,v;
	
	cin>>nc;
	for(caso=0; caso<nc; caso++){
		cin>>a;
		vector<int> a16(16,0);
		for(int i=0; i<16; i++){
			cin>>v;
			if( i/4 == a-1 ){
				a16[v-1] = 1;
			}
		}
		cin>>b;
		vector<int> b16(16,0);
		for(int i=0; i<16; i++){
			cin>>v;
			if( i/4 == b-1 ){
				b16[v-1] = 1;
			}
		}
		int ct=0;
		int res=-1;
		for(int i=0; i<16; i++){
			if( a16[i] == b16[i] && a16[i] == 1){
				ct++;
				res = i+1;
			}
		}
		if( ct == 1){
			cout<<"Case #"<<caso+1<<": "<<res<<endl;
		}
		else if( ct == 0){
			cout<<"Case #"<<caso+1<<": Volunteer cheated!"<<endl;
		}
		else{
			cout<<"Case #"<<caso+1<<": Bad magician!"<<endl;
		}
	}
	return 0;
}
