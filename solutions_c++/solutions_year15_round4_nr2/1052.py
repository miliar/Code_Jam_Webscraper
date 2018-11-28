#include<iostream>
using namespace std;

double rate[100], temple[100];

int main(){
		freopen("in.txt","r",stdin);
		freopen("out.txt","w",stdout);
	int nn,r=1,n,i,j,cnt;
	double v, x, fs, ans;
	scanf("%d",&nn);
	while(nn--){
		cout<<"Case #"<< r <<": ";
		r++;
		cin>>n>>v>>x;
		for(i=0;i<n;i++) {
			cin>>rate[i]>>temple[i];
		}
		if( n== 1 ) {
			if( temple[0] != x ) cout<<"IMPOSSIBLE"<<endl;
			else cout<<v/rate[0]<<endl;
		} else if( n==2 ) {
			if( temple[1] < temple[0] ) {
				swap(  temple[1] , temple[0] );
				swap( rate[1], rate[0] );
			}
			if( temple[1] < x || temple[0] > x ) {
				cout<<"IMPOSSIBLE"<<endl;
			} else if( temple[0] == x ) {
				if( temple[1] == x ) {
					cout<<v/(rate[0]+rate[1])<<endl;
				} else {
					cout<<v/rate[0]<<endl;
				}
			} else if( temple[1] == x ) {
				cout<<v/rate[1]<<endl;
			} else {
				fs =   temple[1]-temple[0];
				cout.precision(8);
				cout<<fixed<<max( v * (temple[1]-x) / (fs * rate[0]), v * (x-temple[0]) / (fs * rate[1]) )<<endl;
				//printf("%.6lf\n",max( v * (temple[1]-x) / (fs * rate[0]), v * (x-temple[0]) / (fs * rate[1]) ));
			}
		}
	}
	return 0;
}
