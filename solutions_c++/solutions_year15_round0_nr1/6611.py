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



int main(){
	
	freopen ("A-small-attempt0.in","r",stdin);
	freopen ("def","w",stdout);
	
	int t, n, i, j;
	string s;
	int a, b, c;
	vector<int> v;
	cin>>j;
	bool bo[10001];
	
	for(int k = 0; k < j; k++){
		
		cin>>n;
		cin>>s;
		
		int rez = 0;
		t = s[0] - '0';
		
		for(i = 1; i <= n; i++){
			
			if(i > t + rez)
				rez += i - t - rez;
			
			
			t += s[i] - '0';
			
		}
		
		
		cout<<"Case #"<<k+1<<": ";
		cout<<rez<<endl;
	//	cout<<r<<" AAA"<<endl;
	}
	

	return 0;
}
