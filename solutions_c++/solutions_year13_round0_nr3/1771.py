#include <cstdio>
#include <string>
#include <vector>
#include <cstring>
#include <iostream>

using namespace std;

const int MAXN=1010;

int T;
int tmp[MAXN],res[MAXN];
vector<string> ar;

void cont(int *temp,int k){

	string s;
	memset(res,0,sizeof res);

	for(int i=1;i<=k;i++)
		for(int j=1;j<=k;j++)
			res[i-1+j-1]+=temp[i]*temp[j];
	
	for(int i=0;i<=101;i++){
		res[i+1]+=res[i]/10;;
		res[i]%=10;
	}
	
	int L=0;
	for(int i=0;i<=100;i++)
		if(res[i])
			L=i;
			
	for(int i=0;i<=L;i++){
		s+=(res[i]+'0');
		if(res[i]!=res[L-i])
			return;
	}
	
	ar.push_back(s);
}

void f(int k,int t){
	
	if(!(t%2) && k<=(t+1)/2){
		cont(tmp,t);
		return;
	}
	
	if(t%2 && k<(t+1)/2){
		cont(tmp,t);
		return ;
	}
	
	if(k==t){
		if(t==1)
			for(int i=1;i<=3;i++){
				tmp[k]=i;
				tmp[t-k+1]=i;
				f(k-1,t);
			}
		else
			for(int i=1;i<=2;i++){
				tmp[k]=i;
				tmp[t-k+1]=i;
				f(k-1,t);
			}
	}
	
	else{
		if(t%2 && k==(t+1)/2)
			for(int i=0;i<=2;i++){
				tmp[k]=i;
				tmp[t-k+1]=i;
				f(k-1,t);
			}
		else
			for(int i=0;i<=1;i++){
				tmp[k]=i;
				tmp[t-k+1]=i;
				f(k-1,t);
			}
	}
}

int main(){
	
	for(int i=1;i<=18;i++)	f(i,i);
	
	int be,en;
	string a,b;
	
	scanf(" %d",&T);
	
	for(int i=1;i<=T;i++){
		
		cin >> a >> b;
		
		for(be=0;be<(int)ar.size();be++){
			if((int)ar[be].size()==(int)a.size() && ar[be]>=a)
				break;
			if((int)ar[be].size()>(int)a.size())
				break;
		}
		
		for(en=0;en<(int)ar.size();en++){
			if((int)ar[en].size()>(int)b.size())
				break;
			if((int)ar[en].size()==(int)b.size() && ar[en]>b)
				break;
		}
		
		printf("Case #%d: %d\n",i,en-be);		
	}

	return 0;
}
