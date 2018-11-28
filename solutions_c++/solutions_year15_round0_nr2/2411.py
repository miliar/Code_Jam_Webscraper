#include<bits/stdc++.h>
using namespace std;
int main(){
	int i,sum,smax,t,count,temp,j;
	int p[1005],d,m;
	
	#ifndef ONLINE_JUDGE
		freopen("inp","r",stdin);
		freopen("out.txt","w",stdout);
	#endif

	cin>>t;
	count=1;
	while(t--){
		cout<<"Case #"<<count<<": ";
		cin>>d;
		m=-1;
		sum=10000000;
		for(i=0;i<d;i++){
			cin>>p[i];
			if(m<p[i]) m = p[i];
		}
		for(i=1;i<=m;i++){
			temp=0;
			for(j=0;j<d;j++){
				if(p[j]>i){
					temp+=((p[j]-1)/i);
					
				}
			
			}
			temp+=i;
			//cout<<temp<<endl;
			if(sum>temp) sum=temp;
		}
		cout<<sum<<endl;
		count++;
	}
	
return 0;
}
