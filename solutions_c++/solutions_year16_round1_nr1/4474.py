#include<bits/stdc++.h>
using namespace std;
int main(){
	#ifndef ONLINE_JUDGE
   		freopen("inp.txt","r",stdin);
    	freopen("out.txt","w",stdout);
    #endif
	int t;
	cin>>t;
	int k=1;
	while(t--){
		char s[1005];
		int a[1005]={0};
		cin>>s;
		a[0]=0;
		int f=0;
		for(int i=1;i<strlen(s);i++){
			if((int)s[i]>=(int)s[f]){
				for(int j=i;j>0;j--){
					a[j]=a[j-1];
				}
				a[0]=i;
				f=i;
			}
			else{
				a[i]=i;
			}
		}
		cout<<"Case #"<<k<<": ";
		for(int i=0;i<strlen(s);i++)
		cout<<s[a[i]];
		cout<<endl;
		k++;
	}
	return 0;
}
