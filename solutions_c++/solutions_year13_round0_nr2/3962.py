#include<iostream>
using namespace std;


int main()
{
	int t;
	cin>>t;
	int mat[101][101];
	for(int i=0;i<t;i++) {
		int n,m;
		cin>>n>>m;
		for(int j=0;j<n;j++) {
			for(int k=0;k<m;k++) {
				cin>>mat[j][k];
			}
		}

		int overall_res=0;
		for(int j=0;j<n;j++) {
			for(int k=0;k<m;k++) {
				int temp=mat[j][k];
				int result=0;
				for(int l=0;l<m;l++) {
					if(mat[j][l]>temp) {
						result=1;
						break;
					}
				}
				if(result==0) {
					continue;
				}	

				
				result=0;
				for(int l=0;l<n;l++) {
					if(mat[l][k]>temp) {
						result=1;
						break;
					}
				}
				if(result==0) {
					continue;
				}
				overall_res=1;
				break;
			}
		}

		
		if(overall_res==1)
			cout<<"Case #"<<i+1<<": NO\n";	
		else		
			cout<<"Case #"<<i+1<<": YES\n";		

	}
	return 0;
}