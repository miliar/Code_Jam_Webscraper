#include<stdio.h>
#include<string.h>
#include<map>
#include<vector>

const int M=1000002013;

struct subway{
	subway(){}
	subway(int o,int e):o(o),e(e){}
	int o,e;
	bool operator<(const subway &l)const{
		if(o!=l.o)return o<l.o;
		return e<l.e;
	}
}data[1005];

std::map<subway,int> list;
std::vector<subway> add;
std::vector<int> per;

int n,m;

void input()
{
	list.clear();
	int p;
	scanf("%d%d",&n,&m);
	for(int i=1;i<=m;i++){
		scanf("%d%d%d",&data[i].o,&data[i].e,&p);
		if(list.find(data[i])!=list.end())list[data[i]]+=p;
		else list[data[i]]=p;
	}
}

void solve()
{
	long long ans=0,pp=0,tmp=-1;
	subway x,y;
	std::map<subway,int>::iterator i,j;
	while(tmp!=ans){
		tmp=ans;
		for(i=list.begin();i!=list.end();i++){
			if(i->second==0)continue;
			j=i;
			for(++j;j!=list.end();++j){
				if(i->second == 0)break;
				if(j->second == 0)continue;
				x=i->first, y=j->first;
				if(x.o==y.o||x.e>=y.e||x.e<y.o)continue;
				if(i->second>j->second){
					pp=(((long long)j->second*(y.o-x.o)%M))*(y.e-x.e); pp%=M;
					ans+=pp;
					i->second-=j->second;
					add.push_back(subway(x.o,y.e));
					add.push_back(subway(y.o,x.e));
					per.push_back(j->second);
					per.push_back(j->second);
					j->second = 0;
				}
				else{
					pp=(((long long)i->second*(y.o-x.o))%M)*(y.e-x.e); pp%=M;
					ans+=pp;
					j->second -= i->second;
					add.push_back(subway(x.o,y.e));
					add.push_back(subway(y.o,x.e));
					per.push_back(i->second);
					per.push_back(i->second);
					i->second = 0;
				}
				ans%=M;
				for(int t=0;t<add.size();t++){
					if(list.find(add[t])!=list.end())list[add[t]]+=per[t];
					else list[add[t]]=per[t];
				}
				add.clear(); per.clear();
			}
		}
		for(i=list.begin();i!=list.end();){
			if(i->second==0){
				j=i;
				++i;
				list.erase(j);
			}
			else ++i;
		}
	}
	printf("%lld\n",ans);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,T;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		input();
		printf("Case #%d: ",t);
		solve();
	}
}