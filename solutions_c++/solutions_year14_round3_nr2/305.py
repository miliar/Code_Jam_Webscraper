#include <bits/stdc++.h>
using namespace std;


class uf2{
	vector<int> a,d;
	void link(int root,int leaf,int dif){
		a[root]+=a[leaf];
		a[leaf]=root;
		d[leaf]=dif;
	}

public:
	uf2(int n):a(n,-1),d(n,0){};

	int find(int i){
		if(a[i]<0)return i;
		int t=a[i];
		a[i]=find(a[i]);
		d[i]+=d[t];
		return a[i];
	};

	bool Union(int i,int j,int dif=0){
		int ri=find(i),rj=find(j);
		if(ri==rj)return 0;
		dif+=d[i]-d[j];
		if(a[ri]<a[rj]) link(ri,rj,dif);else link(rj,ri,-dif);
		return 1;
	}
	int count(int i){
		return -a[find(i)];
	}
	int dist(int i){
		find(i);
		return d[i];
	}
};


typedef long long LL;

int n;
vector<string> s;

LL MODU=1000000007;

void solve(){
	cin>>n;
	s.resize(n);


	vector<int> cnt('z'+1);
	vector<int> one('z'+1);
	vector<char> right('z'+1);
	vector<char> left('z'+1);
	vector<bool> exist('z'+1);

	for(int i=0;i<n;++i){
		cin>>s[i];
		s[i].resize(unique(s[i].begin(),s[i].end())-s[i].begin());

		for(char ch:s[i])cnt[ch]++;
	}

	if(n<=1){
		vector<int> p(n);
		for(int i=0;i<n;++i)p[i]=i;
		LL cnts=0;
		do{
			string tar;
			for(int v:p)tar+=s[v];
			tar.resize(unique(tar.begin(),tar.end())-tar.begin());
			vector<int> tag('z'+1);
			bool ok=1;
			for(char c:tar){
				if(tag[c]){
					ok=0;
					break;
				}
				tag[c]=1;
			}
			cnts+=ok;
		}while(next_permutation(p.begin(),p.end()));
		cout<<cnts<<endl;;
		return;
	}


	for(int i=0;i<n;++i)
		cerr<<s[i]<<' ';
	cerr<<endl;

	for(int i=0;i<n;++i){
		for(int j=1;j<(int)(s[i].size())-1;++j)
			if(cnt[s[i][j]]>1) {
				cout<<"0\n";
				return;
			}
		if(s[i].size()>2)
			s[i].erase(1,s[i].size()-2);
		s[i].resize(unique(s[i].begin(),s[i].end())-s[i].begin());
		for(char ch:s[i])exist[ch]=1;
	}



	for(int i=0;i<n;++i)
		cerr<<s[i]<<' ';
	cerr<<endl;

	LL mul=1;


	for(int i=0;i<n;++i)
		if(s[i].size()>1){

			if(right[s[i][0]]!=0 || left[s[i][1]]!=0){
				cout<<"0\n";
				return;
			}

			right[s[i][0]]=s[i][1];
			left[s[i][1]]=s[i][0];

		}else{
			mul*=++one[s[i][0]];
			mul%=MODU;
		}





	uf2 u('z'+1);

	for(char ch='a';ch<='z';++ch){
		if(left[ch]){
			u.Union(left[ch],ch,1);


			if(u.dist(ch)-u.dist(left[ch])!=1){

				cout<<"0\n";
				return;
			}
		}
		if(right[ch]){
			u.Union(ch,right[ch],1);

			if(u.dist(right[ch])-u.dist(ch)!=1){

				cout<<"0\n";
				return;
			}
		}
	}

	map<char,int> mm;
	for(char ch='a';ch<='z';++ch)if(exist[ch]){
		mm[u.find(ch)]=u.count(ch);
	}

	for(auto v:mm)
		cerr<<v.first<<' '<<v.second<<endl;

	for(int i=2;i<=(int)(mm.size());++i){
		mul*=i;
		mul%=MODU;
	}

	cout<<mul<<endl;
}

int main() {
	//ios_base::sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin>>T;
	for(int i=1;i<=T;++i){
		printf("Case #%d: ",i);
		solve();
		cerr<<i<<' ';
	}
	return 0;
}
