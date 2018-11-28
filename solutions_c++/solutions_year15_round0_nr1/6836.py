#include <bits/stdc++.h>

using namespace std;

int main(){
	
	int t; cin>>t;
	int casos=1;
	while (t--){
	printf("Case #%d: ",casos++);
	string x;
	int n;
	cin>>n>>x;
	
	int cont=0;
	int sum=0;
	for (int i=0;i<x.size();++i){
		int y= x[i]-'0';
				
		if (i>sum){

			cont+=i-sum;
			sum+=i-sum;
			sum+=y;
			
		}else{
			sum+=y;
		}
	}
	
	printf("%d\n",cont);
	
	}
	
	return 0;
}
