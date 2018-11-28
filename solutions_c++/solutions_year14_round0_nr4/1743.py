#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){

	int t;
	int k=1;
	cin>>t;
	while(k<=t){
		int n;
		cin>>n;
		vector<double> a(n),b(n);
		
		for(int i=0;i<n;++i){
			cin>>a[i];
		}
		for(int i=0;i<n;++i){
			cin>>b[i];
		}
		sort(a.begin(),a.end());
		sort(b.begin(),b.end());

/*		for(int i=0;i<n;++i)
			cout<<a[i]<<" ";
		cout<<endl;
		for(int i=0;i<n;++i)
			cout<<b[i]<<" ";*/

		int fp=0,ep=n-1,ep2=n-1,ep3=n-1;
		int score=0,score2=0;
		int m=0;
		while(m<n){
			if(a[ep]>b[ep2]){
				++score;
				--ep;
				--ep2;
			}
			else{
				--ep2;
				++fp;

			}
			++m;

		}
		fp=0;ep=n-1;ep2=n-1;
		int l=0;
		while(l<n){
		//	cout<<a[ep]<<" "<<b[ep2]<<endl;
			if(a[ep]>b[ep2]){
				--ep;
				++score2;
				
			}
			else{
				--ep;
				--ep2;
			}
			++l;
		}
		cout<<"Case #"<<k<<": "<<score<<" "<<score2<<endl;
		++k;

	}


}
