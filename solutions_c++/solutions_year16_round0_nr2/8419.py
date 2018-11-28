#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	ifstream fin;
	ofstream fout;
	fin.open("B-large.in");
	fout.open("jam2lf.txt");
	int t,c,l,i,j,happy,lpos,lneg;
	long int ans;
	string str;
	fin>>t;
	c=1;
	while(t--)
	{
		fin>>str;
		l=str.length();
	//	cout<<l<<endl;
		happy=0;
		for(i=0;i<l;i++) if(str[i]=='+') happy++;
	//	cout<<happy<<endl;
		ans=0;
		while(happy!=l)
		{   	happy=0;
		lpos=-1;
		    lneg=-1;
			for(i=l-1;;i--) {
				if(str[i]=='+') lpos=i;
				else break;}
				for(i=l-1;;i--) {
				if(str[i]=='-') lneg=i;
				else break;}
			//	cout<<lpos<<" "<<lneg<<endl;
				if(lneg!=-1)
				{
					if(str[0]=='+')
					{
						for(j=0;j<lneg;j++) {
							if(str[j]=='+') str[j]='-';
							else {str[j]='+';
							//happy++;
						}
					}
				}
				else {
					j=0;

					while(str[j]=='-'&&j<l){str[j]='+';
						//	happy++;
						//	cout<<"a";
							j++;
						}
				}
		}
		else {
					if(str[0]=='-')
					{
						for(j=0;j<lpos;j++) {
							if(str[j]=='+') str[j]='-';
							else {str[j]='+';
						//	happy++;
						}
					}
				}
				else {
					j=0;
					while(str[j]=='+'&&j<l){str[j]='-';
						//	happy++;
							j++;
						}
				}
	}
	ans++;
	for(i=0;i<l;i++) if(str[i]=='+') happy++;
		}
		fout<<"Case #"<<c<<": "<<ans<<endl;
		c++;
	}
	return 0;
}
