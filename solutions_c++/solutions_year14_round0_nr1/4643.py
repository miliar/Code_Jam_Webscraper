#include<iostream>
#include<vector>
using namespace std;

int main(){
    int T,i =1;	
	cin >> T;
	while(T-->0){
		int a,b,m[4][4],n[4][4];
		cin >> a;
		int t;
		for(int i = 0;i<4;i++)
			for(int j = 0;j<4;j++){
				cin >> t;
				m[i][j]  = t;
			}
		cin >> b;
		for(int i = 0;i<4;i++)
			for(int j = 0;j<4;j++){
				cin >> t;
				n[i][j]  = t;
		}
		int p = 0,magic;
		for(int i = 0;i<4;i++)
			for(int j = 0;j<4;j++){
					if(m[a-1][i] == n[b-1][j]){
						magic = m[a-1][i];
						p++;
					}
		}
		if(p==0)
			printf("Case #%d: %s\n",i++,"Volunteer cheated!");
		else if(p==1)
			printf("Case #%d: %d\n",i++,magic);
		else 
			printf("Case #%d: %s\n",i++,"Bad magician!");
		}
	return 0;
}
