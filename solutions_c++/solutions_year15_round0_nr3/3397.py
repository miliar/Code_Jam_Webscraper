#include <bits/stdc++.h>

using namespace std;
#define int long long
string mul(string a,string b){
	bool neg=0;
	char ac=a[0],bc=b[0];
	if(a[0]=='-')neg^=1,ac=a[1];
	if(b[0]=='-')neg^=1,bc=b[1];
	char res;
	if(ac=='1')res=bc;
	else if(bc=='1')res=ac;
	else if(ac==bc)res='1',neg^=1;
	else if(ac!='i'&&bc!='i')res='i',neg^=((ac=='j'&&bc=='k')?0:1);
	else if(ac!='j'&&bc!='j')res='j',neg^=((ac=='k'&&bc=='i')?0:1);
	else if(ac!='k'&&bc!='k')res='k',neg^=((ac=='i'&&bc=='j')?0:1);
	string ret;
	if(neg)ret="-";
	else ret="";
	ret+=res;
	return ret;
}
string pow(string a,int rep){
	if(rep>=4)rep=rep%4;
	if(rep==0)return "1";
	string res=a;
	for(int i=1;i<rep;i++){
		res=mul(res,a);
	}
	return res;
}
#undef int
int main(){
	#define int long long
	freopen("C-small-attempt1.in","rt",stdin);
	freopen("C-small.out","w+t",stdout);
	int tc,nc=0;cin>>tc;
	while(tc-->0){
		nc++;
		int l,x;cin>>l>>x;
		string seq;cin>>seq;
		bool isn1=false;
		string in="1";//interval
		for(int i=0;i<seq.size();i++){
			char temp=seq[i];
			string tmp="t";
			tmp[0]=temp;
			in=mul(in,tmp);
		}
		in=pow(in,x);
		if(in=="-1")isn1=true;
		if(!isn1){
			cout<<"Case #"<<nc<<": NO"<<endl;
			continue;
		}
//		cout<<"-------------------------\n";
		in="1";//temp in
		int leftesti=-1,rightestk=-1;
		for(int i=0;i<min(4*l,x*l);i++){
			char temp=seq[i%l];
			string tmp="t";
			tmp[0]=temp;
			in=mul(in,tmp);
//			cout<<in<<endl;
			if(in=="i"){
				leftesti=i;break;
			}
		}
//		cout<<"-------------------------\n";
		in="1";
		for(int i=x*l-1;i>=max(0LL,(x-4)*l-1);i--){
			char temp=seq[i%l];
			string tmp="t";
			tmp[0]=temp;
			in=mul(tmp,in);
//			cout<<in<<endl;
			if(in=="k"){
				rightestk=i;break;
			}
		}
//		cout<<"-------------------------\n";
		if(rightestk>leftesti+1&&leftesti!=-1&&rightestk!=-1){
			cout<<"Case #"<<nc<<": YES"<<endl;
		}else{
			cout<<"Case #"<<nc<<": NO"<<endl;
		}
	}
	return 0;
}
