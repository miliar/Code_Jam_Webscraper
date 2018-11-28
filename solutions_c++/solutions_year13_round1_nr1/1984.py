#include<iostream>
#include<vector>

using namespace std;

int main(){
	int ncses,r,i,j,t,count,cn,k,req;
	cin>>ncses;
	cn=1;
	while(ncses-->0){
		cin>>r>>t;
		i=1;	j=0;	count=0;	k=1;	req=((r+i)*(r+i)-(r+j)*(r+j));
		while(t>=req){
			count++;
			t -= ((r+i)*(r+i)-(r+j)*(r+j));
			i = i+2;	j = j + 2*k;
			req = ((r+i)*(r+i)-(r+j)*(r+j));
			
		}
		cout<<"Case #"<<cn<<": "<<count<<endl;
		cn++;
	}
}

