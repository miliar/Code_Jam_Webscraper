#include <iostream>
#include <stdio.h>
using namespace std;
int main()
{
	long long i,j,k,l,m,n,a,b,cnt;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>n;
	for(i = 0; i < n; i++){
		cin>>a>>b>>k;
		cnt = 0;
		for(j = 0; j < a; j++){
			for(l = 0; l < b; l++){
				if((j&l) < k)
				cnt++;
			}
		}
		cout<<"Case #"<<i+1<<": "<<cnt<<endl;
	}

	return 0;
}
