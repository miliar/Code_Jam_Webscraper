#include <iostream>
using namespace std;
int main(){
	int n,m,p,ans,cp=0,q=0;
	cin>>n;
	while(n--){
		q++;
		int a[10];
		for(int i=0;i<10;i++){
			a[i]=1;
		}
		cin>>m;
		int i=1,kk=0;
		while(1){
			cp++;
			if(cp==1000){
				kk=1;
				break;
			}
			p=m*i;
			ans=p;
			i++;
			while(p>0){
				int num=p%10;
				a[num]=0;
				p=p/10;
			}
			if(ans==0){
				a[ans]=0;
			}
			int c=0;
			for(int j=0;j<10;j++){
				if(a[j]==0){
					c++;
				}
			}
			if(c==10){
				break;
			}
		}
		if(kk==1){
			cout<<"Case #"<<q<<": "<<"INSOMNIA"<<endl;
		}
		else{
			cout<<"Case #"<<q<<": "<<ans<<endl;
		}
	}
}