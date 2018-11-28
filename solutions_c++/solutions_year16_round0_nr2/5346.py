#include <iostream>
using namespace std;
int t,k;
long n,i,j,count;
string a;
int main() {
	ios::sync_with_stdio(0);
	cin>>t;
	k=0;
	while(t){
		cin>>a;
		count =0 ;
		++k;
		n=a.size()-1;
		for(i=n;i>=0;--i){
			if(a[i]=='-'){
				a[i]='+';
				for(j=0;j<i;++j){
					if(a[j]=='-')
					a[j]='+';
					else
					a[j]='-';
				}
				++count;
			}
			
		}
		
		cout<<"Case #"<<k<<": "<<count<<endl;
		--t;
	}
	return 0;
}
