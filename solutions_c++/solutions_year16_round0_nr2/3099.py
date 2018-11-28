#include <bits/stdc++.h>
using namespace std;




int main(){
	
	freopen("B-large (1).in","r", stdin);
	freopen("myfile1.txt","w", stdout);
	long long t, i, j, k, q, n, m;
	long long a, res;
	string s;
	cin>>q;
	
	for(t = 1; t <= q; t++){
	
			
			
		cin>>s;
		
		n = s.size();
		
		res = 1;
		
		for(i = 1; i < n; i++){
			if(s[i]!=s[i-1])
				res++;
				
		}		
		
		if(s[n-1]=='+')
			res--;
		
		
			cout<< "Case #"<<t<<": "<<res<<endl;	
		
	}
	
	
	return 0;
}
