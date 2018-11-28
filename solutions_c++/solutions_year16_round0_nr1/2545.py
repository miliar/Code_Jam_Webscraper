//m_o_h_i_t_____t_h_e____g_r_e_a_t____a_n_d_____p_o_w_e_r_f_u_l____!_!_!
#include <bits/stdc++.h>
using namespace std;
#define ll long long 
#define fi first 
#define se second
#define pb push_back  
#define mp make_pair
ll vis[100];
void calc(ll a)
{
	ll temp=a;
	while(temp)
	{
		ll d=temp%10;
		vis[d]=1;
		temp=temp/10;
	}
}
int main()
{
	freopen("inp1.txt","r",stdin);
	freopen("out1.txt","w",stdout);
   ll t, n,ans,caseno;
   caseno=1;
   cin>>t;
   while(t--)
   {
   	cin>>n;
   	memset(vis,0,sizeof(vis));
   	if(n==0)
   		cout<<"Case #"<<caseno<<": "<<"INSOMNIA"<<endl;
   	else
   	{	ll flag=0;
   		ll l=1 ;
   		while(1)
   		{
   			flag=0;
   			for(ll j=0;j<=9;j++)
   				{if(vis[j]==0)flag=1;}
   			if(flag==0)
   				break;

   			ans=l*n;
   			calc(ans);
   			l+=1;
   		}
   		cout<<"Case #"<<caseno<<": "<<ans<<endl;
   		
   	}
    caseno++;




   }
   
	return 0;
}
