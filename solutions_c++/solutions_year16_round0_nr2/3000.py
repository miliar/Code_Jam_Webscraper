#include<bits/stdc++.h>

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int T;
	cin >> T;
	for(int t=0;t<T;++t){
		string in;
		cin >> in;
		in = in +'+';
		int sol=0;
		for(int i=0;i<(signed)in.size()-1;++i)
			if(in[i]!=in[i+1])sol++;
		cout << "Case #" << t+1 << ": " << sol << "\n";
	}
	

}
