#include<iostream>
using namespace std;

int main(){
    int T, K, C ,S, mins;
    cin >> T;
    for(int t=1; t<=T; ++t){
	cin >> K >> C >> S;
	if(C == 1){
	    if(S < K){
		cout << "Case #" << t << ": IMPOSSIBLE" << endl;
	    }else{
		cout << "Case #" << t << ":";
		for(int k=1; k<=K; ++k){
		    cout << " " << k;
		}
		cout << endl;
	    }
	    continue;
	}
	mins = K / 2;
	if(K % 2 == 1) mins += 1;
	if(S < mins){
	    cout << "Case #" << t << ": IMPOSSIBLE" << endl;
	    continue;
	}
	cout << "Case #" << t << ":";
	long long curl, curi;
	for(int i=0; i<K; i+=2){
	    curl = 1;
	    for(int c=0; c<C; ++c){
		curl *= K;
	    }
	    curi = 0;
	    while(curl > K){
		curl /= K;
		curi += curl * i;
	    }
	    if(K >= i+2){
		cout << " " << curi+i+2;
	    }else{
		cout << " " << curi+i+1;
	    }
	}
	cout << endl;
    }
    return 0;
}
