#include <iostream>
#include <fstream>
#include<bits/stdc++.h>
using namespace std;
#define rr 		freopen("input.txt", "r", stdin)
#define wr 		freopen("output.txt", "w", stdout)

int main() {
    ios::sync_with_stdio(0);
    rr;
    wr;
	srand(time(NULL));
	int N,j,T,i,k=0;
	cin>>T>>N>>j;
	cout<<"Case #1:"<<endl;
	if(N%2==0){
	//	srand(time(NULL));
		while(j--){
			int a[N]={0};
			a[0]=1;
			a[N-1]=1;
			for(i=1;i<N-1;i++){
				if(i%2==0)
				a[i]=rand()%2;	
				if(a[i]==1){
					k++;
				}
			}
			for(i=1;i<=k;i++){
				int l;
				l=2*(rand()%((N-2)/2))+1;
				if(a[l]==1){
					i--;
				}
				else
				 a[l]=1;
			}
			for(i=0;i<N;i++){
				cout<<a[i];
			}
			for(i=3;i<=11;i++)
		  		cout<<" "<<i;
			cout<<endl;
			k=0;
		}
	}
	else{
	//	srand(time(NULL));
		while(j--){
			int a[N]={0};
			a[0]=a[N-1]=1;
			for(i=1;i<N-1;i++){
				if(i%2==0)
				a[i]=rand()%2;	
				if(a[i]==1){
					k++;
				}
			}
			k+=2;
			for(i=1;i<=k;i++){
				int l;
				l=2*(rand()%((N-1)/2))+1;
				if(a[l]==1){
					i--;
				}
				else
				 a[l]=1;
			}
			for(i=0;i<N;i++){
				cout<<a[i];
			}
			for(i=3;i<=11;i++)
		  		cout<<" "<<i;
			cout<<endl;
			k=0;
		}
	}
	return 0;
}

