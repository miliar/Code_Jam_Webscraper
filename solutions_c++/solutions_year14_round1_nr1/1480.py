#include <cstdio>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <set>
#include <map>

using namespace std;


vector <string> v;
vector <string> dev;
int n,l;
int cases=0;

int count (int i){
	int cont=0;
	for (int j=0;j<l;++j){
		if (i & (1<<j))
		cont++;
	}
	
	return cont;
}

bool swit (vector <string> &nuevo, int mask){
	
	for (int i=0;i<l;++i)
	if (mask & (1<<i)){
		for (int k=0;k<nuevo.size();++k){
			
			if (nuevo[k][i]=='0')
			nuevo[k][i]='1';
			else
			nuevo[k][i]='0';
		}
	}
	
	sort (nuevo.begin(),nuevo.end());
	
	return (nuevo==dev);
	
}

int main(){
int t;
cin>>t;


while (t--){
	v.clear();
	dev.clear();
	cin>>n>>l;
	for (int i=0;i<n;++i){
		string a;
		cin>>a;
		v.push_back(a);
	}
	for (int i=0;i<n;++i){
		string a;
		cin>>a;
		dev.push_back(a);
	}
	sort (dev.begin(),dev.end());
	vector <string> nuevo;
	int cont=0x3f3f3f3f;
	for (int i=0;i<1<<l;++i){
		nuevo=v;
		bool k=swit(nuevo,i);
		if (k){
			cont=min(cont,count(i));
		}
	}
	cases++;
	printf("Case #%d: ",cases);
	if (cont==0x3f3f3f3f)
	printf("NOT POSSIBLE\n");
	else
	printf("%d\n",cont);
}


return 0;
}

