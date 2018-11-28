#include<iostream>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<algorithm>
#include<set>
#include<map>

#define MOD 1000000007
#define LL long long
#define ULL unsigned long long
#define RESET(a, b) memset(a,b,sizeof(a))

//RevengeofthePancakesB16

using namespace std;
int main(){
	std::ios_base::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
	freopen("B-large.in","r",stdin);
	#endif
	freopen("outputLargeB.txt","w",stdout);

	LL i, j, k, n, cases, t;
	cin>>cases;
	
	for(k=1;k<=cases;k++){
		string str;	
		cin>>str;
		
		n=0;
		
		if(str.length() == 1){
			if(str == "-")
				n = 1;
		}
		else
		while(true){
			
			//find same
			for(i=0;i<str.length()-1;i++){
				if(str[i] != str[i+1])
					break;
			}
			
			if(i == str.length()-1 && str[i] == '+')
				break;
			
			//flip
			string flip = "";
			for(j=i; j>=0;j--){
				if(str[j] == '+')
					flip += '-';
				else
					flip += '+';
			}
			//cout<<flip<<"["<<str<<"],";
			//update
			for(i=0;i<flip.length();i++)
				str[i] = flip[i];
				
			n++;
		}
		
		cout<<"Case #"<<k<<": "<<n<<endl;		
	}
	
return 0;
}

