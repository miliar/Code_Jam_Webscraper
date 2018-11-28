#include<iostream>

using namespace std;
// i->2 j->3 k->4
int change(char c){
	return c-'i'+2;
}
int abs(int x){
	if(x>0)return x;
	else return -1*x;
}
int cal[4][4]={
	{1,2,3,4},
	{2,-1,4,-3},
	{3,-4,-1,2},
	{4,3,-2,-1}
};
int div[4][4]={
	{1,-2,-3,-4},
	{2,1,4,-3},
	{3,-4,1,2},
	{4,3,-2,1}
};
int d[300000];
int se(int l,int r){
	

	if(l-1>=0){
		if(d[r]*d[l-1]<0)return -1*div[abs(d[r])-1][abs(d[l-1])-1];
		else return div[abs(d[r])-1][abs(d[l-1])-1];
	}
	else return d[r];
}
int main(){
	int t;
	cin>>t;
	for(int l=1;l<=t;l++){
		fill(d,d+300000,0);
		int L,X;
		cin>>L>>X;
		for(int i=0;i<L;i++){
			char c;
			cin>>c;
			for(int j=0;j<X;j++)d[j*L+i]=change(c);
		}
		for(int i=1;i<L*X;i++){
			if(d[i-1]>0)d[i]=cal[d[i-1]-1][d[i]-1];
			else{
				 d[i]=-1*cal[abs(d[i-1])-1][d[i]-1];
			}
		}
		bool ans=false;
		for(int i=0;i<L*X;i++){
			if(se(0,i)!=2)continue;
			for(int j=i+1;j<L*X;j++){
				if(se(i+1,j)!=3)continue;
				if(se(j+1,L*X-1)!=4)continue;
				ans=true;
			}
		}
		cout<<"Case #"<<l<<": ";
		if(ans)cout<<"YES"<<endl;
		else cout<<"NO"<<endl;
	}
}
