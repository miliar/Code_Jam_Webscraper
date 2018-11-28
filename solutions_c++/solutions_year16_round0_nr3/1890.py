#include<iostream>
using namespace std;
int T;
int N,J;
#define rep(i,j,k) for(int i=j;i<=k;i++)
int main(){
	//freopen("out","w",stdout);
	cin>>T;
	rep(i,1,T){
		cin>>N>>J;
		cout<<"Case #"<<i<<":"<<endl;
		int cnt=0;
		if(N==16){
			for(int j=3;j<=13;j+=2){
				for(int k=j+2;k<=15;k+=2){
					for(int l=2;l<=12;l+=2){
						for(int m=l+2;m<=14;m+=2){
							if(cnt<J){
								cout<<"1";
								for(int n=2;n<=15;n++){
									if(n==j||n==k||n==l||n==m)
									cout<<"1";
									else 
									cout<<"0";
								}
								cout<<"1 ";
								cout<<"3 2 3 2 7 2 3 2 3"<<endl;
								cnt++;
							}
						}
					}
				}
			}
		}
		if(N==32){
			for(int j=3;j<=29;j+=2){
				for(int k=j+2;k<=31;k+=2){
					for(int l=2;l<=28;l+=2){
						for(int m=l+2;m<=30;m+=2){
							if(cnt<J){
								cout<<"1";
								for(int n=2;n<=31;n++){
									if(n==j||n==k||n==l||n==m)
									cout<<"1";
									else 
									cout<<"0";
								}
								cout<<"1 ";
								cout<<"3 2 3 2 7 2 3 2 3"<<endl;
								cnt++;
							}
						}
					}
				}
			}
		}
	}
}
