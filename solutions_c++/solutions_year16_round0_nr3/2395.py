#include<fstream>
#include<vector>
#include<string>

using namespace std;

void makeVector(string cur, int next, int n, vector<string> &cVec){
	if(next==n-1){
		cur=cur+'1';
		cVec.push_back(cur);
		return;
	}
	string nstr=cur+'0';
	makeVector(nstr,next+1,n,cVec);
	nstr=cur+'1';
	makeVector(nstr,next+1,n,cVec);
}

long long int findDiv(string str, int base){
	int l=str.length(),i;
	long long int res=0,cur=1;
	for(i=l-1;i>=0;i--){
		res += (cur*(str[i]-'0'));
		cur *= base;
	}
	if(res%2==0)
		return 2;
	for(cur=3;cur*cur<=res;cur=cur+2)
		if(res%cur==0)
			return cur;
	return -1;
}

int main(){
	ifstream fin("inp.txt");
	ofstream fout("out.txt");
	int t;
	fin>>t;
	for(int c=1;c<=t;c++){
		fout<<"Case #"<<c<<":\n";
		int n,j,i,k;
		fin>>n>>j;
		string cur="1";
		vector<string>cVec;
		makeVector(cur,1,n,cVec);
		int gencoins=0;
		for(i=0;i<cVec.size();i++){
			vector<long long int>div(9);
			for(k=0;k<9;k++){
				long long int curdiv=findDiv(cVec[i],k+2);
				div[k]=curdiv;
			}
			bool isValid=true;
			for(k=0;k<9;k++)
				if(div[k]==-1){
					isValid=false;
					break;
				}
			if(isValid){
				gencoins++;
				fout<<cVec[i]<<" ";
				for(k=0;k<9;k++)
					fout<<div[k]<<" ";
				fout<<"\n";
			}
			if(gencoins==j)
				break;
		}
	}
}
