#include<cstdio>
#include<iostream>
using namespace std;
int main(){
	int t, p=1;
	scanf("%d", &t);
	while(t--){
		int a[4][4], flag=0;
		int ans1, ans2, c[4], ans;
		scanf("%d", &ans1);
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d",&a[i][j]);
				if(i==ans1-1){
						c[j] = a[ans1-1][j];
				}
			}			
		}
		scanf("%d",&ans2);
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d",&a[i][j]);
			}
		}
		for(int i=0; i<4; i++){
			for(int j=0;j<4;j++){
				if(c[i]==a[ans2-1][j]){
					flag++;
					ans = c[i];
				}
			}
		}
		if(flag==0){
			cout<<"Case #"<< p <<": Volunteer cheated!\n";
		}
		if(flag==1){
			cout<<"Case #"<< p <<": "<< ans<<endl;
		}
		if(flag>1){
			cout<<"Case #"<< p <<": Bad magician!\n";
		}
		p++;
	}
}