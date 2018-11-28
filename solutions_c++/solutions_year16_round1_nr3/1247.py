#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;

int n;
int fc[1001];
int bc[1001][1001];
int ch[1001];
bool ic[1001];
int an;
void aaa(int l,int d)
{
	int cur=ch[l-1];
	if(d==1){
			if(ic[fc[cur]]){
				if(fc[cur]==ch[1])an=max(an,l-1);
			}
			else{
				if(fc[fc[cur]]==cur){
					an=max(an,l);
					ch[l]=fc[cur];
					ic[fc[cur]]=1;
					aaa(l+1,2);
					ic[fc[cur]]=0;
				}
				ch[l]=fc[cur];
				ic[fc[cur]]=1;
				aaa(l+1,1);
				ic[fc[cur]]=0;
			}
	}
	else{
		for(int i=1;i<=bc[ch[1]][0];i++){
			if(!ic[bc[ch[1]][i]]){
				an=max(an,l);
			}
		}
		for(int i=1;i<=bc[cur][0];i++){
			if(!ic[bc[cur][i]]){
				an=max(an,l);
				ch[l]=bc[cur][i];
				ic[bc[cur][i]]=1;
				aaa(l+1,2);
				ic[bc[cur][i]]=0;
			}
		}
		for(int i=1;i<=n;i++){
			if(!ic[i]){
				ch[l]=i;
				ic[i]=1;
				aaa(l+1,1);
				ic[i]=0;
			}
		}
	}
}
int main(){
	int g;
	cin>>g;
for(int t=1;t<=g;t++)	{
	cin>>n;
	memset(fc,0,sizeof(fc));
	memset(bc,0,sizeof(bc));
	for(int i=1;i<=n;i++){
		int b;cin>>b;
		fc[i]=b;
		bc[b][0]++;
		bc[b][bc[b][0]]=i;
	}
	memset(ic,0,sizeof(ic));
	an=0;
	for(int i=1;i<=n;i++){
		ch[1]=i;
		ic[i]=1;
		aaa(2,1);
		ic[i]=0;
	}
	cout<<"Case #"<<t<<": "<<an<<endl;
}
return 0;
}

