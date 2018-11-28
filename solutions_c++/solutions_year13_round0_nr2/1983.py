#include<iostream>
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int q=0;q<t;q++){
		int n,m;
		cin>>n>>m;
		int row[n];
		int col[m];
		for(int i=0;i<n;i++)
			row[i]=0;
		for(int i=0;i<m;i++)
			col[i]=0;
		int A[n][m];
		bool detect =false;
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				cin>>A[i][j];
				if(row[i]<=A[i][j]){
					row[i]=A[i][j];
					if(col[j]<=A[i][j])
						col[j]=A[i][j];
				} else if(col[j]<=A[i][j])
					col[j]=A[i][j];
				else {
					detect = true;
				}
			}
		}
/*
		for(int i=0;i<n;i++)
			cout<<"row["<<i<<"]="<<row[i]<<endl;
		for(int i=0;i<m;i++)
			cout<<"col["<<i<<"]="<<col[i]<<endl;
*/		

		if(detect==false){
			for(int i=0;i<n&&detect==false;i++){
				for(int j=0;j<m;j++){
					if(A[i][j]<row[i]&&A[i][j]<col[j]) {
						detect = true;
						break;
					}
				}
			}
		}
		cout<<"Case #"<<q+1<<": ";
		if(detect==false)
			cout<<"YES"<<endl;
		else
			cout<<"NO"<<endl;
	}
	return 0;
}
