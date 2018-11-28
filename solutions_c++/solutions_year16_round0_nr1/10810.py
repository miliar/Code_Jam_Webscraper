#include<bits/stdc++.h>
using namespace std;
typedef long long int llt;
main()
{
#ifndef ONLINE_JUDGE
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);

#endif
int r[10];
llt t,n,sum,m;
cin>>t;
for(int i =1 ; i<=t ; i++)
{

cin>>n;
memset(r,-1,sizeof r);
sum=10;

for(int j =1 ; j<1000 ; j++)
{
m=n*j;
//cout<<t<<" "<<sum<<" ";
//cout<<n<<endl;
while(m){sum+=r[m%10];r[m%10]=0;m/=10;}
if(!sum){cout<<"Case #"<<i<<": "<<n*j<<"\n";break;}
//n*=j;

}




if(sum)
cout<<"Case #"<<i<<": INSOMNIA\n";

//cout<<endl<<i<<" "<<t<<endl;

}
}
