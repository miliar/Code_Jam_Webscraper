#include<iostream>
#include<cstring>
#include<vector>

typedef long long ll;

using namespace std;

const int maxn=1000000+10;
bool mark[maxn];
int ans[11];
vector<int> v;
int num;
void check(int x,int y){
	ll number=0;
	for(int i=15;i>=0;i--){
		number*=(ll)y;
		if(x&(1<<i))number+=1;
	}
	for(int i=0;i<10000;i++){
		if(v[i]<number && number%(ll)v[i]==0){
			ans[y]=v[i];
			break;
		}
	}
}
int main(){
	cout<<"Case #1:"<<endl;
	for(int i=2;i<maxn;i++){
		if(!mark[i]){
			v.push_back(i);
			for(int j=i+i;j<maxn;j+=i){
				mark[j]=true;
			}
		}
	}
	for(int i=0;i<(1<<16);i++){
		if(i%2==0 || (i&(1<<15))==0)continue;
		memset(ans,-1,sizeof(ans));
		for(int j=2;j<11;j++)check(i,j);
		bool f=false;
		for(int j=2;j<11;j++)if(ans[j]==-1)f=true;
		if(!f){
			num++;
			for(int j=15;j>=0;j--){
				if(i&(1<<j))cout<<1;
				else cout<<0;
			}
			for(int j=2;j<11;j++)cout<<" "<<ans[j];
			cout<<endl;
			if(num==50)break;
		}
	}
	return 0;
}
