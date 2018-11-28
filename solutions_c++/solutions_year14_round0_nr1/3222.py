#include<algorithm>
#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;
int main(){
	freopen("C.in","r",stdin); 
	freopen("CodeJam.out","w",stdout);
	int n,p,q,ins[4][4],map[4][4],i,j,ans[4],res;
	long cal;
	bool exist[17];
	cin>>n;
	for(int nn=1;nn<=n;nn++){
		cin>>p;--p;
		for(i=0;i<4;++i) for(j=0;j<4;++j) cin>>ins[i][j];
		cin>>q;--q;
		for(i=0;i<4;++i) for(j=0;j<4;++j) cin>>map[i][j];
		
		memset(exist,0,sizeof(exist));
		res = 0;
		for(i=0;i<4;i++) exist[ins[p][i]]=1;
		for(i=0;i<4;i++)
			if(exist[map[q][i]]) ans[res++]=map[q][i];
		printf("Case #%d: ",nn);
		if(res == 0) cout<<"Volunteer cheated!"<<endl; 
		else if(res == 1) cout<<ans[0]<<endl; 
		else cout<<"Bad magician!"<<endl; 
	}
	return 0;
}

