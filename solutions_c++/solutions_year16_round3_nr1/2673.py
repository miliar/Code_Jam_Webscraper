#include<bits/stdc++.h>
using namespace std;

int arr[100],danger[100];

int main(){
	
	freopen("input.txt", "r" , stdin);
	freopen ("output.txt","w",stdout);
	
	int t,r,n,i,j;
	scanf("%d",&t);
	for(r=1;r<=t;++r){
		scanf("%d",&n);
		int sum=0;
		for(i=0;i<n;++i) { scanf("%d",&arr[i]); sum+=arr[i]; }
		for(i=0;i<n;++i){
			danger[i]=2*arr[i]-1;
		}
		printf("Case #%d: ",r);
		int people=sum,ref,index; char ch;
		while(people!=0){
			//cout<<people;
			int temp=people-1,count=0,ref=INT_MIN;
			for(i=0;i<n;++i){
				if(arr[i]>ref) {
					ref=arr[i]; index=i;
				}
				if(temp<=2*arr[i]-1){
					ch='A'+i; cout<<ch; ++count; --arr[i];
				}
				if(count==2) break;
			}
			//cout<<count<<endl;
			if(count==0) {
				ch='A'+index; cout<<ch; count=1; --arr[index];
			}
			people-=count;
			cout<<" ";
		}
		cout<<endl;
	}
	
	fclose(stdout);
	return 0;
	
}
