#include <bits/stdc++.h>
using namespace std;

int main() {
	long long int t,it,n,i,ct,need,temp,tp;
	ifstream if1;
    if1.open("A-large.in");
	string s;
    if1>>t;
    vector<long long int> na;
    vector<string> sa;
    for(it=0;it<t;it++){
        if1>>tp;
        na.push_back(tp);
        if1>>s;
        sa.push_back(s);
    }
    if1.close();
	ofstream of;
    of.open("output.txt");
	for(it=0;it<t;it++){
		n=na[it];
		s=sa[it];
		ct=0;
		need=0;
		for(i=0;i<n+1;i++){
			temp=s[i]-48;
			if(temp!=0){
				if(i<=ct){
					ct+=temp;
				}
				else{
					need+=(i-ct);
					ct+=(i-ct);
					ct+=temp;
				}
			}
		}
		of<<"Case #"<<it+1<<": "<<need<<"\n";
	}
	of.close();
	return 0;
}
