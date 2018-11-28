#include<iostream>
using namespace std;

int t,n,p[27],s,l,lp,l2;

void g(){
	for(int j=1; j<=n; j++){
		if(p[j]>p[lp]){
			lp=j;
		}
	}
	l2=0;
	p[l2]=-1;
	for(int j=1; j<=n; j++){
		if(p[j]==p[lp] && j!=lp){
			l2=j;
		}
	}
}

void check(){
	if(2*p[lp]>s)
	{
		cout<<"ERROR";
	}
}
int main(){
	
	cin>>t;
	for(int i=1; i<=t; i++){
		cin>>n;
		s=0;
		l=0;
		for(int j=1; j<=n; j++){
			cin>>p[j];
			s+=p[j];
		}
		g();
		cout<<"Case #"<<i<<":";
		while(s>0){
			if(p[lp]==p[l2]){
				l=0;
				for(int j=1; j<=n; j++){
					if(p[j] && j!=lp && j!=l2){
						l=1;
					}
				}
				if(!l){
					cout<<" "<<char(64+lp)<<char(64+l2);
					p[lp]--;
					p[l2]--;
					s-=2;
					g();
					check();
					continue;
				}
				
			}
			
			if(s>3){
					cout<<" "<<char(64+lp);
					p[lp]--;
					s--;
					g();
			}else if(s==2){
				cout<<" ";
				for(int j=1; j<=n; j++){
					if(p[j]){
						cout<<char(64+j);
						p[j]--;
						s--;
						g();
					}
				}
			}else if(s==3){
				for(int j=1; j<=n; j++){
					if(p[j]>1){
						cout<<" "<<char(64+j);
						p[j]--;
						s--;
						g();
					}
				}
				if(s==3){
					cout<<" ";
					for(int j=1; j<=n; j++){
						if(p[j]){
							cout<<char(64+j);
							p[j]--;
							s--;
							g();
							break;
						}
					}
				}
			}
			check();
			
		}
		cout<<endl;	
	}
	return 0;
}
