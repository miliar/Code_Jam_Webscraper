#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
	int T;
	cin>>T;
	int n;
	char a[100][100]; 
	int b[100];
	int c[100][100];
	int ans=0;
	int t;
	int tans;
	bool lose;
	char cc[100][100];
	for(int x=0;x<T;x++){
		lose=false;
		for(int i=0;i<100;i++){
			for(int j=0;j<100;j++){
				a[i][j]='\0';
				c[i][j]=0;
			}
			b[i]=0;
		}	
		cin>>n;
		for(int i=0;i<n;i++){
			scanf("%s",a[i]);
			c[i][0]=1;
			cc[i][0]=a[i][0];
			for(int j=1;a[i][j]!='\0'&&a[i][j]!='\n'&&a[i][j]!=' ';j++){
				if(a[i][j] != a[i][j-1]){
					b[i]++;
					cc[i][b[i]]=a[i][j];
				}
				c[i][b[i]]++;
			}
			/**cout<<b[i];
			for(int j=0;j<b[i];j++){
				cout<<" "<<c[i][b[j]];

			}
			cout<<endl;*/
			//cout<<cc[i]<<endl;
		}
		//no win
		for(int i=1;i<n;i++){
			if(b[i]!=b[i-1]){
				lose=true;
				break;
			}
		}
		for(int i=0;i<n;i++){
			for(int j=i+1;j<n;j++){
				for(int k=0;k<=b[0];k++){
					if(cc[i][k]!=cc[j][k]){
						lose=true;
						break;
					}
				}
			}
		}
		//
		if(lose){
			printf("Case #%d: Fegla Won\n",x+1);
			continue;
		}
		/**for(int i=0;i<n;i++){
			tans=0;
			for(int j=0;j<n;j++){
				for(int k=0;k<=b[0];k++){
					t=c[i][k]-c[j][k];
					if(t<0)
						t*=-1;
					tans+=t;
				}
			}
			if(tans<ans)
				ans=tans;
		}*/
			//cout<<b[0]<<endl;
		int tt[100];
		for(int i=0;i<100;i++)
			tt[i]=0;
		for(int i=0;i<=b[0];i++){
			for(int j=0;j<n;j++){
				tt[i]+=c[j][i];
			}
		}
		for(int i=0;i<=b[0];i++){
			tt[i]=tt[i]/n;
		}
		int ttans;
		ans=0;
		for(int i=0;i<n;i++){
			tans=0;
			for(int j=0;j<=b[0];j++){
				t=c[i][j]-tt[j];
				if(t<0)
					t*=-1;
				tans+=t;
			}
			ans+=tans;
		}
		printf("Case #%d: %d\n",x+1,ans);




	}
}