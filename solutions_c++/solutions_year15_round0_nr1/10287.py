#include <iostream>
using namespace std;

int calc(int t){
	int n,frd=0;
	string inp;

	int cumm[10000];
	
	cin>>n;
	cin>>inp;

	for(int i=0; i<=n; i++)
		cumm[i] = 0;
	
	cumm[0] = inp[0]-'0';
	for(int i=1; i<=n; i++){
		if(cumm[i-1] < i && inp[i]-'0'>0){
			frd += i - cumm[i-1];
			cumm[i] = (inp[i]-'0') + cumm[i-1] + frd;
		}else
			cumm[i] = (inp[i]-'0') + cumm[i-1];
	}
	cout<<"Case #"<<t+1<<": "<<frd<<endl;
}

int main(){
	int t,j=0;
	cin>>t;
	while(j<t){
		calc(j);
		j++;
	}	
	return 0;
}