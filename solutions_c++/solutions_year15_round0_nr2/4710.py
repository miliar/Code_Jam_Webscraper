#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <stdio.h>
#include <map>
using namespace std;


int f(vector<int> v, int p){
	
	v.push_back(0);
	
	vector<int>::iterator it = max_element(v.begin(),v.end());
	
	
	
	if(*it < 4)
		return *it;
	
	if(p == 6)
		return 9;
	
	int i, n, mn;
	vector<int> v2;
	n = *it;
	
	for(i = 0 ; i < v.size()-1; i++)
		v2.push_back(max(0, v[i] - 1));
	
	mn = 1+f(v2, p + 1);
	
	
	

	
	for(i = 1; i <= n/2;i++){
		
		v[v.size() - 1] = i;
		*it -= i;
	//    cout<<i<<" "<<*it<<endl;
		mn = min(mn, f(v, p + 1)+1);
		*it += i;
	//	cout<<i<<" "<<*it<<endl;
	}
		
		
	return mn;
	
}



int main(){
	
	freopen ("B-small-attempt1.in","r",stdin);
	freopen ("def","w",stdout);
	
	int t, n, i, j;
	string s;
	int a, b, c;
	vector<int> v;
	cin>>j;
	bool bo[10001];
	int rez;
	
	vector<int> v1;
	
	
	for(int k = 0; k < j; k++){
		v1.clear();
		cin>>n;
		
		for(i = 0; i < n; i++){
			
			cin>>t;
			v1.push_back(t);
			
		}
		
		rez = min(f(v1, 0), 9);
		
		cout<<"Case #"<<k+1<<": ";
		cout<<rez<<endl;
	//	cout<<r<<" AAA"<<endl;
	}
	

	return 0;
}
