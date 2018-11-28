#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;


int main()
{
	int T;
	int N,M;
	int k=0;
	int i,j;

	freopen("I:/B-small-attempt0.in", "r", stdin);
	cin>>T;
	int max;
	int a[101][101];
	bool no=false;
	while(k++<T){
		cin>>N>>M;
		max=0;
		no=false;
		for(i=1;i<=N;++i){
			for(j=1;j<=M;++j){
				cin>>a[i][j];
				if(max<a[i][j]) 
					max=a[i][j];
			}
			a[i][0]=max;
			max=0;
		}
		max=0;
		for(i=1;i<=M;++i){
			for(j=1;j<=N;++j){
				if(max<a[j][i]) 
					max=a[j][i];
			}
			a[0][i]=max;
				max=0;
		}
		for(i=1;i<=N && no==false;++i){
			for(j=1;j<=M;++j){
				if(a[i][j]<a[i][0] && a[i][j]<a[0][j]){
					no=true;
					break;
				}
			}
		}
		cout<<"Case #"<<k<<": ";
		if(no==true)
			cout<<"NO"<<endl;
		else
			cout<<"YES"<<endl;
	
	}//while
	fclose(stdin);
	return 0;
}