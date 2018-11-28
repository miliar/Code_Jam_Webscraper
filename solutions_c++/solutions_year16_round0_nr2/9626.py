#include <bits/stdc++.h>
#define input freopen("in.txt","r",stdin)
#define output freopen("out.txt","w",stdout)
using namespace std;
#define EPS 1e-8
#define PI acos(-1)
#define Vector Point
 

int main() {
	input;
	output;
	int t;
	cin>>t;
	int cases=1;
	while(t--){
		string cad;
		cin>>cad;
		string cad2="";
		cad2+=cad[0];
		int j=0;
		for (int i = 1; i < cad.size(); ++i)
			if(cad2[j]!=cad[i])
				cad2+=cad[i],j++;
		int sol=0;
		if(cad2[0]=='+'){
			sol=cad2.size()-(cad2.size()%2!=0);
		}
		else{
			sol=cad2.size()-(cad2.size()%2==0);
		}
		printf("Case #%d: %d\n",cases++,sol);
	}
	return 0;
}

