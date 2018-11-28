#include<iostream>
#include<cstdio>
#include<vector>
#include <algorithm>

using namespace std;

int main(){
	int t=0,n;
	//freopen("A-small-attempt1.in","r",stdin);
	//freopen("in.txt","r",stdin);
	//freopen("1.out","w",stdout);
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		int a,b;
		vector<int> l;
		scanf("%d",&a);
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				scanf("%d",&n);
				if(j==a-1){
					l.push_back(n);
				}
			}
		}
		/*for(int p=0;p<4;p++){
            printf("%d ",l[p]);
		}
		printf("\n");*/
		int count=0,num;
		scanf("%d",&b);
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
                scanf("%d",&n);
				if(j==b-1){
                      //  printf("in : %d\n",n);
					if(find(l.begin(),l.end(),n)!=l.end()){
						num = n;
						count++;
					}
					/*for(int x=0;x<4;x++){
                        if(l[x]==n){
                            num=n;
                            count++;
                        }
					*/
				}
			}
		}
		if(count==1){
			printf("Case #%d: %d\n",i+1,num);
		}else if(count > 1){
			printf("Case #%d: Bad magician!\n",i+1);
		}else if(count < 1){
			printf("Case #%d: Volunteer cheated!\n",i+1);
		}
	}
	return 0;
}
