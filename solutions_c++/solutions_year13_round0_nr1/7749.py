#include<cstdio>
#include<cmath>
#include<vector>
#include<algorithm>
#include<iostream>
#include<string>
using namespace std;

int main()
{
	int T,c1,c2,z;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("a.out","w",stdout);
	vector<string> s;
	s.resize(4);
	while(scanf("%d",&T)!=EOF){
		vector<int> result;
		vector<int> dot;
		dot.resize(T);
		result.resize(T);
		for(int i=0;i<T;i++){
			result[i]=0;
			dot[i]=0;
			for(int j=0;j<4;j++){
				cin>>s[j];
			}
			for(int j=0;j<4;j++){//row
				c1=0;
				c2=0;
				for(int k=0;k<3;k++){
					if(s[j][k]=='X'){
						if(s[j][k+1]!='X' && s[j][k+1]!='T') break;
						c1++;
					}
					else if(s[j][k]=='O'){
						if(s[j][k+1]!='O' && s[j][k+1]!='T') break;
						c2++;
					}
					else if(s[j][k]=='.'){
						dot[i]=1;
						break;
					}
				}
				if(c1==3){
					result[i]=1;
					break;
				}
				else if(c2==3){
					result[i]=2;
					break;
				}
			}
			for(int k=0;k<4;k++){//col
				c1=0;
				c2=0;
				for(int j=0;j<3;j++){
					if(s[j][k]=='X'){
						if(s[j+1][k]!='X' && s[j+1][k]!='T') break;
						c1++;
					}
					else if(s[j][k]=='O'){
						if(s[j+1][k]!='O' && s[j+1][k]!='T') break;
						c2++;
					}
					else if(s[j][k]=='.'){
						dot[i]=1;
						break;
					}
				}
				if(c1==3){
					result[i]=1;
					break;
				}
				else if(c2==3){
					result[i]=2;
					break;
				}
			}
			c1=0;
			c2=0;
			for(int j=0;j<4;j++){//dia1
				if(s[j][j]=='X'){
					if(s[j+1][j+1]!='X' && s[j+1][j+1]!='T') break;
					c1++;
				}
				else if(s[j][j]=='O'){
					if(s[j+1][j+1]!='O' && s[j+1][j+1]!='T') break;
					c2++;
				}
				else if(s[j][j]=='.'){
					dot[i]=1;
					break;
				}
				if(c1==3){
					result[i]=1;
					break;
				}
				else if(c2==3){
					result[i]=2;
					break;
				}
			}
			z=3;
			c1=0;
			c2=0;
			for(int j=0;j<4;j++){//dia2
				if(s[j][z]=='X'){
					if(s[j+1][z-1]!='X' && s[j+1][z-1]!='T') break;
					c1++;
				}
				else if(s[j][z]=='O'){
					if(s[j+1][z-1]!='O' && s[j+1][z-1]!='T') break;
					c2++;
				}
				else if(s[j][z]=='.'){
					dot[i]=1;
					break;
				}
				if(c1==3){
					result[i]=1;
					break;
				}
				else if(c2==3){
					result[i]=2;
					break;
				}
				z--;
			}
		}
		for(int i=0;i<T;i++){
			if(result[i]==1)
				cout<<"Case #"<<i+1<<": X won"<<endl;
			else if(result[i]==2)
				cout<<"Case #"<<i+1<<": O won"<<endl;
			else if(result[i]==0 && dot[i]==1)
				cout<<"Case #"<<i+1<<": Game has not completed"<<endl;
			else if(result[i]==0 && dot[i]==0)
				cout<<"Case #"<<i+1<<": Draw"<<endl;
		}
	}
	return 0;
}
