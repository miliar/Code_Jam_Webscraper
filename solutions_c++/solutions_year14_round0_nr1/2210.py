#include <iostream>
using namespace std;
#define ff(i,n) for(i=0; i<n; i++)

int main(){
	int T, i=1; 
	cin>>T;
	do{
		int c[4][4], d[4][4];
		int f,n,x,y;
		cin>>f;
		ff(x,4)	ff(y,4)	cin>>c[x][y];
		cin>>n;
		ff(x,4)	ff(y,4)	cin>>d[x][y];
		int res=0,ans;
		ff(x,4)	ff(y,4)	if(c[f-1][x]==d[n-1][y]){	
			res++;
			if(res==1)	ans=c[f-1][x];
		}
		cout<<"Case #"<<i<<": ";
		switch(res){
			case 0: cout<<"Volunteer cheated!";
			break;
			case 1: cout<<ans;
			break;
			default: cout<<"Bad magician!";
		}
		cout<<endl;
	}while(++i<=T);
	return 0;
}