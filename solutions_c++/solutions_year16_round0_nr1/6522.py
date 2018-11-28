#include <bits/stdc++.h>
using namespace std;

long long int buk[10];

bool verifica(){
	return buk[0] && buk[1] && buk[2] && buk[3] && buk[4] && buk[5] && buk[6] && buk[7] && buk[8] && buk[9] ? true:false;
}
void imp(){
	cout << buk[1] <<" " << buk[2] <<" " << buk[3] <<" " << buk[4] <<" " << buk[5] <<" " << buk[6] <<" " << buk[7] <<" " << buk[8] <<" " << buk[9]<<endl;
}
int main(){
	long long int t, n, acum;
	string num;
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>num;
		n=stoi(num);
		acum=n;
		//cout<<"Valor = "<<n<<endl;
		for(int j=0;j<10;j++)
			buk[j]=0;
		//imp();
		for(int j=0;j<num.length();j++)
			buk[num[j]-'0']++;
		//imp();
		while(!verifica() && n>0){
			//imp();
			acum+=n;
			num=to_string(acum);
			for(int j=0;j<num.length();j++)
				buk[num[j]-'0']++;
		}
		if(n==0) cout<<"Case #"<<i<<": INSOMNIA\n";
		else cout<<"Case #"<<i<<": "<<acum<<"\n";
	}
	return 0;	
}