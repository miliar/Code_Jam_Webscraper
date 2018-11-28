#include<bits/stdc++.h>
using namespace std;
int main() {
    int tc;
	scanf("%d",&tc);
	for(int t=1;t<=tc;t++){
		int n;
		int x=1,y=0;
        scanf("%d",&n);
        vector<double> naom(n),ken(n);
		for(int i=0;i<n;i++)
			scanf("%lf",&naom[i]);
		for(int i=0;i<n;i++)
			scanf("%lf",&ken[i]);
		sort(naom.begin(),naom.end());
		sort(ken.begin(),ken.end());
		if(n==1){
			if(naom[0]>ken[0])
				printf("Case #%d: %d %d\n",t,x,x);
            else
				printf("Case #%d: %d %d\n",t,y,y);
		}
		else{
            int n1;
			for(int i=0;i<n;i++){
				n1=0;
				int p=n-i;
				int q=i;
				for(int j=i;j<n;j++){
					if(naom[j]>ken[j-i]){
						n1++;
					}
					q++;
				}
				if(n1==n-i)
					break;
			}
			int k=0,j=0;
			int n2=0;
			for(int i=0;i<n;i++){
				while(j<n){
					if(ken[j]>naom[i]){
						k++;
						j++;
						break;
					}
					j++;
				}
			}
			printf("Case #%d: %d %d\n",t,n1,n-k);
		}
	}
	return 0;
}
