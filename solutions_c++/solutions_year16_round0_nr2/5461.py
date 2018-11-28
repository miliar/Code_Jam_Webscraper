#include <iostream>
#include <string>

using namespace std;

int main() {
	ios_base::sync_with_stdio(0);

	string st;
	int T,i,j,cnt,end,start;
	cin>>T;
	for(i=1;i<=T;i++) {
		cin>>st;
		end=st.length()-1;

		cnt=0;
		while(end>=0) {
			if(st[end]=='+')
				end--;
			else {
				start=0;
				while(st[start]=='+' && start<=end) {
					st[start++]='-';
				}
				if(start!=0)
					cnt++;
				for(j=0;(j<<1)<end;j++) {
					if(st[j]=='-' && st[end-j]=='-') {
						st[j]='+';	st[end-j]='+';
					}
					else if(st[j]=='+' && st[end-j]=='+') {
						st[j]='-';	st[end-j]='-';
					}
					else if(st[j]=='-' && st[end-j]=='+') {
						st[j]='-';	st[end-j]='+';
					}
					else {
						st[j]='+';	st[end-j]='-';
					}
				}
				if(end%2==0) {
					if(st[j]=='+')
						st[j]='-';
					else
						st[j]='+';
				}
				cnt++;
			}
		}

		cout<<"Case #"<<i<<": "<<cnt<<"\n";
	}	
	return 0;
}