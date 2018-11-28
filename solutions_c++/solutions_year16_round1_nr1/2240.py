#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main() {
	int t;
	//scanf("%d",&t);
	int X=0;
	ifstream f1;
    ofstream f2;
    f1.open("A-large.in");
    f2.open("output.out");
	f1>>t;
	//ll n,j
	int x=1;
	while(t--)
    {
        string s;
        f1>>s;
        int n=s.length();
        string s1="";
        s1+=s[0];
        for(int i=1;i<n;i++)
        {
            if(s[i] >= s1[0] ) s1=s[i]+s1;
            else s1=s1+s[i];

        }
        f2<<"Case #"<<x<<": "<<s1<<endl;
        x++;
    }
	f1.close();
    f2.close();
	return 0;
}
