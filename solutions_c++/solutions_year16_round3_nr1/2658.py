#include <fstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,a) FOR(i,0,a)
	
const int MAX_N=26;

int N;
int P[MAX_N+4];

vector<string> ans;

int main(){
	ifstream fin("input.in");
	ofstream fout("output.txt");
	int T;
	fin>>T;
	REP(t,T){
		fin>>N;
		ans.clear();
		REP(i,N){
			fin>>P[i];
		}
		if (N==2){
			if (P[0]==P[1]){
				REP(i,P[0]){
					ans.push_back("AB");
				}
			}
			else if (abs(P[0]-P[1])==1){
				string s="A";
				if (P[0]>P[1]){
					s="A";
					P[0]--;
				}
				else{
					s="B";
				}
				ans.push_back(s);
				REP(i,P[0]){
					ans.push_back("AB");
				}
			}
			else if (abs(P[0]-P[1])==2){
				string s="AA";
				if (P[0]>P[1]){
					s="AA";
					P[0]=P[1];
				}
				else{
					s="BB";
				}
				ans.push_back(s);
				REP(i,P[0]){
					ans.push_back("AB");
				}
			}
		}
		else{
			ans.push_back("AB");
			P[0]--;
			P[1]--;
			bool flg=true;
			while(flg){
				string s="A";
				bool flg2=false;
				for(int i=N-1;i>=0;i--){
					if (P[i]){
						s[0]='A'+ i;
						ans.push_back(s);
						flg2=true;
						P[i]--;
					}
				}
				if (!flg2) flg=false;
			}
			reverse(ans.begin(),ans.end());
		}
		fout<<"Case #"<<t+1<<":";
		REP(i,ans.size()){
			fout<<" "<<ans[i];
		}
		fout<<endl;
	}
	return 0;
}