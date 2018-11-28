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
	string a,nuevo,x,y,z;
	for(int j=1;j<=n;j++){
		cin >> a;
		stringstream ss;
		char c = a[0];
		ss << c;
		ss >> nuevo;
		for(int i=1;i<a.size();i++){
			stringstream s1;
			char c1 = a[i];
			s1 << c1;
			s1 >> z;
			x= nuevo+z;
			y= z+nuevo;
			if( x.compare(y)>0 ){
				nuevo = x;
			}
			else
				nuevo = y;
			//cout <<z<<" " <<x<<" "<<y<<" "<<nuevo<<endl;	
		}
		cout <<"Case #"<<j<<": "<<nuevo<<endl;
	}
}
