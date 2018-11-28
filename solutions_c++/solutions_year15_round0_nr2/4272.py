#include<bits/stdc++.h>

using namespace std;

int main(){
	int test;
	cin>>test;
	for(int te=0;te<test;te++){
		int d;
		cin>>d;
		int* p = new int[d];
		
		int max = 0;
		for(int i=0;i<d;i++){
			cin>>p[i];
			if(p[i]>max) max = p[i];
		}

		int res = 0;

		for(int m=1;m<=max;m++){
			int temp = 0;
			for(int j=0;j<d;j++){
				if(p[j]<=m)	continue;
				temp+=(p[j]-1)/m;
			}
			if(m==1) res = temp+m;
			if(temp+m<res) res = temp+m;
		}

		cout<<"Case #"<<(te+1)<<": "<<res<<endl;
	}
	return 0;
}