#include<bits/stdc++.h>
using namespace std;

int main()
{   freopen("ran.txt","r",stdin);
	freopen("o.txt","w",stdout);
   long int test,n,ran[1001],i,j,cake,len,cakemin_time,cas;
    cin>>test;
    for(cas=1;cas<=test;cas++)
	{
        cin>>n;
        len=0;
        for(i=0;i<=n-1;i++)
		{
            cin>>ran[i];
            len=max(len,ran[i]);
        }
        cakemin_time=1000000;
        for(i=1;i<=len;i++){
            cake=0;
            for(j=0;j<=n-1;j++){
                if(ran[j]%i==0) cake+=(ran[j]/i)-1;
                else{cake+=ran[j]/i;}
            }
            cakemin_time=min(cakemin_time,cake+i);
        }
       cout<<"Case #"<<cas<<": "<<cakemin_time<<endl;
    }
fclose(stdout);
return 0;
}
