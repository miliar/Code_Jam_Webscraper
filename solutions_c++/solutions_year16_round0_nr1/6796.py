#include<bits/stdc++.h>
#define lli long long

using namespace std;

int main(){
	
	ifstream cin ("input.txt");
	ofstream cout ("output.txt");
	
	int t;
	cin>>t;
	for(int tt = 0 ; tt < t ; tt ++ ){
		lli n;
		cin>>n;
		cout<<"Case #"<<tt+1<<": ";
		if(n == 0){
			cout<<"INSOMNIA"<<endl;
		}
		else{
			set <int> digit;
			set <int>::iterator it;
			for(int i=0;i<10;i++)
			digit.insert(i);
			lli ans;
			for(lli i=1;;i++){
				lli num = n*i;
				while(num>0){
					int j = num%10;
					it = digit.find(j);
					if(it != digit.end())
					digit.erase(it);
					num /= 10;
				}
				if(digit.size() == 0)
				{
					ans = n*i;
					break;
				}
			}
			cout<<ans<<endl;
		}
	}
	cin.close();
	cout.close();
	return 0;
}
