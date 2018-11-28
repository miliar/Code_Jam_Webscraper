#include <bits/stdc++.h>
using namespace std; 

#define MAX 220 
#define input freopen("in.txt","r",stdin)
#define output freopen("out.txt","w",stdout)
int main(){       
	//input;
	//output;
	int n;
	cin >> n;
	string a;char b;
	for(int j=1;j<=n;j++){
		cin >> a;int cont=0;b=a[0];
		for(int i=1;i<a.size();i++){
			if(b!=a[i]){
				cont++;
				b=a[i];
			}
		}
		if(a[a.size()-1]=='-')
			cont++;
		cout <<"Case #"<<j<<": "<<cont<<endl;
	}
}
