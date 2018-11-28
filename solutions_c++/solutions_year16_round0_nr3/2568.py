#include <bits/stdc++.h>
using namespace std;

string comp(int a){
	
	string s;
	
	int i;
	
	for(i = 0; i < 14; i++){
		s+= a % 2 + '0';
		a/=2;
	}
	
	s+='1';
	
	reverse(s.begin(),s.end());
	
	s+='1';
	
	return s;
	
}

vector<long long> check(string s){
	
	vector<long long> vec, emp;
	
	long long res, i, j, k;
	string c;
	bool b;
	for(i = 2; i <= 10; i++){
		res = 0;
		b = false;
		for(j = 0; j < 16; j++)
			if(s[16 - j - 1] == '1')
				res += pow(i, j);
		
		for(k = 2; k*k <= res; k++){
			if(res %k == 0){
				vec.push_back(k);
				b = true;
				break;
			}
		}
		
		if(!b)
			return emp;
		
	}
	
	return vec;
	
	
}



int main(){
	
	//freopen("B-large (1).in","r", stdin);
	freopen("myfile1.txt","w", stdout);
	long long t, i, j, k, q, n, m;
	long long a, res;
	string s, c;
	cin>>q;
	
	vector<long long> v;
	
	for(t = 1; t <= q; t++){
	
			
			
		cin>>n>>m;
		
		cout<< "Case #"<<t<<": "<<endl;	
		
		for(i = 0; m; i++){
			s = comp(i);
			
			//cout<<s<<endl;
			//cin>>n;
			v = check(s);
			if(v.size()!= 0){
				cout<<s<<" ";
				for(n = 0; n < 9; n++)
					cout<<v[n]<<" ";
				cout<<endl;
				m--;
			}
			
			
						
			
		}
		
				
	}
	
	
	return 0;
}
