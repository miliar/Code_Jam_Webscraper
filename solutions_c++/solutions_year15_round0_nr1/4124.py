#include <iostream>
#include <algorithm>
#include <iomanip>
#include <climits>
#include <cstring>

using namespace std;

int main()
{
int T,z,ans,num,sum,n,i;
char c,str[1010];
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
cin >> T;
for(z=1;z<=T;z++)
{
cin >> n;
cin >> str;
ans=0;
sum=0;
for(i=0;i<=n;i++)
{
c=str[i];	
num=c-48;
if(i>sum && num!=0){
	ans+=i-sum;
	sum=i;
}
sum+=num;
}
//cout << "Case #" << z << ": ";
//cout << ans << endl;
cout<<"Case #"<<z<<": "<<ans<<"\n";
}

return 0;
}


