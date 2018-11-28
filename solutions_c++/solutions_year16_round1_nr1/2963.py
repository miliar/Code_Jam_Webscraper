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
		string res="";
		res+=cad[0];
		char p=cad[0];
		for(int i=1;i<cad.size();i++){
			if(p>cad[i])
				res+=cad[i];
			else
				res=cad[i]+res,p=cad[i];
		}
		printf("Case #%d: ",cases++);
		cout<<res<<endl;
	}
	return 0;
}

