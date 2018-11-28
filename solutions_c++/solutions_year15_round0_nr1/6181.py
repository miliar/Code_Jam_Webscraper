#include <iostream>
#include <queue>
#include <vector>
#include <string.h>
#include <stdio.h>

using namespace std;

int main() {
	// your code goes here

	// google code jam question is here and then or also we have here

	// a very easy question here

	freopen("A-large.in","r",stdin);
    freopen("outl.in","w",stdout);

	vector<int> a;
	queue<int> q;
	char y[100001];
	long long j=1;
	long i,count,t,x,s,l,sum=0;
	cin>>t;
	while(t--){
			count=0;
			cin>>s;
		//	y[0]='\0';
			a.clear();
			memset(y,'\n',sizeof(y));

			cin>>y;
			i=0;
			while(y[i]!='\0'){

				l=y[i]-'0';
				a.push_back(l);
				i++;
			}
			count=0;
			sum=a[0];
			for(i=1;i<a.size();i++){
		//		cout<<a[i]<<" ";
				if(sum>=i){
					sum+=a[i];
				}else{
					count+=(i-sum);
					sum+=a[i]+(i-sum);
				}
			}
			//cout<<endl;

			cout<<"Case #"<<j<<":"<<" "<<count<<endl;
			j++;
	}

	return 0;
}
