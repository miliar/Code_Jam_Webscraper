#include <bits/stdc++.h>

using namespace std;

char ss[105];
char temp[105];

int main(){
	
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	int teskes;
	scanf("%d",&teskes);
	
	for(int tc=1;tc<=teskes;tc++){
		scanf("%s",ss);
		int d=strlen(ss);
		
		int ans=0;
		for(int x=d-1;x>=0;x--){
			if(ss[x]=='+'){
				continue;
			}

			if(ss[0]=='+'){
				for(int y=0;y<=x;y++){
					if(ss[y]=='+')ss[y]='-';
					else break;
				}
				ans++;
			}
			//cout<<"fuker "<<ss<<endl;
			for(int y=0;y<=x;y++){
				temp[y]=ss[y];
				if(temp[y]=='+')temp[y]='-';
				else temp[y]='+';
			}
			
			int idx=x;
			for(int y=0;y<=x;y++){
				ss[y]=temp[idx];
				idx--;
			}
			ans++;
			//cout<<"fu "<<x<<" "<<ss<<endl;
		}
		printf("Case #%d: %d\n",tc,ans);
	}
	return 0;
}
