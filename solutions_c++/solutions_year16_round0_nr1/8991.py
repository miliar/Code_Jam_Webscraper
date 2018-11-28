#include <bits/stdc++.h>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int t=1;t<=T;t++)
	{ 
		int64_t n,cp1,cp,k;
		cin >> n;
		if(n==0)
			cout << "Case #" << t << ": INSOMNIA" << endl;
		else{
			set<int> s;
			k=0;
			while(s.size()!=10){
				k++;
				cp=n*k;
				cp1=cp;
				while(cp!=0){
					int x=cp%10;
					cp/=10;
					s.insert(x);
				}
			}
			cout << "Case #" << t << ": " << cp1 << endl;
		}
	}
}
