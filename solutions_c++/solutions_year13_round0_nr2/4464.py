#include<iostream>
using namespace std;

int a[101][101];
int maxr[101];
int maxc[101];
int main(){
	int T,n,m,tmp,done;
	cin>>T;
	for(int i=0;i<T;i++){
		done=0;
		cin>>n>>m;
		for(int j=0; j<n;j++){
			for(int k=0;k<m;k++)	{	cin>>a[j][k];	}	}		//input
			
		//for(int j=0; j<n;j++){//print
		//	for(int k=0;k<m;k++)	cout<<a[j][k]<<' ';
		//	cout<<endl;	}		
		
		for(int j=0; j<n; j++){//max elt of rows
			maxr[j]=a[j][0];
			for(int k=0; k<m;k++){
				if(a[j][k] > maxr[j]) maxr[j] = a[j][k];
			}
		}
		
		for(int j=0; j<m; j++){//max elt of col.
			maxc[j]=a[0][j];
			for(int k=0; k<n;k++){
				if(a[k][j] > maxc[j]) maxc[j] = a[k][j];
			}
		}
		//print
		//for(int j=0; j<n;j++) cout<<maxr[j]<<' ';
		//cout<<endl;
		//for(int j=0; j<m;j++) cout<<maxc[j]<<' ';
		//cout<<endl;
		//check
		
		for(int j=0; j<n;j++){
			if(done==1) break;
			for(int k=0;k<m;k++)	{
				if(done==1) break;
				tmp=min(maxr[j],maxc[k]);
				if(a[j][k] !=	tmp){
					cout<<"Case #"<<(i+1)<<": NO"<<endl;
					done=1;
					break;
				}
			}
		}
		
		if(done==0)	cout<<"Case #"<<(i+1)<<": YES"<<endl;	
	}
}
//Case #1: YES
//Case #2: NO
