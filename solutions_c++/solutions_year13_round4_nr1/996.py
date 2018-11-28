#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<iomanip>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
//setprecision
using namespace std;
class W{
	public:
//W* l;
//W* r;
int l;
int d;
int y;
};


class ind{
	public:
	ind():i(-1){
		
	}
	int i;
};

class pa{
	public:

	long long int o;
	long long int e;
	long long int p;
};
bool compare(const pa w1,const pa w2){
	return w1.o<w2.o;
}
int main(){
	int TT;
	cin>>TT;

	map<int,int> mp;

	long long int n;
	int m;
	int s;
	pa p[1100];
	int a[4000];
	int b[4000];
	int c[4000];
	int pm[4000];
	int counter;
	int t;
	const long long int MO=1000002013;

	long long int tmp;

	for(int T=1;T<=TT;++T){
		cout<<"Case #"<<T<<": ";
		cin>>n>>m;

		long long int k;
		int cost1=0;
		
		for(int i=0;i<m;++i){
			cin>>p[i].o>>p[i].e>>p[i].p;	
			a[i*2]=p[i].o;
			a[i*2+1]=p[i].e;
			k=p[i].e-p[i].o;
			tmp=(2*n-k+1)*k/2%MO;
				tmp=tmp*p[i].p%MO;
			cost1=(cost1+tmp)%MO;

			
		}
		sort(a,a+(2*m));
		counter=0;	
		for(int i=0;i<2*m;++i){
			if(i>0&&a[i]==a[i+1])
				continue;
			mp[a[i]]=counter;
			pm[counter]=a[i];
			++counter;
		}
		s=counter;

		sort(p,p+m,compare);
		for(int i=0;i<s;++i){
			b[i]=0;
			c[i]=0;
		}
		int oi;
		long long int cost=0;
		int ei;
		int ni=0;
		for(int l=0;l<s;++l){
			//cerr<<pm[l]<<"!!!"<<endl;
			for(;ni<m;++ni){
				if(p[ni].o==pm[l]){
					b[mp[p[ni].e]]+=p[ni].p;
					c[mp[p[ni].o]]+=p[ni].p;
				}
				else
					break;
			}
			//ei=mp[p[i].o];
			ei=l;
			//cerr<<b[ei]<<"==="<<endl;
			for(int j=ei;j>=0;--j){
				
				//cerr<<"   "<<pm[j]<<endl;
				if(c[j]==0)
					continue;
				if(c[j]>=b[ei]){
					c[j]-=b[ei];
					k=pm[l]-pm[j];
					tmp=(2*n-k+1)*k/2%MO;
						tmp=tmp*b[ei]%MO;//TODO
					cost=(cost+tmp)%MO;
					b[ei]=0;
					//cerr<<k<<endl;
					break;
				}
				else{
					b[ei]-=c[j];
					k=pm[l]-pm[j];
					tmp=(2*n-k+1)*k/2%MO;
						tmp=tmp*c[j]%MO;//TODO
					cost=(cost+tmp)%MO;
					c[j]=0;
					//cerr<<k<<endl;
				}
			}
		}
		//cout<<cost1<<endl;
		//cout<<cost;
		cout<<(cost1-cost)%MO;





		cout<<"\n";
	}
	return 0;
}




//int compare(const void* a,const void* b){
//	//return *((int*)a)-*((int*)b);
//	return ((W*)a)->d-((W*)b)->d;
//}
//qsort(a,10,sizeof(int),compare);
