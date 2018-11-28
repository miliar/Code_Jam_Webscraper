#include<bits/stdc++.h>
using namespace std;
typedef long long int LL;
std::vector<int>v(105);
void cool(int j)
{
    vector<int>u;
    for(int f=0;f<=j;f++)
    {
    	u.push_back(1^v[f]);
    }
    int d=u.size();
    d--;
    for(int f=0;f<=j&&d>=0;f++)
    {
    	v[f]=u[d];
    	d--;
    }
}

int main()
{

	 ios_base:: sync_with_stdio(false); cin.tie(0);
	  
	 freopen("input.in","r",stdin);
	 freopen("output.in","w",stdout);
      
      int t;cin>>t;for(int tc=1;tc<=t;tc++)
      {
          string s;	 
      	 cin>>s;
      	 int n=s.size();
      	 
      	 for(int i=0;i<n;i++)
      	 {
      	 	if(s[i]=='+')
      	 		v[i]=1;
      	 	else
      	 		v[i]=0;
      	 }
          int res=0;
      	 for(int i=n-1;i>=0;i--)\
      	 {
             if(v[i]==0)
             {
             	if(v[0]==0)
             	{
                  cool(i);
                  res++;
             	}
                else
                {
                	 int j=i;
                	 while(j>=0&&v[j]!=1)
                	 	j--;
                	 cool(j);
                	 res++;
                	 cool(i);
                	 res++;
                }
             }
      	 }

       cout<<"Case #"<<tc<<": "<<res<<endl;
         
      }        
	 return 0;
}



