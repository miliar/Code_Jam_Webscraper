#include <iostream>
using namespace std;



int main()
{
	freopen("small.in", "r", stdin);
	freopen("small.out", "w", stdout);
	int T, a, b;
	int ary[] = {1, 4, 9, 121, 484};
	
	cin>>T;
	for(int tt = 0; tt < T; ++tt){
		cin>>a>>b;			
		int n = sizeof(ary) / sizeof(int);
		int ans = 0;
		for(int i = 0; i < n; ++i)
			if(ary[i] >= a && ary[i] <= b)
				++ans;
		
		cout<<"Case #"<<tt + 1<<": ";
		cout<<ans<<endl;
	}
	return 0;
//	cout<<"hello world"<<endl;
//	system("pause");
} 
