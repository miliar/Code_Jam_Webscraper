#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#define PI 3.142
using namespace std;
vector <int> v;
int k,x;
string str1;
int check(int j,int ii)
{
    x=0;
    for(int tt=0;tt<ii;tt++)
    {
    if(str1[j+tt]=='b' || str1[j+tt]=='c' || str1[j+tt]=='d' || str1[j+tt]=='f' || str1[j+tt]=='g' || str1[j+tt]=='h' || str1[j+tt]=='j' || str1[j+tt]=='k' || str1[j+tt]=='l' || str1[j+tt]=='m' || str1[j+tt]=='n' || str1[j+tt]=='p' || str1[j+tt]=='q' || str1[j+tt]=='r' || str1[j+tt]=='s' || str1[j+tt]=='t' || str1[j+tt]=='v' || str1[j+tt]=='w' || str1[j+tt]=='x' || str1[j+tt]=='y' || str1[j+tt]=='z')
                 x++;
    else x=0;
    if(x==k)
    return 1;
    
}   
    return 0;
}  
int main()
{
    int n=0,t,i,ii,xx=0,j;
    string str;
    freopen("A-small-attempt0.in","rt",stdin);
	//freopen("A-large.in","rt",stdin);
    freopen("A.out","wt",stdout);
	cin>>t;
	while(t>0)
	{
              n++,t--;
              xx=0;
              cin>>str>>k;
              for(ii=k;ii<=str.size();ii++)
              {
              for(i=0;i<str.size()-ii+1;i++)
              { 
                str1=str.substr(i,ii);
                for(j=0;j<str1.size();j++)
                {
                 int r=check(j,ii);
                 xx+=r;
                break;
                 }
              }
              }
              cout<<"Case #"<<n<<": "<<xx<<endl;
              }
              return 0;
  }
