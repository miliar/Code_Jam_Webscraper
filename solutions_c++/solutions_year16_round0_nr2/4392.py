//Author DBug<Deepak Sharma>
#include <bits/stdc++.h>

#define forn(i,n) for(long long int i=0;i<n;i++)
#define fora(i,a,b) for(long long int i=a;i<b;i++)
#define vi(v,n) for(int ii=0;ii<n;ii++){int tmpi; cin>>tmpi;v.push_back(tmpi);}
#define vo(v) for(int io=0;io<v.size();io++){cout<<v[io]<<",";}cout<<endl;
#define td(at,bt) cout<<at<<","<<bt<<endl;
#define pb push_back

using namespace std;

int check(vector<int> v){
	forn(i,10){
		if(v[i]==0) return 0;
	}
	return 1;
}

int main(){
	ios_base::sync_with_stdio(false);
	ifstream fin;
	fin.open("input.in");
	ofstream fout;
	fout.open("output.txt");
	int t;
	fin>>t;
	
	forn(it,t){
		string s;
		fin>>s;
		vector<int> a(s.size());
		if(s[0]=='+'){
			a[0]=0;
		}
		else{
			a[0]=1;
		}
		fora(i,1,s.size()){
			if(s[i]=='+'){
				a[i]=0;
			}
			else{
				a[i]=a[i-1]+1;
			}
		}
		long long int res=0;
		forn(i,a.size()){
			if(a[i]==1){
				if(i==0){
					res+=1;
				}
				else{
					res+=2;
				}
			}
		}	
		if(it==0){
			fout<<"Case #"<<it+1<<": "<<res;
		}
		else{
			fout<<endl<<"Case #"<<it+1<<": "<<res;
		}		
	}
}