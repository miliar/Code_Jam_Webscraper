#include<iostream>
#include<fstream>
#include<vector>
#include<unordered_map>
#include<unordered_set>

using namespace std;
unordered_map<long,int> memo;

long truc(long l, int d){
	int divsor = 1;
	for(int i=0;i<d;i++){
		divsor*=10;
	}
	return l%divsor;
}
long numd(int l){
	long ll = l;
	int nd = 0;
	while(ll>0){
		nd++;
		ll/=10;
	}
	nd/=2;
	return nd;
}
long tominus(long l,int ha){
	int nd = numd(l);
	return truc(l,nd+ha);
}

long rev(long l){
	long res = 0;
	while(l>0){
		res = res*10+(l%10);
		l/=10;
	}
	return res;
}

long check(long l){
	if(l<20){
		return l;
	} else if(memo.find(l)!=memo.end()){
		return memo[l];
	} else {
		long ld = l % 10;
		long tom = tominus(l,0);
		long nd = numd(l);
		long afterm = truc(rev(l),nd);
		cout<<l<<"\t"<<rev(l)<<"\t"<<tom<<"\t"<<afterm<<endl;
		long extra = 0;
		if(tom==0){
			long res = check(l-1)+1;
			memo[l]=res;
			return res;
		}
		if(afterm>1){
			long aft = rev(l-tom+1);
			long res = check(aft)+tom;
			memo[l]=res;
			return res;
		} else if(afterm==1){
			long tod = tominus(l,1)+9;
			long res = check(l-tod)+tod;
			memo[l]=res;
			return res;
		}else{
			cout<<"error"<<endl;
		}
	}
}

int main(int argc, char** argv){
	ifstream fin(argv[1]);
	ofstream fout(argv[2]);
	int n;
	fin>> n;
	for(int i=0;i<n;i++){
		int l;
		int x;
		string str;
		fin>>l;
		int r = check(l);
		fout<<"Case #"<<(i+1)<<": "<<r<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}

