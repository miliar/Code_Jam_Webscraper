#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef unsigned long long int ull;
#define inf 100000000000000000
int n;
int p[30];

int main()
{
     freopen("0in.txt","r",stdin);
     freopen("0out.txt","w",stdout);
     int tcase,t,tot,id,tmp,i,j;
	 scanf("%d",&tcase);
	 for(t=1;t<=tcase;t++)
	 {
	    scanf("%d",&n);
		 for(i=0;i<n;i++)
		 scanf("%d",&p[i]);
		 
		 tot = 0;
		 for(i=0;i<n;i++)
		 {
		 
		 	tot+=p[i];
		 }
		 vector<string>ans;
		 string str;
		 int c,nxt;
		 bool f;
		 while(tot>0)
		 {
		 	str = "";
			c = 0;
			for(i=0;i<n;i++)
			{
				if(p[i]>c)
				{
					c = p[i];
					nxt = i;
				}
			}
			tot--;
			p[nxt]--;
		 	str += char('A'+nxt);
		    //cout<<"tot: "<<tot<<endl;
			 if(tot>1){
			 
			 for(i=0;i<n;i++)
			 {
			 	// cout<<p[i]<<endl; 
			 	 f = 1;
			 	if(p[i]>0)
			 	{
			 	   p[i]--;
					tot--;
					f = 0;
					for(j=0;j<n;j++)
					{
					   if(p[j]>tot/2)
					   {
					     f = 1;	
					   } 
					 
					}
					//cout<<i<<" "<<f<<" "<<tot<<endl;
					if(f==0)
					{
					    str += char('A'+i);	
					}
					else
					{
						p[i]++;
						tot++;
					}	
				}
				if(f==0)
				break;
			}
		   }
			else
			{
				for(i=0;i<n;i++)
		    	{
		 		if(p[i]>0)
		 		{
		 			str+=char('A'+i);
		 			tot--;
		 			p[i]--;
				 }
			   }
			}
		 	ans.push_back(str);
		  
		 }
	      
		 
		 int len = ans.size();
		 printf("Case #%d: ",t);
		 for(i=0;i<len;i++)
		 cout<<ans[i]<<" ";
		 cout<<endl;
	 
	 
	 }	

}

