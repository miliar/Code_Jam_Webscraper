#include<bits/stdc++.h>
using namespace std;

#define  IN(name) freopen(name,"r",stdin)
#define OUT(name) freopen(name,"w",stdout)
int cnt[30];
int sum,n;
const double eps = 1e-9;
void print(){
	for(int i=0;i<n;i++)
		cerr<<cnt[i]<<" ";
	cerr<<endl;
}
bool can_evacuat_2(pair<char,char> & resut){
	if(sum < 2)return 0;
	int newsum = sum - 2;
	for(int i=0;i<n;i++){
		if(cnt[i] <= 0)continue;
		cnt[i]--;
		for(int j=0;j<n;j++){
			if(cnt[j] <= 0)continue;
			cnt[j]--;
			bool ok = 1;
			for(int k=0;k<n;k++){
				double percent = ((cnt[k]*1.0) / newsum) * 100  ;
				if( (50.0 - percent) <= -eps ){
					ok = 0;
				}
			}
			if(ok){
				resut.first = (char)(i+'A');
				resut.second = (char)(j+'A');
				return 1;
			}
			cnt[j]++;
		}
		cnt[i]++;
	}
	return 0;
}

char getLargest(){
	int r = -1,best=0;
	for(int i=0;i<n;i++){
		if(cnt[i] > best ){
			best = cnt[i];
			r = i;
		}
	}
	return r;
}


int main(){
	IN("input.txt");
	OUT("output.txt");

	int t;
	scanf("%d",&t);
	for(int cs=1;cs<=t;cs++){
		sum = 0;
		memset(cnt,0,sizeof cnt);
		scanf("%d",&n);
		for(int i=0;i<n;i++){cin>>cnt[i]; sum += cnt[i];}
		vector<string> result;
		while(getLargest() != -1){
			pair<char,char> p;
			if(can_evacuat_2(p)){
				string str = "" ;
				str += (p.first);
				str += (p.second);
				sum -= 2;
				result.push_back(str);
			}else{
				int r  = getLargest();
				cnt[r]--;
				string str = "";
				str += (char)(r+'A');
				result.push_back(str);
			}
		}
		printf("Case #%d:",cs);
		for(int i=0;i<(int)result.size();i++){
			cout<<" "<<result[i];
		}
		cout<<endl;
	}
}
