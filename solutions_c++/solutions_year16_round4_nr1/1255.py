#include <bits/stdc++.h>
typedef long long ll;

using namespace std;
int A[20][5000];

int R,P,S,N;
//r=1,p=2,s=3;
void compute(){
	for(int i=1;i<=N;i++){
		for(int j=0;j<(1<<(i-1));j++){
			if(A[i-1][j]==1){
				A[i][j*2]=1;
				A[i][j*2+1]=3;
			} else if(A[i-1][j]==2){
				A[i][j*2]=2;
				A[i][j*2+1]=1;
			} else {
				A[i][j*2]=2;
				A[i][j*2+1]=3;
			}
		}
	}
	int r1=0;
	int p2=0;
	int s3=0;
	for(int i=0;i<(1<<N);i++){
		if(A[N][i]==1){
			r1++;
		} else if(A[N][i]==2){
			p2++;
		} else {
			s3++;
		}
	}
	if(r1!=R || p2 != P || s3 != S){
		A[N][0]=9;
	}
}
string prnt(vector<int>& v){
	string s="";
	for(int i=0;i<v.size();i++){
		if(v[i]==1){
			s.push_back('R');
		} else if(v[i]==2){
			s.push_back('P');
		} else if(v[i]==3){
			s.push_back('S');
		} else {
			// cout << i << " " << v[i] << endl;
			// cout << "IMPOSSIBLE" << endl;
			return "";
		}
	}
	return s;
}
string f(string s0){
	if(s0.length()==1){
		return s0;
	}
	int size = s0.length()/2;
	string s1 = f(s0.substr(0,size));
	string s2 = f(s0.substr(size));
	if(s1<s2){
		return s1+s2;
	} else {
		return s2+s1;
	}
}
void main2(){
	vector<int> pos[3];
	vector<string> vv;
	cin >> N >> R>> P >> S;
	memset(A,0,sizeof(A));
	A[0][0]=1;
	compute();
	for(int i=0;i<(1<<N);i++){
		pos[0].push_back(A[N][i]);
	}

	memset(A,0,sizeof(A));
	A[0][0]=2;
	compute();
	for(int i=0;i<(1<<N);i++){
		pos[1].push_back(A[N][i]);
	}

	memset(A,0,sizeof(A));
	A[0][0]=3;
	compute();
	for(int i=0;i<(1<<N);i++){
		pos[2].push_back(A[N][i]);
	}
	for(int i=0;i<3;i++){
		string ss=prnt(pos[i]);
		if(ss!=""){
			ss= f(ss);
			vv.push_back(ss);
		}
	}
	if(vv.size()==0){
		cout << "IMPOSSIBLE" << endl;
	} else{
		sort(vv.begin(),vv.end());
		cout << vv[0] << endl;
	}

}

int main(int argc, char const *argv[]){
	int T;
	cin >> T;
	for(int t=0;t<T;t++){
		cout << "Case #" << t+1 << ": ";
		main2();
	}
	return 0;
}