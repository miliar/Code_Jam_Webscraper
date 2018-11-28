#include <bits/stdc++.h>
using namespace std;

#define sd(a) scanf("%d",&a)
#define ss(a) scanf("%s",a)
#define sl(a) scanf("%lld",&a)
#define clr(a) memset(a,0,sizeof(a))
#define debug(a) printf("check%d\n",a)
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define ll long long
#define MAX 100005
#define mod 1000000007

int main() {
	
	int t;
	
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
	
	sd(t);
	
	string s;
	int k,kk=0;
	
	while(t--){
		kk++;
		cout<<"Case #"<<kk<<": ";
		cin>>s;
		cin>>k;
		int count = 0;
		
		for(int i=s.length()-1;i>=k-1;i--){
			 
			 if(s[i]=='-'){
			 	count++;
			 	int temp = k;
			 	while(temp--){
			 		char c;
			 		s[i-temp]=='+'?c='-':c='+';
			 		s[i-temp]=c;
			 	}
			 	
			 }
		}
		int flag=1;
		
		for(int i=0;i<s.length();i++){
			if(s[i]=='-'){
				flag = 0;
				break;
			}
		}
		
		if(flag)
			cout<<count<<endl;
		else{
			cout<<"IMPOSSIBLE"<<endl;
		}
		
	}
	
	
	
	return 0;
}
