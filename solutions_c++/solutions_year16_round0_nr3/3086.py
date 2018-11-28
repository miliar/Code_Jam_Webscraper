#include <bits/stdc++.h>
using namespace std;
int cnt, n, j;
vector <long long> divs[50];
vector <string> nums;
long long check (string s, int base){
	long long ans=0, mult=1;
	for(int i=n-1 ; i>=0 ; i--, mult*=base)
		ans+=mult*(s[i]-'0');
	for(long long i=3 ; i*i<=ans ; i++)
		if(ans%i==0)
			return i;
	return 0;
}

bool solve (string s){
	long long div;
	for(int i=2 ; i<11 ; i++){
		div=check(s,i);
		if(!div){
			divs[cnt].clear();
			return 0;
		}
		divs[cnt].push_back(div);
	}
	return 1;
}
void rec(string s="1"){
	if(cnt==j)
		return;
	if(s.size()==n-1){
		if ( solve(s+"1") ){
			cnt++;
			nums.push_back(s+"1");
		}
		return ;
	}
	rec(s+"0");
	rec(s+"1");
}
int main() {
    ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
    int t;
    fstream f1;
    f1.open("Txt.txt",ios::out);
    cin >> t;
    cin >> n >> j;
    cnt=0;
    rec();
    f1 << "Case #1:\n" ;
    for(int i=0 ; i<j ; i++){
    	f1 << nums[i] << ' ';
    	for(int j=0 ; j<9 ; j++)
    		f1 << divs[i][j] << ' ';
    	f1 << '\n';
    }
    f1.close();
    return 0;
}
