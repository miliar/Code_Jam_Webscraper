#include<bits/stdc++.h>
using namespace std;
#define MAXX 9223372036854775807
int main() 
{
	//freopen("input_file_name.in","r",stdin);
    //freopen("output_file_name.out","w",stdout);
    int t,i,j;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        long int n;
        cin>>n;
        bool complete=false;
        if(n==0)
     {   cout<<"Case #"<<i<<": INSOMNIA\n";
        continue;
     }
    long long ans=n,temp,c=1;
    int done[10];
    memset(done,0,sizeof(done));
     while(ans<MAXX&&complete==false)
     {
        temp=ans;
        if(temp%10==0)done[0]=1;
        while(temp>0)
        {
            done[temp%10]=1;
            temp=temp/10;
        }
        int p;
        for(p=0;p<10;p++)
        {
            if(done[p]==false)break;
        }
        if(p==10)complete=true;
        else{
        c++;
        ans=n*c;}
     }
     if(complete==false)
      cout<<"Case #"<<i<<": INSOMNIA\n";
     else
       cout<<"Case #"<<i<<": "<<ans<<"\n";
    }
	return 0;
}
