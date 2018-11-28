#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int main() {
	int t;
	string N;
	int num_visit[10];
	int visited;
	long long int find, dummy, c;
	int i, j;
	//vector<int> v;
	cin>>t;
	for(i = 1;i<=t;++i){
		cin>>N;
		visited = 0;
		find = 0;
		memset(num_visit, 0 ,sizeof num_visit);
		cout<<"Case #"<<i<<": ";

		/*for(j = 0;j<N.size();++j){
			v.push_back((int)(N[i]-'0'));
			if(bool[v[j]] == 0){
				++visited;
				bool[v[j]] = 1;
			}
		}*/
		if(N[0] == '0')
			cout<<"INSOMNIA"<<endl;
		else{
		
		/*******Find Sleep Value*******/
	
			while(visited < 10){
				++find;
				dummy= 0;
				for(j = N.size()-1;j>=0;--j){
					c = ( ((int)(N[j]-'0')) * find) + dummy;
					dummy = c/10;
					c = c%10;
					if(num_visit[c] == 0){
					++visited;
					++num_visit[c];
					}
				}
				if(dummy > 0 && num_visit[dummy] == 0){
					++visited;
					++num_visit[dummy];
				}
			}
		
		/****String -to- Number*****/
		
			dummy = 1;
			c = 0;
			for(j = N.size()-1;j>=0;--j){
				c += ( (int)(N[j]-'0') * dummy);
				dummy *= 10;
			}
		
		/******Result******/
		
			cout<<c * find<<endl;
		}
	}
	return 0;
}