#include <iostream>
#include <deque>

using namespace std;

#define ff(i,n) for(i=0;i<n;i++)
#define dq deque<double>

dq input(int N){
	int j,k,p;
	double t;
	dq n(N);
	ff(j,N)	cin>>n[j];
	ff(j,N){
		double min=n[j];
		p=-1;
		for(k=j+1;k<N;k++){
			if(n[k]<min){
				min=n[k];
				p=k;
			}
		}
		if(p!=-1){
			t=n[p];
			n[p]=n[j];
			n[j]=t;
		}
	}
	return n;
}

bool check(dq a, dq b){
	int i;
	ff(i,a.size())	if(a[i]<b[i])	return true;
	return false;
}

void print(dq a){
	int i;
	ff(i,a.size())	cout<<a[i]<<" ";
	cout<<endl;
}

int main(){
	int T,i=1;
	for(cin>>T;T--;i++){
		int N;
		cin>>N;
		dq n=input(N),k=input(N);
		int x=0,y=0,res=0;
		while(x<N&&y<N){
			if(k[y]>n[x]){x++; y++;}
			else {y++;res++;}
		}
		/*print(n);
		print(k);
		cout<<endl;*/
		while(check(n,k)){
			n.pop_front();
			k.pop_back();
		}
		cout<<"Case #"<<i<<": "<<n.size()<<" ";
		cout<<res<<endl;
	}
	return 1;
}