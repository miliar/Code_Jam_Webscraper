#include <iostream>
using namespace std;
int main(){
	long long a,b,n,m,tmp,p=0;
	bool cek=true;
	cin>>n;
	for (int i=1;i<=n;i++){
		cin>>a;
		if(a==0){
			cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		p=0;
		b=0;
		int caci[50]{};
		cek=true;
		while (cek){
			p++;
			b=a*p;
			while (b>0){
				tmp=b%10;
				caci[tmp]+=1;
				b=b/10;
			}
			
			for (int j=0;j<=9;j++){
				cek=false;
				if (caci[j]<1){
					cek=true;
					break;
				}
			}
		}
		cout<<"Case #"<<i<<": "<<a*p<<endl;
	}
}
