#include<cstdio>
#include<map>
#include<vector>
#include<algorithm>
using namespace std;
#define MAX 105
int N;
const long long INF=(1LL<<60);
map<vector<int> ,int> M_CHP;
map<vector<int> ,int> M_CHN;

// NEGATIVE == 0
// POSITIVE == 1

int makeallneg(vector<int> v);
int makeallpos(vector<int> v);

int makeallneg(vector<int> v)
{
	int i;
	for(i=0;i<v.size();i++) if(v[i]!=0) break;
	if(i==v.size()) return 0; 
	if(M_CHN.count(v)) return M_CHN[v];
	vector<int> tmp(v);
	int last=v.back();
	if(last==0) { v.pop_back();return M_CHN[tmp]=min(1+makeallpos(v),makeallneg(v)); }
	else {
		int x=v[0];
		int sum=0;
		if(x==0) {
		  sum=1;
		  v[0]=1;
		} 
		reverse(v.begin(),v.end());
		for(i=0;i<v.size();i++) v[i]=!v[i];
		v.pop_back();
		return M_CHN[tmp]=(min(2+makeallpos(v),1+makeallneg(v))+sum);
	}
}

int makeallpos(vector<int> v)
{
	int i;
	for(i=0;i<v.size();i++) if(v[i]!=1) break;
	if(i==v.size()) return 0; 
	if(M_CHP.count(v)) return M_CHP[v];
	vector<int> tmp(v);
	int last=v.back();
	if(last==1) { v.pop_back();return M_CHP[tmp]=min(1+makeallneg(v),makeallpos(v)); }
	else {
		int x=v[0];
		int sum=0;
		if(x==1) {
		  sum=1;
		  v[0]=0;
		} 
		reverse(v.begin(),v.end());
		for(i=0;i<v.size();i++) v[i]=!v[i];
		v.pop_back();
		return M_CHP[tmp]=min(2+makeallneg(v),1+makeallpos(v))+sum;
	}
}


int main()
{
	int tc=1,T;
	char buf[BUFSIZ];
	scanf(" %d",&T);
	while(T--){
	   printf("Case #%d: ",tc++);
	   scanf(" %s",buf);
	   M_CHN.clear();
	   M_CHP.clear();
	   int i;
	   vector<int> v;
	   for(i=0;buf[i];i++) if(buf[i]=='+') v.push_back(1);
			       else v.push_back(0);
	   N=i;
	  int ans1=makeallpos(v);
	  int ans2=makeallneg(v)+1;
	 printf("%d\n",min(ans1,ans2));
	}
	return 0;
}
