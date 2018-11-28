#include<bits/stdc++.h>
using namespace std;

int main(){
	freopen("output.txt","w",stdout);
	int T,val=1;
	cin>>T;
	while(T--){
		int k,c,s;
		cin>>k>>c>>s;
		printf("Case #%d: ",val);
		for(int i=1;i<=k;i++)
			printf("%d ",i);
		cout<<endl;
		val++;
	}
	return 0;
}
