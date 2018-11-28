#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<string>
#include<map>
using namespace std;
map< pair<string, string> , string>  op;
int max(int a, int b){
	if(a>b)return a;
	return b;
}
int min(int a, int b){
	if(a>b)return b;
	return a;
}

string getStr(char c){
	if(c=='i')return "i";
	if(c=='j')return "j";
	if(c=='k')return "k";
	return "1";
}

string pow(string a, long long  n){
	if(n==1)return a;
	string tmp = pow(a,n/2);
	tmp = op[make_pair(tmp,tmp)];
	if(n%2==1)tmp = op[make_pair(a,tmp)];
	return tmp;
}


int main(){
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	
	op[make_pair("1","1")] = "1";op[make_pair("1","i")] = "i";op[make_pair("1","j")] = "j";op[make_pair("1","k")] = "k";
	op[make_pair("1","-1")] = "-1";op[make_pair("1","-i")] = "-i";op[make_pair("1","-j")] = "-j";op[make_pair("1","-k")] = "-k";

	op[make_pair("-1","1")] = "-1";op[make_pair("-1","i")] = "-i";op[make_pair("-1","j")] = "-j";op[make_pair("-1","k")] = "-k";
	op[make_pair("-1","-1")] = "1";op[make_pair("-1","-i")] = "i";op[make_pair("-1","-j")] = "j";op[make_pair("-1","-k")] = "k";


	op[make_pair("i","1")] = "i";op[make_pair("i","i")] = "-1";op[make_pair("i","j")] = "k";op[make_pair("i","k")] = "-j";
	op[make_pair("i","-1")] = "-i";op[make_pair("i","-i")] = "1";op[make_pair("i","-j")] = "-k";op[make_pair("i","-k")] = "j";

	op[make_pair("-i","1")] = "-i";op[make_pair("-i","i")] = "1";op[make_pair("-i","j")] = "-k";op[make_pair("-i","k")] = "j";
	op[make_pair("-i","-1")] = "i";op[make_pair("-i","-i")] = "-1";op[make_pair("-i","-j")] = "k";op[make_pair("-i","-k")] = "-j";



	op[make_pair("j","1")] = "j";op[make_pair("j","i")] = "-k";op[make_pair("j","j")] = "-1";op[make_pair("j","k")] = "i";
	op[make_pair("j","-1")] = "-j";op[make_pair("j","-i")] = "k";op[make_pair("j","-j")] = "1";op[make_pair("j","-k")] = "-i";

	op[make_pair("-j","1")] = "-j";op[make_pair("-j","i")] = "k";op[make_pair("-j","j")] = "1";op[make_pair("-j","k")] = "-i";
	op[make_pair("-j","-1")] = "j";op[make_pair("-j","-i")] = "-k";op[make_pair("-j","-j")] = "-1";op[make_pair("-j","-k")] = "i";


	op[make_pair("k","1")] = "k";op[make_pair("k","i")] = "j";op[make_pair("k","j")] = "-i";op[make_pair("k","k")] = "-1";
	op[make_pair("k","-1")] = "-k";op[make_pair("k","-i")] = "-j";op[make_pair("k","-j")] = "i";op[make_pair("k","-k")] = "1";

	op[make_pair("-k","1")] = "-k";op[make_pair("-k","i")] = "-j";op[make_pair("-k","j")] = "i";op[make_pair("-k","k")] = "1";
	op[make_pair("-k","-1")] = "k";op[make_pair("-k","-i")] = "j";op[make_pair("-k","-j")] = "-i";op[make_pair("-k","-k")] = "-1";



	int t;
	scanf("%d", &t);
	for(int casenum = 1;casenum<=t;casenum++){
		char str[11000];
		long long n,t;
		cin >>n>>t;
		scanf("%s",str);
		string ans = getStr(str[0]);
		for(int i = 1;i<n;i++){
			ans = op[make_pair(ans, getStr(str[i]))];
		}
		ans = pow(ans, t);
		if(ans!="-1"){
			printf("Case #%d: NO\n",casenum);
			continue;
		}
		int m = n*min(t,4);
		ans = getStr((str[0]));
		long long st = -1;
		if(ans=="i")st = 0;
		else{
			for(int i = 1;i<m;i++){
				ans = op[make_pair(ans, getStr(str[i%n]))];
				if(ans=="i"){
					st = i;
					break;
				}
			}
		}
		if(st==-1){
			printf("Case #%d: NO\n",casenum);
			continue;
		}
		ans = getStr((str[n-1]));
		long long ed = -1;
		if(ans=="k")ed = m-1;
		else{
			for(int i = m-2;i>=0;i--){
				ans = op[make_pair(getStr(str[i%n]),ans)];
				if(ans=="k"){
					ed = i;
					break;
				}
			}
		}
		if(ed==-1){
			printf("Case #%d: NO\n",casenum);
			continue;
		}
		ed = n*t-m+ed;
		if(ed>st){
			printf("Case #%d: YES\n",casenum);
		}else{
			printf("Case #%d: NO\n",casenum);
		}
	}
	return 0;
}