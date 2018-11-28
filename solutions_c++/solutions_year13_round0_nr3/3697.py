#include<iostream>
#include<strings.h>
#include<fstream>
#include<vector>
#include<math.h>
using namespace std;

bool is_pal(long long n){
	vector<short> X;
	while (n>0){
		short u= n -(int(n/10))*10;
		n= int (n/10);
		X.push_back(u);
	}
	int l=X.size();
	for (int i=0; i<int((l/2)); i++){
		if (X[i]!=X[l-i-1]){
			return false;
		}
	}
	return true;
}

main(){
	int T;
	scanf("%d",&T);
	fstream mf;
	mf.open("D:/seijee.txt");
	for (int cs=1; cs<=T; cs++){
		
		/*string Astring, Bstring;
		cin>>Astring>>Bstring;
		vector<short> A,B,temp;
		int l=Astring.length();
		for (int i=0; i<l;i++ ){
			A.push_back(Astring[l-i-1]-48);
		}
		int sqrtAln = int((l+1)/2);
		
		
		l=Bstring.length();
		for (int i=0; i<l;i++ ){
			B.push_back(Bstring[l-i-1]-48);
		}
		int sqrtBln = int((l+1)/2);
		//intake*/
		long long A,B;
		cin>>A>>B;
		long long sqA=int(sqrt(A)), sqB=int(sqrt(B));
		sqA--;
		long long temp = sqA*sqA;
		int count=0;
		
		while (temp<=B){
			if (is_pal(sqA)){
				temp = sqA*sqA;
				if (is_pal(temp) && temp>=A && temp<=B){
					count++;
				}
			}
			sqA++;
		}
		mf<<"Case #"<<cs<<": "<<count<<endl;
		cout<<"Case #"<<cs<<": "<<count<<endl;
	}
	mf.close();
}
