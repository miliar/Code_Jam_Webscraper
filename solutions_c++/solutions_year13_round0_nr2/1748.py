#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
using namespace std;

int n,m;
int a[102][102],flag[102][102];
int rMax[102],cMax[102];

void maxfill(){

	memset(rMax,0,sizeof(rMax));
	memset(cMax,0,sizeof(cMax));

	for(int i=0;i<n;i++){
	
		for(int j=0;j<m;j++){
			rMax[i]=max(a[i][j],rMax[i]);
			cMax[j]=max(a[i][j],cMax[j]);
		}
	}

}
bool isyes(){

	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)
			if(flag[i][j]==0)
				return false;
	return true;
}
bool process(){

	maxfill();
	memset(flag,0,sizeof(flag));
	
	for(int i=0;i<n;i++)
	{
		int mx=rMax[i];
		for(int j=0;j<m;j++)
		if(mx==a[i][j])
			flag[i][j]=mx;
		
	
	}

	for(int i=0;i<m;i++)
	{
		int mx=cMax[i];
		for(int j=0;j<n;j++)
		if(mx==a[j][i])
			flag[j][i]=mx;
		
	
	}
	return isyes();
}
int main(){
	char File[]="B-large";	
	
	char in[100],out[100];
	strcpy(in,File);strcpy(out,File);
	strcat(in,".in");strcat(out,".out");
	freopen(in,"rt",stdin);
	freopen(out,"wt",stdout);
	
	int T,cas=1;
	cin>>T;
	while(T--){

		cin>>n>>m;
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				cin>>a[i][j];

	
		bool f=process();
		printf("Case #%d: ",cas++);
		if(f) printf("YES\n");
		else  printf("NO\n");


	}
	return 0;
}