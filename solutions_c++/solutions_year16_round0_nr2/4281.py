#include <iostream>
#include <cstdlib>

using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
 	freopen("B-large.out","w",stdout);
    long long T,C=1,i,p=1;
    string S;
    char a;
    cin>>T;
    while(T--)
    {
    	cin>>S;
    	a=S[0];
    	for(i=1;i<S.size();i++)
    	{
    		if(S[i]==a)continue;
    		else 
			{
    			a=S[i];
    			p++;
			}
		}
		if(S[S.size()-1]=='+')p--;
		cout<<"Case #"<<C<<": "<<p<<endl;
		p=1;
    	C++;
	}
}
