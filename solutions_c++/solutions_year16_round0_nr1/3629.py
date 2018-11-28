#include<cstdio>
#include<iostream>

using namespace std;

int countDigits(int v) {
	int res=0;
	if(v<0) v=-v;
	while(v!=0) {
		res|=1<<(v%10);
		v/=10;
	}
	return res;
}

int main(int argc, char** argv) {
	int tsts;
	
	cin>>tsts;
	
	for(int t=1;t<=tsts;++t) {
		int val;
		cin>>val;
		
		cout<<"Case #"<<t<<": ";
		if(val==0) {
			cout<<"INSOMNIA";
		} else {
			int res=0;
			for(int i=1;;++i) {
				//cout<<"Processing: "<<(val*i)<<" ";
				res|=countDigits(val*i);
				if(res==((1<<10)-1)) {
					cout<<(val*i);
					break;
				}
			}
		}
		cout<<endl;
	}
	
	return 0;
}