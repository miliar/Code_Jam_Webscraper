#include <iostream>
#include <cstdio>

using namespace std;

int main(){
freopen("in.txt","r",stdin);
freopen("out.out","w",stdout);
int t;cin>>t;
int a[4][4],b[4][4];
for(int i=0;i<t;i++){
int count=0;int res;
	int c1;cin>>c1;c1--;for(int j=0;j<4;j++)for(int k=0;k<4;k++)cin>>a[j][k];
	int c2;cin>>c2;c2--;for(int j=0;j<4;j++)for(int k=0;k<4;k++)cin>>b[j][k];
	for(int j=0;j<4;j++){
		for(int k=0;k<4;k++){
			//cout<<a[c1][j]<<b[c2][k]<<"***";
			if(a[c1][j]==b[c2][k])
			count++,res=a[c1][j];
		}
	}
	 cout<<"Case #"<<i+1<<": ";
	if(count==1)cout<<res;
	else if (count>1)cout<< "Bad magician!";
	else cout<<"Volunteer cheated!";
	cout<<endl;	 
}

return 0;
}