#include<bits/stdc++.h>
using namespace std;

int main(){
	ios::sync_with_stdio(false);
    freopen("A-large (1).in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	string str;
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>str;
		int n=str.length();
		int A[91];
		int num[10];
		
		memset(A,0,sizeof(A[0])*91);
		memset(num,0,sizeof(num[0])*10);
		
		for(int j=0;j<n;j++)
			A[str[j]]++;
			
		if(A[90]>0){
			num[0]=A[90];
			A[69]-=A[90];
			A[82]-=A[90];
			A[79]-=A[90];
		}
		if(A[87]>0){
			num[2]=A[87];
			A[84]-=A[87];
			A[79]-=A[87];
		}
		if(A[85]>0){
			num[4]=A[85];
			A[70]-=A[85];
			A[79]-=A[85];
			A[82]-=A[85];
			
		}
		
		if(A[88]>0){
			num[6]=A[88];
			A[83]-=A[88];
			A[73]-=A[88];
		}
		
		if(A[71]>0){
			num[8]=A[71];
			A[69]-=A[71];
			A[73]-=A[71];
			A[72]-=A[71];
			A[84]-=A[71];
			
		}
		
		if(A[70]>0){
			num[5]=A[70];
			A[73]-=A[70];
			A[86]-=A[70];
			A[69]-=A[70];
			
		}
		
		if(A[83]>0){
			num[7]=A[83];
			A[69]-=2*A[83];
			A[78]-=A[83];
		}
		if(A[73]>0){
			num[9]=A[73];
			A[78]-=2*A[73];
		}
		if(A[72]>0)
			num[3]=A[72];
		if(A[79]>0)
			num[1]=A[79];
		
		cout<<"Case #"<<i<<": ";
				for(int k=0;k<10;k++){
					char x=k+48;
					for(int l=0;l<num[k];l++)
						cout<<x;
				}
				cout<<endl;
		
	}
}

