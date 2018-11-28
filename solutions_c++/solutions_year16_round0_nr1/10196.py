#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
#include<fstream>
#include<vector>
#include <sstream>
#include <set>
using namespace std;

ofstream out("ans.in");
ifstream in("A-large.in");
set<int> elems;
int main(){
	
	int t;
	long long n;
	long long data;
	in>>t;
	for(int i=0;i<t;i++){
		in>>n;
		long long cnt=1;
		long long last_num;
		long long tmp;
		bool isfind=false;
		while(!isfind){
			tmp=cnt*n;
			last_num=tmp;
			if(tmp==(cnt-1)*n){
				
				break;
			}
			while(tmp>0){
				elems.insert((int)tmp%10);
				//cout<<tmp%10<<endl;
				if(elems.size()==10){
					isfind=true;
					elems.clear();
					break;
				}
				tmp/=10;
				
			}
			
			cnt++;
			
		}
	
		if(isfind){
			out<<"Case #"<<i+1<<": "<<last_num<<endl;
		}else{
			out<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		}
	}
	return 0;
	
}
