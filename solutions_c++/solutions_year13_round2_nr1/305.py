#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;



int main(){
	int t;
	scanf("%d",&t);
	for(int x=1;x<=t;x++){
		printf("Case #%d: ",x);
		int a,n;
		scanf("%d %d",&a,&n);
		vector<int> motes;
		for(int i=0;i<n;i++){
			int num;
			scanf("%d",&num);
			motes.push_back(num);
		}
		sort(motes.begin(),motes.begin()+n);
		int add=0;
		int del=n;
		if(a==1){
			printf("%d\n",n);
			continue;
		}
		for(int i=0;i<n;i++){
			if(a>motes[i]){
				a+=motes[i];
			}else{
				int d=add+n-i;
				if(d<del){
					del=d;
				}
				int ad=add;
				while(a<=motes[i]){
					ad++;
					a+=a-1;
				}
				a+=motes[i];
				add=ad;
				if(del<=add){
					add=del;
					break;
				}
			}
		}
		printf("%d\n",add);
	}

}
