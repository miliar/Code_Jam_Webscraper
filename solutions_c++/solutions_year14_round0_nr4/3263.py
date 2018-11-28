#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;

int main(){

	int T,n;
	int dewar,war;
	cin>>T;
	getchar();
	for(int num=1; num<=T; ++num){
		cin>>n;
		getchar();
		vector<double> v1(n);
		vector<double> v2(n);
		string line1,line2;
		getline(cin,line1);
		getline(cin,line2);
		stringstream strm1(line1);
		stringstream strm2(line2);
		for(int i=0;i<n;++i){
			strm1>>v1[i];
			strm2>>v2[i];
		}
		//cout<<"ok"<<endl;
		sort(v1.begin(),v1.end());
		sort(v2.begin(),v2.end());
		//cout<<"ok"<<endl;

		int p1=n-1,p2=n-1;
		//cout<<endl<<" debug: "<<v1[p1]<<"  "<<v2[p2]<<endl;
		dewar=0;
		while( p1>=0&&p2>=0 ){
			if(v1[p1]>v2[p2]){
				dewar++;
				--p1;
				--p2;
			}
			else
				--p2;
			
		}
		//cout<<"p2: "<<p2<<endl;
		//dewar=n-p1;
		

		p1=0;
		p2=0;
		while(p2<n){
			while(p2!=n && (v2[p2]<=v1[p1]) ){
				++p2;
			}
			if(p2==n)
				break;
			++p1;
			++p2;
		}
		//cout<<"ok"<<endl;
		war=n-p1;

		cout<<"Case #"<<num<<": "<<dewar<<" "<<war<<endl;
	}
}