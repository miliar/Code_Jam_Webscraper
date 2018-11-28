#include<iostream>
#include<algorithm>
#include<math.h>
using namespace std;

bool myfunction (int i,int j) { return (i>j); }

int main(){
	ios_base::sync_with_stdio(false);
	int t; cin>>t;
	for(unsigned int t1 = 1; t1<=t; t1++){
		cout<<"Case #"<<t1<<": ";
		int d;
		char ch = 'n';
		cin>>d;
		int p[d], maxVal = 0, cost, small=1000000;
		
		for (unsigned int i = 0; i < d; i ++){
			cin>>p[i];
			if(p[i] > maxVal){
				maxVal = p[i];
			}
		}
		
		for (unsigned int j = 1; j <= maxVal; j ++){
			cost = 0;
			for (unsigned int i = 0; i < d; i ++){
				if(p[i] > j){
					if(p[i]%j == 0)
						cost = cost + (p[i]/j) - 1;
					else
						cost = cost + (p[i]/j);
				}
			}
			if(small > (cost+j)){
				small = cost+j;
			}
		}
		cout<<small<<endl;
	}
	return 0;
}
