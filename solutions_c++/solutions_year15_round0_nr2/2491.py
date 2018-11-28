#include <cstdio>
#include <iostream>
using namespace std;
int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for(int tc = 1; tc<=t ;++tc){
		int n,ins[1000],opt=0;
		cin>>n;
		for(int i=0;i<n;++i){
			scanf("%d",&ins[i]);
			if(ins[i]>opt) opt=ins[i];
		}
		for(int i=opt;i>0;--i){
			int cal =i;
			for(int j=0;j<n;++j) cal+=(ins[j]-1)/i;
			if(cal < opt){
				opt = cal;
			}
		}	
		printf("Case #%d: %d\n",tc,opt);
	}
	return 0;
}