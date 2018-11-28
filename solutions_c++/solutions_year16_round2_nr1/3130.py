#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define inf 0x7fffffff
#define SCD(t) scanf("%d",&t)
#define SCLD(t) scanf("%ld",&t)
#define SCLLD(t) scanf("%lld",&t)
#define SCC(t) scanf("%c",&t)
#define SCS(t) scanf("%s",t)
#define SCF(t) scanf("%f",&t)
#define SCLF(t) scanf("%lf",&t)
#define pr pair<int,int>
#define mp(a,b) make_pair(a,b)
#define pb push_back
#define fr first
#define sc second
#define mset(arr,val) memset(arr,val,sizeof(arr));
#define XX -'A'

const int MAX = 1000005;
const int MOD = 1e9+7;

std::vector< int > ch;

void getmin(int mn,string s){
	for(int i =0;i<s.length();i++){
		char ch2 = s[i];
		ch[ch2 XX] -= mn;
	}
}
void getmin(int mn,string s,string s2){
	for(int i =0;i<s.length();i++){
		char ch2 = s[i];
		ch[ch2 XX] -= mn;
	}

	for(int i =0;i<s2.length();i++){
		char ch2 = s2[i];
		ch[ch2 XX] -= 2*mn;
	}
}


int main(){
	// freopen("input.txt","r",stdin);
	// freopen("A-large.in","r",stdin);
	// freopen("outl1.txt","w",stdout);
	int t;
	cin>>t;
	int num = 0;
	while(t--){
		num++;
		ch.clear();
		ch.resize(30);
		string s;
		cin>>s;
		for(int i = 0;i<s.length();i++){
			ch[s[i] XX]++;
		}

		std::vector< int > nums(10);
		
		int mn = ch['Z' XX];
		nums[0] = mn;
		getmin(mn,"ZERO");

		mn = ch['U' XX];
		nums[4] = mn;
		getmin(mn,"FOUR");
		
		mn = ch['F' XX];
		nums[5] = mn;
		getmin(mn,"FIVE");
		
		mn = ch['X' XX];
		nums[6] = mn;
		getmin(mn,"SIX");
		
		mn = ch['G' XX];
		nums[8] = mn;
		getmin(mn,"EIGHT");
		
		mn = ch['I' XX];
		nums[9] = mn;
		getmin(mn,"IE","N");
		
		mn = ch['V' XX];
		nums[7] = mn;
		getmin(mn,"SVN","E");
		
		mn = ch['N' XX];
		nums[1] = mn;
		getmin(mn,"ONE");
		
		mn = ch['W' XX];
		nums[2] = mn;
		getmin(mn,"TWO");
				
		mn = ch['H' XX];
		nums[3] = mn;
		getmin(mn,"THR","E");


		cout<<"Case #"<<num<<": ";
		for(int i=0;i<=9;i++){
			int ans = nums[i];
			while(ans--){cout<<i;}
		}
		cout<<endl;

	}
}


// int get(int num){
// 	int l;
// 	switch(num){
// 		case 1:
// 		l=getmin("ONE");
// 		break;
// 		case 2:
// 		l=getmin("TWO");
// 		break;
// 		case 3:
// 		l=getmin("THR","E");
// 		break;
// 		case 4:
// 		l=getmin("FOUR");
// 		break;
// 		case 5:
// 		l=getmin("FIVE");
// 		break;
// 		case 6:
// 		l=getmin("SIX");
// 		break;
// 		case 7:
// 		l=getmin("SVN","E");
// 		break;
// 		case 8:
// 		l=getmin("EIGHT");
// 		break;
// 		case 9:
// 		l=getmin("IE","N");
// 		break;
// 		case 0:
// 		l=getmin("ZERO");
// 		break;
// 	}
// 	return l;
// }