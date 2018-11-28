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
	
	freopen("D-small-attempt1.in","r", stdin);
	freopen("myfile1.txt","w", stdout);
	long long t, i, j, k, q, n, m;
	long long a, res;
	string s, c;
	cin>>q;
	
	vector<long long> v;
	
	for(t = 1; t <= q; t++){
	
			
			
		cin>>n>>m;
		cin>>n;
		
			
		j = 1;
		for(i = 0; i <m; i++)
			j = j * n;
		
		k = j / n;
		
		
		
		
		cout<< "Case #"<<t<<": ";
	
		for(i = 0; i < n; i++){
		
			res= 1 + i*k;
			cout<<res<<" ";
		}
		cout<<endl;
				
	}
	
	
	return 0;
}
