
#include<bits/stdc++.h>
#define md 1000000007
#define ll long long
#define gc getchar_unlocked
using namespace std;
char a[510][510];
int getdirection(int r,int c,int n,int m){
	for(int i=c+1;i<m;i++){
		if(a[r][i]!='.'){
			return 1;
		}
	}
	for(int i=c-1;i>=0;i--){
		if(a[r][i]!='.'){
			return 0;
		}
	}
	for(int i=r+1;i<n;i++){
		if(a[i][c]!='.'){
			return 3;
		}
	}
	for(int i=r-1;i>=0;i--){
		if(a[i][c]!='.'){
			return 2;
		}
	}
	return -1;
}
int main()
{
	
    	#ifndef ONLINE_JUDGE
			freopen("inp.txt","r",stdin);
			freopen("out.txt","w",stdout);
		#endif
		int test;
		cin>>test;
		for(int tt=1;tt<=test;tt++){
			int n,m;
			int ct=0;
			cin>>n>>m;
			for(int i=0;i<n;i++)
				cin>>a[i];
			int ff=0;
			for(int i=0;i<n;i++)
				for(int j=0;j<m;j++){
					//cout<<i<<j<<endl;
					if(a[i][j]!='.'){
						if(a[i][j]=='<')
						{
							int f=0;
							for(int k=j-1;k>=0;k--)
								if(a[i][k]!='.'){
									f=1;
									break;
								}
								if(f==1)
									continue;
								int c=getdirection(i,j,n,m);
								if(c==-1)
								{
									ff=1;
									break;
								}
								else{
									ct++;
								}
						}
						else if(a[i][j]=='>'){
							int f=0;
							for(int k=j+1;k<m;k++)
								if(a[i][k]!='.'){
									f=1;
									break;
								}
								if(f==1)
									continue;
								int c=getdirection(i,j,n,m);
								if(c==-1)
								{
									ff=1;
									break;
								}
								else{
									ct++;
								}
						}
						else if(a[i][j]=='^'){
							int f=0;
							for(int k=i-1;k>=0;k--)
								if(a[k][j]!='.'){
									f=1;
									break;
								}
								if(f==1)
									continue;
								int c=getdirection(i,j,n,m);
								if(c==-1)
								{
									ff=1;
									break;
								}
								else{
									ct++;
								}
						}
						else if(a[i][j]=='v'){
							int f=0;
							for(int k=i+1;k<n;k++)
								if(a[k][j]!='.'){
									f=1;
									break;
								}
								if(f==1)
									continue;
								int c=getdirection(i,j,n,m);
								if(c==-1)
								{
									ff=1;
									break;
								}
								else{
									ct++;
								}
						}
						
					}
				}
				printf("Case #%d: ",tt);
				if(ff==1)
					printf("IMPOSSIBLE\n");
				else
					printf("%d\n",ct);
		}
    return 0;
}