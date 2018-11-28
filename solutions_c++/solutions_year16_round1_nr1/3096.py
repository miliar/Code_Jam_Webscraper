#include<iostream>
#include<string>
using namespace std;



int main()
{
	freopen ("A-large.in","r",stdin);
    freopen("A-large1.out","w",stdout);
    int t;
    cin>>t;
    for(int y=0;y<t;y++)
    {
    		string s;
    		cin>>s;
    		string s1;
    		s1+=s[0];
    		for(int i=1;i<s.size();i++)
    		{
    			if(s[i]>=s1[0])
    			s1 = s[i]+s1;
    			else
    			s1 = s1+s[i];
			}
			cout<<"Case #"<<y+1<<": "<<s1<<endl;
	}
}
