/*
  Author: Santhosh Reddy
  Problem: 
  Algo..etc: 
*/
 
 
#include<bits/stdc++.h>
#define vi vector<int> 
#define vc vector<char> 
#define pb push_back
#define mp make_pair
#define I vector<int>::iterator  
#define rI vector<int>::iterator 
#define ss(a) scanf("%s",a)
#define si(a) scanf("%d",&a)
#define sl(a) scanf("%ld",&a)
#define pi(a) printf("%d ",a)
#define pl(a) printf("%ld ",a)
#define ps(a) printf("%s ",a)
#define For(i,n) for(i=0;i<n;i++)
#define fOR(i,n) for(i=1;i<=n;i++)
#define nl printf("\n")
#define MAX 
#define INF 4e16
#define ULL unsigned long long
using namespace std;
//std::ios_base::sync_with_stdio(false);





int main()
{
	int t;
	si(t);
	for(int p=1;p<=t;p++){
		string inp;
		int extra;
		cin>>extra>>inp;
		int stood=(inp[0]-'0'),reqd=0;
		for(int i=1;i<inp.length();i++){
			if(stood>=i)stood+=(inp[i]-'0');
			else if(inp[i]-'0'){
				reqd+=(i-stood);
				stood+=(i-stood+(inp[i]-'0'));
			}
		}
		cout<<"Case #"<<p<<": "<<reqd<<endl;
	}
	return 0;
}
 
