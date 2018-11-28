#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<fstream>
using namespace std;
int main(){
freopen ("A-large.in","r",stdin);
freopen ("output.out","w",stdout);
int t;
cin>>t;
int sh;
string p;
for(int qq=0;qq<t;qq++)
{
cin>>sh;
char ch;
cin.get(ch);
getline(cin,p);
int n=0;  
int r=0; 
int no;

if(p.size()!=0)
	r=p[0]-'0';
for(int i=1;i<p.size();i++)
{
no=p[i]-'0';
if(no>0 && i>r)
	{
		n+=i-r;
		r+=i-r+no;
    }
else
	r+=no;
}
cout<<"Case #"<<qq+1<<": "<<n<<endl;
n=0;r=0;

}
}
