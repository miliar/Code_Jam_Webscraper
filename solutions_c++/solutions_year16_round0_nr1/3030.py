#include <bits/stdc++.h>
using namespace std;

bool seen[10];

bool all(){
	
	for(int i = 0; i < 10; i++)
		if(seen[i] == false)
			return false;
	
	return true;
}

void add(int a){
	
	while(a){
		seen[a%10]= true;
		a/=10;
		
	}
	
}


int main(){
	
	freopen("A-large.in","r", stdin);
	freopen("myfile1.txt","w", stdout);
	long long t, i, j, k, q, n, m;
	long long a, res;
	cin>>q;
	
	for(t = 1; t <= q; t++){
		for(i = 0; i < 10; i++)
			seen[i] = false;
			
			
		cin>>a;
		res = -1;
		m = 1;
		for(i = 1; i < 15000; i++){
			m = i * a;
			add(m);
			if(all()){
				res = m;
				break;
			}
				
		}		
		
		if(res != -1)
			cout<< "Case #"<<t<<": "<<res<<endl;	
		else
			cout<< "Case #"<<t<<": INSOMNIA"<<endl;
	}
	
	
	return 0;
}
