#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
typedef vector<vector<int> > Matrix;
Matrix a,b;

int checkCol(int N, int row){
    int temp;
    temp = a[0][row];
    for(int i=0; i<N; ++i){
	if(a[i][row] < temp) temp = a[i][row];
	else if(temp < a[i][row]) return 1;
	
    }
    return 0;
}

int main(void){
    int T,N,M,temp,MAX=0,MIN=10;
    string res;
    cin >> T;
    for(int i=0; i<T; ++i){

	cin >> N >> M;
	for(int j=0; j<N; ++j){
	    a.push_back(vector<int>());
	    for(int k=0; k<M; ++k){
		cin >> temp;
		if(temp < MIN) MIN=temp;
		if(MAX < temp) MAX=temp;
		a.at(j).push_back(temp);
	    }
	}
	b.assign(N, vector<int>(M, MAX));
	for(int height=MAX-1; MIN<=height; --height){
	    for(int j=0; j<N; ++j){
		if(find(a.at(j).begin(),a.at(j).end(),height)!=a.at(j).end()){
		    if(*max_element(a.at(j).begin(),a.at(j).end()) <= height)
			b.at(j).assign(M,height);
		}
	    }
	    for(int k=0; k<M; ++k){
		int findflag=0;
		for(int j=0; j<N; ++j){
		    if(a.at(j).at(k)==height)
			findflag=1;
		    else if(height < a.at(j).at(k)){
			findflag=2;
			break;
		    }
		}
		if(findflag==2) continue;
		else if(findflag==1){
		    for(int j=0; j<N; ++j)
			b.at(j).at(k)=height;
		}
	    }
	}
	
	if(a==b) res = "YES";
	else if(a!=b) res = "NO";
	cout << "Case #" << i+1 << ": " << res << endl;
	a.clear(); b.clear();
    }
}

