#include<iostream>
#include <string>
#include <cstdio>
#include <set>
#include <deque>
#include<vector>

using namespace std;
string S;


int main()
{
	
	freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
	long long T;
	string s;
	cin>>T;
	
	for( long long i=1; i<=T; i++){
		cin>>s;
		cout<<"Case #"<<i<<": ";
		vector<int> ans(10);
		for(int j=0 ; j<s.length(); j++){
			if(s[j]=='Z')
				ans[0]++;
			else if(s[j]=='W')
				ans[2]++;
			else if(s[j]=='G')
				ans[8]++;
			else if(s[j]=='X')
				ans[6]++;
			else if(s[j]=='U')
				ans[4]++;
			else if(s[j]=='F')
				ans[5]++;
			else if(s[j]=='S')
				ans[7]++;
			else if(s[j]=='O')
				ans[1]++;
			else if(s[j]=='R')
				ans[3]++;
			else if(s[j]=='N')
				ans[9]++;
		}

		ans[5]= ans[5]- ans[4];
		ans[7]= ans[7]- ans[6];
		ans[1]= ans[1]- ans[0]- ans[2]- ans[4];
		ans[3]= ans[3]- ans[0]- ans[4];
		ans[9]= (ans[9]- ans[1]- ans[7])/2;


		for(int j=0 ; j<10; j++)
			for(int k=0 ; k<ans[j]; k++)
				cout<<j;
		cout<<endl;
	
	}

	return 0;
}

//void generate(int ind, string s){
//  
//
//}