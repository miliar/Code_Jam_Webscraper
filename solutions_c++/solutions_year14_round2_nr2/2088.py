#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<vector>

using namespace std;

int main(){

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	scanf("%d",&T);
	for(int caseNo =1;caseNo<=T;caseNo++){
		int A,B,K,win=0;
		cin>>A;
		cin>>B;
		cin>>K;
		for(int i=0;i<A;i++){
			for(int j=0;j<B;j++){
				if((i&j)<K)
					win++;
			}
		}
		cout<<"Case #"<<caseNo<<": "<<win<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}