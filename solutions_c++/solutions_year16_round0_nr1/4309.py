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
	long long int t;
	fin>>t;
	
	forn(it,t){
		long long int n;
		fin>>n;
		if(n==0){
			string res = "INSOMNIA";
			if(it==0){
				fout<<"Case #"<<it+1<<": "<<res;
			}
			else{
				fout<<endl<<"Case #"<<it+1<<": "<<res;
			}
		}
		else{
			long long int res=n,iter=1,res2=n;
			vector<int> v(10,0);
			while(!check(v)){
				//cout<<res<<endl;
				long long int tmp = res;
				while(tmp!=0){
					long long int tmp2 = tmp%10;
					tmp/=10;
					//cout<<tmp2<<endl;
					v[tmp2]=1;
				}
				res2 = res;
				res=n*++iter;
			}
			res=res2;
			if(it==0){
			fout<<"Case #"<<it+1<<": "<<res;
			}
			else{
				fout<<endl<<"Case #"<<it+1<<": "<<res;
			}
		}
		
	}
}