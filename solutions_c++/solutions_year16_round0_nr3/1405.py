/*
jai shree ram _/\_
A hacker from NITP
*/

#include<bits/stdc++.h>
using namespace std;

#define mod 1000000007
typedef set<string> ss;
typedef vector<int> vs;
typedef map<int,char> msi;
typedef pair<int,int> pa;
typedef long long int ll;

int n,j,i,k,p;
string str;
queue<pair<string,int> > q;
pair<string,int> f;
int main()
{
	freopen("C-larg.in", "r", stdin);
  	freopen("C-larg.out", "w", stdout);
	ios_base::sync_with_stdio(false);
	cin.tie(0);
  	int t,l=1;
	cin>>t;
	while(t--)
	{
	    cin>>n>>j;
	    cout<<"Case #"<<l++<<":\n";
	    str="11000000000000000000000000000011";
	    cout<<str<<" ";
        for(k=3;k<=10;k++)
            cout<<k<<" ";
        cout<<11<<"\n";
        j--;
	    q.push(make_pair(str,1));
	    while(j>0)
        {
            f=q.front();
            q.pop();
            str=f.first;
            p=f.second;
            for(i=p+1;i<29;i++)
            {
                if(j>0)
                {
                    str[i]='1',str[i+1]='1';
                    cout<<str<<" ";
                    for(k=3;k<=10;k++)
                        cout<<k<<" ";
                    cout<<11<<"\n";
                    q.push(make_pair(str,i+1));
                    j--;
                    str[i]='0',str[i+1]='0';
                }
            }
        }
	}
	return 0;
}
