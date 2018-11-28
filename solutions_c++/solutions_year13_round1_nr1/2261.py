#include<iostream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<fstream>
#include<set>
#include<iomanip>
#include<string>
using namespace std;
long long t,r,w,c=0;
//double pi = 3.1415926535897;
int main(){
	ifstream cin("A-small-attempt1.in");
	ofstream cout("out.txt");
	cin>>w;
	for(long long gr = 1; gr <= w; gr++){
		cin>>r>>t;
		//t*=pi;
		c = 0;
		while( ((r+1)*(r+1) - r*r) <= t){
			t -= (r+1)*(r+1) - r*r;
			c++;
			r+=2;
		}
		cout<<"Case #"<<gr<<": "<<c<<endl;
	}

//	system("pause");
	return 0;
}