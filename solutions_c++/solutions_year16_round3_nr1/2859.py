#include<iostream>
#include<string>

using namespace std;

int n, m, s, a[30], T;

int main(){
	cin>>T;
	for(int t=0; t<T; t++) {
		cin>>n;
		cout<<"Case #"<<t+1<<": ";
		if(n==2) {
			cin>>s>>m;
			n = 0;
			if(s<m) swap(s,m), n = 1;
			while(s>m) {
				s--;
				cout<<char(n+'A')<<" ";
			}
			for(int i=0; i<m; i++) cout<<'A'<<'B'<<" ";
		} else {
			s = 0;
			for(int i=0; i<n; i++) cin>>a[i], s+=a[i];
			while(s>2) {
				m = 0;
				for(int i=0; i<26; i++) 
					if(a[m]<a[i]) m = i;
				cout<<char(m+'A')<<" ";
				s--;
				a[m]--;
			}
			for(int i=0; i<26; i++) 
				if(a[i]) cout<<char(i+'A');
		}
		cout<<endl;
	}
}