#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<set>
#include<map>
#include<queue>
#include<cstring>
#include<stack>
#include<fstream>
using namespace std;
int main(){
	ifstream cin;
	ofstream cout;
	cin.open("C:\\Users\\hp\\Downloads\\5.in");
	cout.open("C:\\Users\\hp\\Downloads\\out.txt");
	int t,i,x=1;
	cin>>t;
	while(t--){
	int smax,c=0,p=0;
	string s;
	cin>>smax;
	cin>>s;
	for(i=0;i<smax+1;i++){
		c+=(s[i]-'0');
		if(i>=c){
		p+=(i+1-c);
		c++;
		}
		
	}
	cout<<"Case #"<<x<<": "<<p<<endl;
	x++;
	}
	return 0;
}