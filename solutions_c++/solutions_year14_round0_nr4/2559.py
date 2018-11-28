#include <iostream>
#include<iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <cstring>
#include <fstream>
using namespace std;

//https://code.google.com/codejam/contest/351101/dashboard#s=p0

int main()
{

    freopen("D-large.in","r",stdin);
    freopen("rqrd3.out","w",stdout);
long double nm[1000] , yn[1000] ;
int t ,n,cs=1 ;
cin>>t ;
while(t--)
{
cin>>n ;
for(int i=0;i<n;i++)
cin>>nm[i] ;
for(int i=0;i<n;i++)
cin>>yn[i] ;

sort(nm,nm+n) ;
sort(yn,yn+n) ;

/*for(int i=0;i<n;i++)
cout<<nm[i]<<" ";
cout<<"\n";
for(int i=0;i<n;i++)
cout<<yn[i]<<" ";
*/
//soln for fair play.....

int fair_play=0;
bool fr_n[1000]={false} ;
bool fls_yn[1000]={false} ;

for(int i=0;i<n;i++)
for(int j=0;j<n;j++)
if(fr_n[j]==false && yn[j]>nm[i]) 
{
fr_n[j]=true ;
fair_play++ ;
break ;
}

int fls_play=0;

for(int i=0;i<n;i++)
for(int j=0;j<n;j++)
if(fls_yn[j]==false && nm[j]>yn[i]) 
{
fls_yn[j]=true ;
fls_play++ ;
break ;
}



cout<<"Case #"<<cs++<<": "<<fls_play<<" "<<n-fair_play<<endl ;

}

return 0;
}
