#include<iostream>
#include<string>
#include<cstdio>
#define gc getchar_unlocked
using namespace std;
void scanint(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}
bool isHavingNeg(string s)
{
	for(int i=0;i<s.length();i++)
		if(s[i]=='-')
			return true;
	return false;
}
int main()
{
	int T;
	scanint(T);
	int j=1;
    while(T--)
    {
    	int count=0;
    	string s;
    	cin>>s;
    	while(isHavingNeg(s))
    	{
            int index=0;
            if(s[index]=='+')
            {
                while(s[index]=='+' && index<s.length())
                    index++;
                index--;
                string s1=s;
                for(int i=0;i<=index;i++)
                {
                    if(s1[index-i]=='+')
                        s[i]='-';
                    else
                        s[i]='+';
                }
                count++;
            }
            index=0;
            if(s[index]=='-')
            {
                while(s[index]=='-' && index<s.length())
                    index++;
                index--;
                string s1=s;
                for(int i=0;i<=index;i++)
                {
                    if(s1[index-i]=='+')
                        s[i]='-';
                    else
                        s[i]='+';
                }
                count++;
            }
    		

    	}
    	cout<<"Case #"<<j<<": "<<count<<endl;
    	j++;
    }

}