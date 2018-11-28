#include<iostream>
#include <stdio.h>
#include <string>
#include <string.h>
#include <vector>
#include <set>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;
#define I64 long long
#define oo 2000000000

const int kk= 1000000;
char a[1005],b[1005];
int main(){
	freopen("D:\\test.txt","r",stdin);
	freopen("D:\\out.txt","w",stdout);
	int t,n;
	cin>>t;
	for(int j=1;j<=t;j++){
		scanf("%d\n",&n);
		char c,d;
		int tong=0,res=0;
		memset(a,0,sizeof a);
		memset(b,0,sizeof b);
		for(int i=0;i<=n;i++){
			scanf("%c",&a[i]);
			a[i]-='0';
			b[i]=a[i];
			if(i>0) b[i]+=b[i-1];
			if(i>0 && a[i]>0){
				if(i>b[i-1]){
				res+=i-b[i-1];
				b[i]+=i-b[i-1];
				}

			}
		}
		if(j<t)
			scanf("%c",&c);
		cout<<"Case #"<<j<<": "<<res<<endl;
		

	}
	return 0;
}



