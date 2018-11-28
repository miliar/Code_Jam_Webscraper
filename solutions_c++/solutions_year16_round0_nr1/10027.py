#include<bits/stdc++.h>
using namespace std;

bool used[10]={false};
int counter=0; 
int T, tc;
unsigned long  n, k, dg; 

void ekstrak(unsigned long x){
	unsigned long s=x;
	while (s>0){
		dg=s%10; 
		if (!used[dg]) {used[dg]=true; counter++;}
		s/=10;
	}
}

int main(){
	cin.sync_with_stdio(0); cin.tie(0); 
	
	cin>>T; 
	for (tc=1; tc<=T; tc++){
		cin>>n;
		counter=0; //digit yang udah kepake ada berapa
		for (int i=0; i<=10; i++) used[i]=false; //reset jadi belom kepake
		
		if (n==0) {cout<<"Case #"<<tc<<": INSOMNIA\n"; continue;}
		
		for (k=1; counter<=10; k++){
			if (counter==10) {cout<<"Case #"<<tc<<": "<<(k-1)*n<<endl; break;}
			ekstrak(k*n);
		}
	}
}
