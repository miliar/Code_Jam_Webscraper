#include<iostream>
using namespace std;
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
using namespace std;

int main(){

	int i,j,n,m,t,a[100][100],rows[100],cols[100],r,c;
	bool check;
	cin>>t;
	for(int counter=1;counter<=t;counter++){
		check=true;
		scanf("%d %d",&n,&m);
		for(i=0;i<n;i++)
			rows[i]=0;
		for(i=0;i<m;i++)
			cols[i]=0;

		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				scanf("%d",&a[i][j]);
				rows[i] = max((rows[i]),(a[i][j]));
				cols[j] = max((cols[j]),(a[i][j]));
			}
		}

		for(i=0;i<n && check==true;i++){
			for(j=0;j<m && check==true;j++)
				if(a[i][j]<min((rows[i]),(cols[j]))) check=false;
		
			
		}
		if(check==true) cout<<"Case #"<<counter<<": YES\n";
		else cout<<"Case #"<<counter<<": NO\n";
	}
	return 0;
}
















	