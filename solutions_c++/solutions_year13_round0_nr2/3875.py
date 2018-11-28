#include <iostream>
using namespace std;
int lawn[100][100];
int rawlawn[100][100];
int rowmax[100];
int colmax[100];

void mow(int n,int m,bool rmajor){
	if( rmajor ){
		for(int i=0;i<n;++i){
			for(int j=0;j<m;++j){
				if( rawlawn[i][j] > rowmax[i] )
					rawlawn[i][j]=rowmax[i];
			}
		}
	}else{
		for(int i=0;i<m;++i){
			//cout<<"colmax "<<i<<"= "<<colmax[i]<<endl;
			for(int j=0;j<n;++j){
				if( rawlawn[j][i] > colmax[i] )
				rawlawn[j][i]=colmax[i];
			}
		}
	}
}
void init(int n,int m){
	for(int i=0;i<n;++i){
		for(int j=0;j<m;++j){
			rawlawn[i][j]=100;
		}
	}
}
void display(int n,int m){
	for(int i=0;i<n;++i){
		for(int j=0;j<m;++j){
			cout<<rawlawn[i][j]<<" ";
		}
		cout<<endl;
	}
}
bool compare(int n,int m){
	bool ret=true;
	for(int i=0;i<n;++i){
		for(int j=0;j<m;++j){
			if( rawlawn[i][j] != lawn[i][j] ){
				ret=false;
				break;
			}
		}
	}
	return ret;
}
int main() {
	int t,n,m;

	cin>>t;
	for(int i=1;i<=t;++i){
		cin>>n>>m;
		init(n,m);
		for(int j=0;j<n;++j){
			int max=0;
			for(int k=0;k<m;++k){
				cin>>lawn[j][k];
				if( lawn[j][k] > max)
					max = lawn[j][k];
			}
			rowmax[j]=max;
		}
		for(int j=0;j<m;++j){
			int max=0;
			for(int k=0;k<n;++k){
				if( lawn[k][j] > max)
					max = lawn[k][j];
			}
			colmax[j]=max;
		}
		mow(n,m,true);
		//display(n,m);
		mow(n,m,false);
		//	display(n,m);
		cout<<"Case #"<<i<<": ";
		if( compare(n,m) ){
			cout<<"YES";
		}else{
			cout<<"NO";
		}
		cout<<endl;
	}
	return 0;
}
