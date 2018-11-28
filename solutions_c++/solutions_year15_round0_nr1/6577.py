#include <bits/stdc++.h>
using namespace std;

int main() {
int t=1,tc;
cin>>tc;
while(t<=tc){
	int m;
            string arr;
            int s=0;
			int a=0;
			cin>>m>>arr;
            for(int i=0;i<m+1;i++)
            {
            
            if(i>s){ a+=(i-s); s+=(i-s);}
            s+=arr[i]-'0';
            }
            cout<<"Case #"<<t<<": "<<a<<endl;
t++;}
	return 0;
}