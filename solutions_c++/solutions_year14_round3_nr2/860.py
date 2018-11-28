#pragma comment(linker, "/STACK:1234567890000")

#include<iostream>
#include<iomanip>
#include<queue>
#include<stack>
#include<sstream>
#include<algorithm>
#include<list>
#include<map>
#include<vector>
#include<string>
#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<set>

#define Author "DemoVersion"
using namespace std;
int dx[]={0,0,-1,1,1,-1,1,-1};
int dy[]={1,-1,0,0,1,1,-1,-1};
typedef pair<int,int> pii;
typedef long long ll;
typedef unsigned long long ull;
struct Block{
    char f,e;
    int isIn[30];
    Block(){
        int i=0;
        for(i=0;i<30;i++)
            isIn[i]=0;
    }
};
void myCpy(Block &a,Block b){
	a.f=b.f;
	a.e=b.e;
	for(int i=0;i<30;i++)
		a.isIn[i]=b.isIn[i];
}
bool myOr(int A[],int B[]){
	for(int i=0;i<30;i++){
		if(A[i]&&B[i])return false;
		if(B[i])A[i]=1;
	}
	return true;
}
Block makeBlock(string s){
	Block out;
	int i=1;
	out.f=s[0];
	while(i<s.length()&&s[i]==out.f){
		i++;
	}
	int l=s.length()-1;
	out.e=s[s.length()-1];
	while(l>=0&&s[l]==out.e){
		l--;
	}
	for(;i<l;i++){
		out.isIn[s[i]-'a']=1;
	}
	return out;
}
bool cmprs(string a,string &out){
	int i,isIn[30]={0};
	out="";
	for(i=0;i<a.length();i++){
		if(isIn[a[i]-'a'])return false;
		isIn[a[i]-'a']=1;
		out+=a[i];
		while(i<a.length()-1&&a[i+1]==a[i]){
			i++;
		}
		if(a[i+1]==a[i])i++;
	}
	return true;
}
int main(){

    ios_base::sync_with_stdio(0);
        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);
    int N,T,z,i,cnt;
	string blocks[110];
	string Rblocks[110];

	vector<int> per;
    string s,Tmp;
    cin>>T;
    for(z=1;z<=T;z++){
		cin>>N;
		cnt=0;
		for(i=0;i<N;i++){
			cin>>s;
			if(cmprs(s,blocks[i])==false){
				goto Home;
			}
			Rblocks[i]=blocks[i];
			reverse(Rblocks[i].begin(),Rblocks[i].end());
		}
		per.clear();
		for(i=0;i<N;i++){
			per.push_back(i);
		}
		do{
			s=blocks[per[0]];
			for(i=1;i<N;i++){
					s+=blocks[per[i]];
			}
			if(i==N&&cmprs(s,Tmp)){
				cnt++;
				continue;
			}

		}while(next_permutation(per.begin(),per.end()));
		Home:
		cout<<"Case #"<<z<<": "<<cnt<<endl;
    }
	return 0;
}
