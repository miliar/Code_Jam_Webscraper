#include <iostream>
#include <stdio.h>
#include <vector>
#include <math.h>
#include <stdio.h>
#include <map>
#include <string>
using namespace std;


int T;
int n;
int main(){
	freopen("A-large.in","r",stdin);
	freopen("out2.txt","w",stdout);
	cin>>T;
	for(int j=1;j<=T;j++){
		bool arr[10];
		for(int i=0;i<10;i++)arr[i]=false;
		cin>>n;
		cout<<"Case #"<<j<<": ";
		if(n==0){
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		int cur=0;
		while(true){
			cur+=n;
			int t=cur;
			while(t>0){
				arr[t%10]=true;
				t/=10;
			}
			bool ok=true;
			for(int i=0;i<10;i++){
				if(!arr[i]){
					ok=false;
					break;
				}
			}
			if(ok){
				break;
			}
		}
		cout<<cur<<endl;
	}
}