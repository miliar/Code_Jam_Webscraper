#include<bits/stdc++.h>

using namespace std;

int A[300] = {0}, n;

inline void flip(int k){                // Flips first k nos
	int B[100];
	int j =0;
	for(int i =k-1; i>= 0; i--){
		B[j++] = (A[i] ? 0 : 1);
	}
	for(int i =0; i< k; i++)
		A[i] = B[i];
}

inline int check(){                      // returns the len of first cont +s
	int i =0;
	while(A[i]){
		i++;
	}
	return i;
}

inline int depth(){                     // returns the len of last minus
	int i = n;
	while(A[i-1] && i>0){
		i--;
	}
	return i;
}

long long t;
int main(){
	ios:: sync_with_stdio(false);
	cin>>t;

	for(int j =0; j< t; j++){

	long long ans=0,len;
	char inp[304];
	cin>>inp;
	n = strlen(inp);
	for(int i =0; i< n; i++){
		A[i] = ((inp[i] == '+') ? 1 : 0);
	}
	int dep;
	while(dep = depth()){	
		if(check()){
			ans++;
			flip(check());
		}
		flip(dep);
		ans++;
	}
	cout<<"Case #"<<j+1<<": "<<ans<<endl;

	}
	return 0;
}



