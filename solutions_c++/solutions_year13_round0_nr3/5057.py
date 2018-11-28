#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<cstring>
#include<string>
#include<set>
#include<map>
#include<cmath>
#include<fstream>
#include<stack>
#include<queue>
#include<sstream>
using namespace std;
int val;

bool Check(int num)
{
    stringstream ss;
    ss<<num;
    string p = ss.str();
    int l = p.length();

    for(int i=0;i<=l/2;i++)
        if(p[i]!=p[l-i-1]) 
			return false;
    return true;
}
int main()
{
    freopen("C-small-attempt2.in","r",stdin);
    freopen("out.txt","w",stdout);
    int sq[1028]; int i;
    memset(sq,false,sizeof(sq));sq[1]=true;
    for(i=2;i<=1000;i++){if(i*i <1000)
		sq[i*i]=true; else break;}
    for(int j=2;j<=1000;j++)
        if(sq[j]){
			if(Check(j) && Check(sqrt(j)))
				sq[j]=true;
			else
				sq[j]=false;
		}
	
int tc,a,b;
scanf("%d",&tc);
for(int T=1;T<=tc;T++)
{
scanf("%d%d",&a,&b); int count=0;
while(b>=a)
{
	if(sq[b]){count++; }b--;
}
cout<<"Case #"<<T<<": "<<count<<endl;
}
    return 0;
}