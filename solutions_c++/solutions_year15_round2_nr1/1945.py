#include <bits/stdc++.h>
using namespace std;
 long int pp( long int v, long int m){
	 long int i,t=1;
	for(i=0;i<m;i++){
		t=t*v;
	}
	return t;
}

 long int  reverse( long int k){
	 long int i,ans,temp;
	 long int n=log10(k)+1;
	ans=0;
	for(i=0;i<n;i++){
		temp=k/pp(10,n-1-i);
		ans=ans+(temp)*pp(10,i);
		k=k%pp(10,n-1-i);
	}
	return ans;
}
int main() {
	 long int i,t,curr,n,count,ttp,it,j;

	ifstream if1;
    if1.open("A-small-attempt0.in");
	if1>>t;
	vector<long long int> na;
	for(i=0;i<t;i++){
        if1>>ttp;
        na.push_back(ttp);
	}
	if1.close();

	ofstream of;
    of.open("output.txt");
	for(it=0;it<t;it++){
		n=na[it];
		 long int a[n+5],act[n+5];
		for(j=0;j<=n;j++){
			a[j]=n+1;
			act[j]=n+1;
		}
		a[1]=1;
		act[1]=1;
		curr=1;
		count=1;
		for(i=2;i<=n;i++){
			 long int temp;
			temp=reverse(i);
			act[i]=min(count+1,a[i]);
			if(temp<=n){
				a[temp]=min(a[temp],act[i]+1);
			}
			count=act[i];
		}
		of<<"Case #"<<it+1<<": "<<act[n]<<"\n";
	}
	of.close();
	return 0;
}
