#include <bits/stdc++.h>
using namespace std;

int t;

string s[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
string inp;

int order[] = {0,6,7,8,5,9,3,4,2,1};
    
int a[26];
int ans[10];

int main(){
    cin >> t;
    for(int ii=1;ii<=t;ii++){
	cin >> inp;
	memset(ans,0,sizeof(ans));
	memset(a,0,sizeof(a));
	for(string::iterator it = inp.begin(); it != inp.end(); ++it) a[*it - 'A'] ++;
	
	for(int i=0;i<10;i++){
	    int c = 9999999;
	    for(string::iterator it2=s[order[i]].begin(); it2 != s[order[i]].end(); ++it2) c = min(c,a[*it2 - 'A']);
	    for(string::iterator it2=s[order[i]].begin(); it2 != s[order[i]].end(); ++it2) a[*it2 - 'A'] -= c;
	    ans[order[i]] = c;
	    //	    cerr << order[i] << "   " << c << endl;
	}
	printf("Case #%d: ",ii);
	for(int i=0;i<10;i++){
	    for(int j=0;j<ans[i];j++) printf("%d",i);
	}
	printf("\n");
    }
    return 0;
}
