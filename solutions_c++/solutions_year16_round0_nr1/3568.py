#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
    int t, cnt, x[10];
    long long n, sol;
    string s;
    stringstream ss;
    fstream f1;
    f1.open("Txt.txt",ios::out);
    cin >> t;
    for(int ind=1 ; ind<=t ; ind++){
    	cin >> n;
    	cnt=0;
    	memset(x,0,sizeof(x));
    	for(int i=1 ; i<10000 && cnt!=10; i++){
    		sol=n*i;
    		ss<<sol;
    		s=ss.str();
    		for(unsigned int j=0 ; j<s.size() ; j++)
    			cnt+=(x[s[j]-'0']++==0);
    		ss.str("");
    	}
    	f1 << "Case #" << ind << ": " ;
    	if(cnt==10)
    		f1 << sol << '\n';
    	else
    		f1 << "INSOMNIA\n";
    }
    f1.close();
    return 0;
}
