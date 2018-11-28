#include <iostream>
using namespace std;

bool app1[17], app2[17];

int main()
{
//	freopen("in.txt", "r", stdin);
//	freopen("out.txt", "w", stdout);
	int t;
	cin>>t;
	for(int cas = 1; cas <= t; cas ++){
		for(int i = 0; i < 17; i ++)
			app1[i] = app2[i] = false;
		int a, b;
		cin>> a;
		for(int i = 1; i <= 4; i ++){
			for(int j = 1; j <= 4; j ++){
				int bb;
				cin>> bb;
				if(i == a)
					app1[bb] = true;
			}
		}
		cin>> b;
		for(int i = 1; i <= 4; i ++){
			for(int j = 1; j <= 4; j ++){
				int bb;
				cin>> bb;
				if(i == b)
					app2[bb] = true;
			}	
		}
		int cnt = 0, ans = -1;
		for(int i = 1; i < 17; i ++){
			if(app1[i] && app2[i]){
				cnt ++;
				ans = i;	
			}
		}
		cout<<"Case #"<<cas<<": ";
		if(cnt >= 2){
			cout<<"Bad magician!"<<endl;
		}else if(cnt == 1){
			cout<<ans<<endl;
		}else{
			cout<<"Volunteer cheated!"<<endl;
		}
	}	
}
