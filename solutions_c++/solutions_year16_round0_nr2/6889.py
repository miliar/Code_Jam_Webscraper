#include<bits/stdc++.h>
#define lli long long

using namespace std;

int main(){
	
	ifstream cin ("input.txt");
	ofstream cout ("output.txt");
	
	int t;
	cin>>t;
	for(int tt = 0 ; tt < t ; tt ++ ){
		string str;
		cin>>str;
		int n = str.length();
		lli ans = 0;
		cout<<"Case #"<<tt+1<<": ";
		int y = 0;
		for(int i=0;i<n;i++){
			if(str[i] == '-'){
				y = i;
				while(str[y] == '-' && y<n)
				y++;
				if(i == 0)
				ans++;
				else
				ans+=2;
				i = y-1;
			}
		}
		cout<<ans<<endl;
	}
	cin.close();
	cout.close();
	return 0;
}
