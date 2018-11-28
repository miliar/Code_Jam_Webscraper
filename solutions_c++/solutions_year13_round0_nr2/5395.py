#include<cstdio>
#include<vector>
#include<algorithm>
#include<cstring>

using namespace std;

bool f[100][100];
int m[100][100];
int he[101];

int main()
{
	int n;
	scanf("%d",&n);
	for(int k=0;k<n;k++){
		vector<int> num;
		memset(he,0,sizeof(he));
		int h,w;
		scanf("%d%d",&h,&w);
		for(int i=0;i<h;i++){
			for(int j=0;j<w;j++){
				scanf("%d",&m[i][j]);
				he[m[i][j]]++;
				num.push_back(m[i][j]);
			}
		}

		sort(num.begin(),num.end());
		num.erase(unique(num.begin(),num.end()),num.end());

		for(int i=1;i<num.size();i++){
			he[num[i]]+=he[num[i-1]];
		}

		int u;
		for(u=0;u<num.size();u++){
			memset(f,0,sizeof(f));
			int cnt=0;
			for(int i=0;i<h;i++){
				if(m[i][0]>num[u])continue;
				int a=0;
				for(int j=0;j<w;j++){
					if(m[i][j]<=num[u])a++;
				}
				if(a==w){
					for(int j=0;j<w;j++){
						if(f[i][j]!=true)cnt++;
						f[i][j]=true;
					}
				}
			}
			for(int i=0;i<w;i++){
				if(m[0][i]>num[u])continue;
				int a=0;
				for(int j=0;j<h;j++){
					if(m[j][i]<=num[u])a++;
				}
				if(a==h){
					for(int j=0;j<h;j++){
						if(f[j][i]!=true)cnt++;
						f[j][i]=true;
					}
				}
			}
			if(he[num[u]]!=cnt){
				printf("Case #%d: NO\n",k+1);
				break;
			}
		}
		if(u==num.size()){
			printf("Case #%d: YES\n",k+1);
		}
	}
	return 0;
}