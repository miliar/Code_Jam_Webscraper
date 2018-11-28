
#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	//makedivisor();
	/**for(int i=0;i<100;i++)
		cout<<i<<" "<<prime[i]<<" \n";
	*/
	freopen("in.txt","r",stdin) ;
	freopen("out.txt","w",stdout)  ;
	cin>>t;
	for(int tt=1;tt<=t;tt++){
		long long int n,k;
		string ss;
		cin>>ss;

		cout<<"Case #"<<tt<<": ";

		int count=0;
		bool mnstopls=false;
		bool plstomns=true;
		bool flag;
		if(ss.size()==1){
			if(ss[0]=='+')
			cout<<"0\n";
			else
			cout<<"1\n";
		}
		else{
			for(int i=1;i<ss.size();i++)
			{
				if(ss[i-1]!=ss[i]){
					count++;
					if(ss[i-1]=='-')
					flag=mnstopls;
					else
					flag=plstomns;
				}
			}
			if(count==0&&ss[0]=='-')
			cout<<"1\n";
			else if(count==0)
			cout<<"0\n";
			else
			{if(count>0&&flag==plstomns)
			count++;
			else
			count=count;//:-p
			cout<<count<<endl;
			}
		}
	}
}








