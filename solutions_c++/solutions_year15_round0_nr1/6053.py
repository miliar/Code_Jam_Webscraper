#include <iostream>
#include<fstream>
using namespace std;
int main()
{
	int o,T,i,smax,s,ss,p,j;
	char c[2000];
    ifstream in("in");
    ofstream out("out");
    in>>T;
    for(i=1;i<=T;i++)
	{
		out<<"Case #"<<i<<": ";
		in>>smax;
		ss=0;
		p=0;
		in.get();
		in.get(c,2000);
		in.get();
		//cout<<c[0]<<" ";
		for(j=0;j<=smax;j++)
		{
			s=int(c[j])-48;
        	ss=ss+s;
        	//if (i==5) cout<<ss<<" ";
			if (ss-s<j&&s>0)
			{
				o=p;
				p=p+j-ss+s;
				ss=ss+p-o;
			}
		}
		//cout<<s[smax]<<" ";
		out<<p;
		out<<endl;
	}

}
