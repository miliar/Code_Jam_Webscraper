#include<bits/stdc++.h>
using namespace std;

int main() {
	freopen("test.txt","rt",stdin);
	freopen("o.txt","wt",stdout);

	ios::sync_with_stdio(false);

	int test;
//	cin>>test;
//	scanf("%d",&test);
	cin>>test;
	for(int tt=1;tt<=test;tt++){
		long long n;
		cin>>n;
		if(n == 0){
			cout<<"Case #"<<tt<<": INSOMNIA"<<endl;
		}
		set<int> st;
		for(int i=1;i<100000;i++){
			long long t = i*n;
			while(t){
				st.insert(t%10);
				t/=10;
			}
			if((int)st.size() == 10){
				cout<<"Case #"<<tt<<": "<<(i*n)<<endl;
				break;
			}
		}

//		printf("Case #%d: %d\n");
	}


	return 0;
}
