#include<algorithm>
#include<iostream>
#include<fstream>
#include<stack>
#include<utility>
#include<queue>
using namespace std;

const int MAXM=1000;
const int MOD=1000002013;

struct move{
	long long o,e,p;
	move(){}
	move(int a,int b,int c){o=a;e=b;p=c;}
};
struct event{
	long long d,p;
	bool end;
	event(){}
	event(long long a,long long b,bool c){d=a;p=b;end=c;}
	bool operator<(const event &oth)const{return 2*d+end>2*oth.d+oth.end;}
};

bool beg(const move &a,const move &b){return a.o<b.o;}
bool end(const move &a,const move &b){return a.e<b.e;}

long long n,m,t,orig,after;
move peeps[MAXM],peepsback[MAXM];
ifstream fin("input.in");
ofstream fout("output.out");
stack<pair<long long,long long> >st;//(d,p)
priority_queue<event>que;

long long f(long long x){return ((n*n+n-2)/2-((n-x)*(n-x)+(n-x)-2)/2)%MOD;}

int main(){
	fin>>t;
	for(int k=1;k<=t;k++){
		fin>>n>>m;
		orig=after=0;
		for(int i=0;i<m;i++){
			int a,b,c;
			fin>>a>>b>>c;
			//peeps[i]=peepsback[i]=move(a,b,c);
			que.push(event(a,c,false));
			que.push(event(b,c,true));
			orig+=c*f(b-a);
			orig%=MOD;
		}
		//sort(peeps,peeps+m,beg);
		//sort(peepsback,peepsback+m,end);
		while(!que.empty()){
			event e=que.top();
			que.pop();
			if(e.end){
				while(e.p){
					pair<long long,long long>beg=st.top();
					st.pop();
					long long pmax=min(e.p,beg.second);
					after+=pmax*f(e.d-beg.first);
					after%=MOD;
					e.p-=pmax;
					beg.second-=pmax;
					if(beg.second)st.push(beg);
				}
			}
			else{
				st.push(make_pair(e.d,e.p));
			}
		}
		fout<<"Case #"<<k<<": "<<(orig-after+MOD)%MOD<<endl;
	}
}