#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

#define loop(n) for(int i=0;i<n;i++)
int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int n , count, s, shyness, no, added;
	char c;
	cin>>n;
	loop(n) {
		count = 0;
		added = 0;
		cin>>s;
		for(int j=0;j<s+1;j++) {
			cin>>c;
			no = c - '0';
			if(j>count && no!=0) {
				added += (j-count);
				count=j;
			}
			count+=no;
		}
		cout<<"Case #"<<(i+1)<<": "<<added<<endl;
	}
	// your code goes here
	return 0;
}