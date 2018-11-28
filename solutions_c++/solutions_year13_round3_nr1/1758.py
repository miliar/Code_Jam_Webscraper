#include<iostream>
#include<algorithm>
#include<stack>
#include<queue>
#include<vector>
#include<string>
#include<set>
#include<sstream>
#include<stdlib.h>
#include<stdio.h>
#include<bitset>
#include<map>
#include<iomanip>
#include<typeinfo>

using namespace std;

//#defines
#define sc(n) scanf("%d",&(n))
#define scc(n) scanf("%c",&(n))
#define scs(n) scanf("%s",(n))
#define scl(n) scanf("%lld",&(n))
#define tr(container, it) \ 
      for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define sz(a) int ((a).size())
#define pb push_back
#define all(c) sc.begin(),(c).end()

//typedefs
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
vector<vii> AdjList;

int findAllSubstrings2(const char *s,int len)
{
	stringstream ss;
	string v;
	char ch;
	int c,ans=0,f;
    while(*s)
    {
        int x=0;f=0;
        while(*(s + x))
        {	v="";c=0;
            for(int y = 0; y <= x; y++){
               ss << *(s + y);
               ss >>ch;
               v+=ch;
               if(ch!='a' && ch!='e' && ch!='i' && ch!='o' && ch!='u'  )
               		c++;
               	else 
               		c=0;
               	if(c>=len)
               		f=1;
            }
            	if(v.length()>=len && f==1 )
            	ans++;
            	f=0;
              //  cout << "\n";
            x++;
        }
        s++;
    }
    	return ans;
}

int main()
{

	int i,j,k,t,m,n,c,flag,x,y;
	string s,v,w,son;
	char ch[1000005];

	cin>>t;
	k=t;
	while(t--) {

		scs(ch);
		cin>>n;
		cout<<"Case #"<<k-t<<": "<<findAllSubstrings2(ch,n)<<endl;;
	}

	return 0;
}


