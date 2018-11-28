#include <iostream>
using namespace std;

int T;
int inp1[4][4];
int inp2[4][4];
int a1,a2;
int matchCnt=0;int matchVal=-1;
void solve(){
	int r1[4];
	matchCnt=0;
	matchVal=-1;
	for(int j1=0;j1<4;++j1){
		int elem=inp1[a1-1][j1];
		for(int j2=0;j2<4;++j2){
			if(elem == inp2[a2-1][j2]){
				++matchCnt;
				matchVal=elem;
			}
		}
	}

}
int main(){
    cin>>T;
	for(int xx=1;xx<=T;++xx){
		cin>>a1;
		for(int tt1=0;tt1<4;++tt1){
			for(int tt2=0;tt2<4;++tt2){
				cin>>inp1[tt1][tt2];
			}
		}
		cin>>a2;
		for(int tt1=0;tt1<4;++tt1){
			for(int tt2=0;tt2<4;++tt2){
				cin>>inp2[tt1][tt2];
			}
		}
		solve();
		if(matchCnt==1)
			cout<<"Case #"<<xx<<": "<<matchVal<<endl;
		else if(matchCnt>1)
			cout<<"Case #"<<xx<<": "<<"Bad magician!"<<endl;
		else
			cout<<"Case #"<<xx<<": "<<"Volunteer cheated!"<<endl;
	}

}
