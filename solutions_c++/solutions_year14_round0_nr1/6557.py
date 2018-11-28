#include <iostream>

using namespace std;

int main() {

	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);

	int a[4][4],b[4][4],c[17]={0};
	int t,x,y,i,j,l,ans,count;
	
	cin>>t;

	for(l=0;l<t;++l) {

		for(i=1;i<17;++i) c[i]=0;
		cin>>x;
		for(i=0;i<4;++i)
			for(j=0;j<4;++j)
				cin>>a[i][j];
		for(j=0;j<4;++j) c[a[x-1][j]]++;
		cin>>y;
		for(i=0;i<4;++i)
			for(j=0;j<4;++j)
				cin>>b[i][j];
		for(j=0;j<4;++j) c[b[y-1][j]]++;

		ans=1;
		count=0;
		for(i=1;i<17;++i)
			if (c[i]==2) {
				ans=i;
				count++;
			}

		cout<<"Case #"<<l+1<<": ";
		if (count==0) cout<<"Volunteer cheated!"<<endl;
		else if (count==1) cout<<ans<<endl; else cout<<"Bad magician!"<<endl;
	}

	return 0;
}