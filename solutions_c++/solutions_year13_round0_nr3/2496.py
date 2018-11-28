#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
vector <long long> v,p,re;
int t,ct=1,ps,vs,s;
long long a,b/*,p[10000001]*/,tmp,ch,cst=10;
int main(void){
	freopen("C-large-1.in","r",stdin);
	freopen("output.txt","w",stdout);
	for(int i=1; i<=3000; i++){
		tmp=(long long)i;
		ch=0;
		while(tmp){
			if(tmp%10>2)
				ch=1;
			v.push_back(tmp%10);
			tmp/=10;
		}
		if(!ch){
			vs=v.size();
			tmp=0;
			for(int j=vs-1; j>=0; j--){
				tmp*=10;
				tmp+=v[j];
			}
			for(int j=1; j<vs; j++){
				tmp*=10;
				tmp+=v[j];
			}
			
			p.push_back(tmp);
			tmp=0;
			for(int j=vs-1; j>=0; j--){
				tmp*=10;
				tmp+=v[j];
			}

			for(int j=0; j<vs; j++){
				tmp*=10;
				tmp+=v[j];
			}
			
			
			p.push_back(tmp);
		}
		v.clear();
	}

	ps=p.size();
	for(int i=0; i<ps; i++){
		tmp=p[i]*p[i];
		ch=0;
		while(tmp){
			v.push_back(tmp%10);
			tmp/=10;
		}
		vs=v.size();
		for(int j=0; j<vs; j++){
			if(v[j]!=v[vs-1-j]){
				ch=1;
				break;
			}
				
		}
		tmp=p[i]*p[i];
		if(!ch){
			re.push_back(tmp);
		}
		v.clear();
	}
	re.push_back(9);
	sort(re.begin(),re.end());

	scanf("%d",&t);
	while(t--){
		scanf("%lld %lld",&a,&b);
		printf("Case #%d: %d\n",ct,upper_bound(re.begin(),re.end(),b)-lower_bound(re.begin(),re.end(),a));
		ct++;
	}

	return 0;
}

