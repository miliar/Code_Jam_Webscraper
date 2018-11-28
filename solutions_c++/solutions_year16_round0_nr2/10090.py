
#include <iostream>
using namespace std;

int main(){
	freopen("B-small-attempt1.in","r",stdin);
	freopen("output_file_name.out","w",stdout);
	int t;
	char d;
	int c,r;
	cin>>t;
	char s[t][100];
	for(int i=0;i<t;i++)
	cin>>s[i];
	for(int i=0;i<t;i++){
		c=0;
		r=0;
		d = 'g';
		for(int k=0;s[i][k]!='\0';k++){
			if(s[i][k]=='+'||s[i][k]=='-')
			r+=1;
		}
		for(int j=0;j<r;j++){
			if(d!=s[i][j])
			{
				d=s[i][j];
				c+=1;
			}
		}
		if(s[i][r-1]=='+')
		c-=1;
		cout<<"Case #"<<i+1<<": "<<c<<endl;
	}
}
