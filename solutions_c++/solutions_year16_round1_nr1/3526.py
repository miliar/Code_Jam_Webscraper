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
int main()
{
	int T;
	scanint(T);
    int k=1;
    while(T--)
    {
    	string s;
        cin>>s;
        string s1;
        for(int i=0;i<s.length();i++)
        {
            if(s1.length()==0)
                s1.push_back(s[i]);
            else if(s[i]<s1[0])
                s1.push_back(s[i]);
            else if(s[i]>=s1[0])
            { 
                string s2=s1;
                s1="";
                s1.push_back(s[i]);
                for(int j=0;j<s2.length();j++)
                    s1.push_back(s2[j]);
            }
        }
        cout<<"Case #"<<k<<": "<<s1<<endl;
        k++;
    }

}