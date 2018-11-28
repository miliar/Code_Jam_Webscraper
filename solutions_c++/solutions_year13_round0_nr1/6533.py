#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
bool X,O;
void C(string s){
	sort(s.begin(),s.end());
	if(s=="OOOO" || s=="OOOT") O=true;
	if(s=="XXXX" || s=="TXXX") X=true;
}
int main(){
	//freopen("test","r",stdin);
	//freopen("out","wb",stdout);
	int t;
	string input,d;
	cin>>t;
	int index=1;
	while(t--){
		vector<string> B;
		X=false,O=false;
		int count=0;
		for(int i=0;i<4;i++){
			cin>>input;
			B.push_back(input);
			C(input);
		}
		string l="",r="";
		for (int i = 0; i < 4; ++i){
			string s="";
			l+=B[i][i];
			for (int j = 0; j < 4; ++j){
				s+=B[j][i];
				if(i+j==3) r+=B[j][i];
				if(B[j][i]!='.') count++;
			}
			C(s);
		}
		C(l);C(r);
		if(count<16){
			if(X && !O) cout<<"Case #"<<index<<": X won"<<endl;
			else if(O && !X) cout<<"Case #"<<index<<": O won"<<endl;
			else if(O && X) cout<<"Case #"<<index<<": Draw";
			else cout<<"Case #"<<index<<": Game has not completed"<<endl;
		}
		else{
			if(X && !O) cout<<"Case #"<<index<<": X won"<<endl;
			else if(O && !X) cout<<"Case #"<<index<<": O won"<<endl;
			else cout<<"Case #"<<index<<": Draw"<<endl;
		}
		index++;
	}
	return 0;
}