#include<cstdio>
#include<algorithm>
#include<cstring>
#include<list>
#define N 20010
using namespace std;
char s[N];
int main(){
	int T,ans;
	scanf("%d",&T);
	list<char> l;
	for(int cs=1;cs<=T;cs++){
		l.clear();
		scanf("%s",s);
		for(int i=0;s[i];i++){
			l.push_back(s[i]);
		}
		ans=5*l.size()/2;
		bool flag=true;
		while(flag){
			flag=false;
			for(list<char>::iterator it=l.begin();it!=l.end();++it){
				list<char>::iterator nit=it;
				++nit;
				if(nit==l.end()) break;
				if(*it==*nit){
					ans+=5;
					l.erase(it);
					l.erase(nit);
					flag=true;
					break;
				}
			}
		}
		printf("Case #%d: %d\n",cs,ans);
	}
	return 0;
}
