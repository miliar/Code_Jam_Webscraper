#include<bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
	freopen("input2large.in", "r", stdin);
	freopen("output2large.in", "w", stdout);
	int t, k,c, i, j ,n, l;
	cin>>t;
	string str;
	//char str[105];
	k=1;
	getchar();
	while(t--){
		//gets(str);
		cin>>str;
		c=0;
		l=str.size();
		for(i=l-1;i>=0;i--){
			if(str[i]=='+'){
				continue;
			}
			if(str[0]=='+'){
				c++;
				for(j=0;j<i;j++){
					if(str[j]=='+')str[j]='-';
					else break;
				}
			}
			//if(i==0)break;
			c++;
			reverse(str.begin(), str.begin()+i+1);
			for(j=0;j<i;j++){
				if(str[j]=='+')str[j]='-';
				else str[j]='+';
			}
		}
		cout<<"Case #"<<k<<": "<<c<<endl;
		k++;
	}
	return 0;
}