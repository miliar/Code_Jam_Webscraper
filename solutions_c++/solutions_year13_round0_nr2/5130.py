#include <iostream>
using namespace std;
int n,m;
int a[101][101];
bool shana(int cs){
	scanf("%d%d",&n,&m);
	for (int i=0;i<n;i++)
		for (int j=0;j<m;j++)
			scanf("%d",&a[i][j]);
	int U[101],L[101];
	for (int i=0;i<n;i++)
		L[i]=100;
	for (int i=0;i<m;i++)
		U[i]=100;		
	for (int p=0;p<n+m;p++){
		int min=1000,mini=-1,minj=-1;
		int dir=-1;
		for (int i=0;i<n;i++){
			if( L[i]<100 ) continue;
			for (int j=0;j<m;j++){
				if (U[j]<100) continue;
				if (a[i][j]<min){
					min=a[i][j];
					mini=i;
					minj=j;
				}
			}
		}
		//cout<<mini<<" "<<minj<<endl;
		if (min==1000)
			return true;
		bool flag=true;
		for (int i=0;i<n;i++)
			if (a[i][minj]>a[mini][minj])
				flag=false;
		if (flag)
			U[minj]=a[mini][minj];
		if (!flag) {
			flag=true;
			for (int j=0;j<m;j++)
				if (a[mini][j]>a[mini][minj])
					flag=false;	
			if (flag)
				L[mini]=a[mini][minj];
		}	
		/*
		for (int i=0;i<n;i++)
			cout<<L[i]<<" ";
		cout<<endl;
		for (int j=0;j<n;j++)
			cout<<U[j]<<" ";
		cout<<endl;
		*/
		if (!flag)
			return 0;
	}
	return 1;
}
int main(){
	int cn;
	scanf("%d",&cn);
	for (int cs=1;cs<=cn;cs++){
		printf("Case #%d: %s\n",cs,shana(cs)?"YES":"NO");
	}
	return 0;
}
