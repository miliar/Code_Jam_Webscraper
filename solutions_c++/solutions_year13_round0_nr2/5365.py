#include <iostream>
#include <fstream>
using namespace std;
ofstream fout("haha.out");
int main() {
	int T,M,N;
	int i,j,t,a[10][10],b[10][10];
	bool flag,line;
	cin>>T;
	for (t=1;t<=T;++t){
		cin>>M>>N;
		flag = true;
		for(i=0;i<M;++i) {
			line = true;
			for(j=0;j<N;++j){
				cin>>a[i][j];
				if ( a[i][j]==2 ) line = false;
				b[i][j]=2;
			}
			if (line) {
				for (j=0;j<N;++j)
					b[i][j]=1;
			}
		}
		for (j=0;j<N;++j) {
			line = true;
			for (i=0;i<M;++i) {
				if (a[i][j]==2) line = false;
			}
			if (line) {
				for (i=0;i<M;++i)
				b[i][j]=1;
			}
		}
		for(i=0;i<M;++i) {
			for(j=0;j<N;++j){
				if (a[i][j]!=b[i][j]) {
					flag=false;
					break;
				}
				//cout<<b[i][j]<<' ';
			}//cout<<endl;
			if (flag==false) break;
		}
		cout << "Case #"<<t<<": ";
		if (flag) {
			cout << "YES\n";
		}else cout<<"NO\n";
	}
}
