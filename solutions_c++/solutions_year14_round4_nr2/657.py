#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
	
class W{
	public:
	int k;
	int v;
};
bool compare(const W x,const W y){
	return x.v<y.v;
}
int main(){
	int TT;
	cin>>TT;


	int a[1100];
	W b[1100];
	W c[1100];
	W d[1100];
	W e[1100];
	int n;
	for(int T=1;T<=TT;++T){

		cin>>n;
		for(int i=0;i<n;++i){
			cin>>a[i];
			b[i].k=i;
			b[i].v=a[i];
		}	
		sort(b,b+n,compare);
		int g=0;
		int cs=0;
		int ds=0;
		c[cs]=b[n-1];
		++cs;
		int count;
		for(int i=n-2;i>=0;--i){
			count=0;
			for(int j=0;j<cs;++j){
				if(b[i].k>c[j].k)
					++count;
			}
			for(int j=0;j<ds;++j){
				if(b[i].k>d[j].k){
					++count;
				}
			}
			if(count<=cs+ds-count){
				c[cs]=b[i];
				++cs;
			}
			else{
				d[ds]=b[i];
				++ds;
			}
		}
		for(int i=0;i<cs;++i){
			e[i]=c[cs-1-i];
		}
		for(int i=0;i<ds;++i){
			e[cs+i]=d[i];
		}
		count=0;
		for(int i=0;i<n;++i){
			//cout<<e[i].v<<" ";
			for(int j=i+1;j<n;++j){
				if(e[i].k>e[j].k)
					++count;
			}
		}
		
		int ans=count;
		cout<<"Case #"<<T<<": "<<ans<<"\n";



	}
	return 0;
}
