#include<bits/stdc++.h>
using namespace std;
/*      my general mistakes that costed me a lot
          * check for overflows
          * check and mod and use int type variables where possible to avoid tles
          * while multiplying two variables whose value can exceed integer 
          limt make sure to typecase them
          * use scanf when you are not working with the best possible optimisation
          * return a value from a function that has a return type sometimes the 
          compiler may give the correct answer but there will be problem in the judge
          * be very cautious about uninitiaalised variables , infact never keep them
          or handle them properly*/
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define ll long long int
#define pp pair<int,int> 
#define ve vector
#define mod 1000000007
/************************************CODE BEGINS HERE************************/
int a[30];
int main()
{
            freopen("abc.in","r",stdin);
            freopen("out1.txt","w",stdout);
              int tt=0;
			  int t;
			  cin>>t;
			  while(t--)
			  {
			  	   tt++;
			  	   int n;
			  	   cin>>n;
			  	   memset(a,0,sizeof(a));
			  	   for(int i=0;i<n;i++)
			  	   {
			  	   	  cin>>a[i];
			  	   	  
				   }
				   vector<string> res;
				while(1)
				{
					    int sum=0;
					     priority_queue<pair<int,int> > pq;
					    for(int i=0;i<n;i++)
					    {
					           sum+=a[i];	 
						}
					//	cout<<"sum "<<sum<<endl;
						if(sum==0)
						break;
						int mx=0;
						int pos1=-1;
						int pos2=-1;
						string temp="";
						for(int i=0;i<n;i++)
						{
						   	   if(a[i]>mx)
								  {
								  	 mx=a[i];
								  	 pos1=i;
								   } 
						}
						mx=0;
						for(int i=0;i<n;i++)
						{ 
						          if(i!=pos1 && a[i]>mx)
						          {
						          	  mx=a[i];
						          	  pos2=i;
								  }
						}
						a[pos1]--;
						a[pos2]--;
						mx=0;
						int tsum=0;
					//	cout<<"pos1 "<<pos1<<" "<<pos2<<endl;
						for(int i=0;i<n;i++)
						{
							   if(a[i]>mx)
							   mx=a[i];
							   tsum+=a[i];
						}
						
					
					//	cout<<"left sum "<<tsum<<" "<<mx<<endl;
						
						if(mx>=(tsum/2)+1)
						{
					//		cout<<"haan "<<endl;
							    temp+=char('A'+pos1);
							    a[pos2]++;
							    res.pb(temp);
						}
						else
						{
							   temp+=char('A'+pos1);
							   temp+=char('A'+pos2);
							   res.pb(temp);
						}
				}
				cout<<"Case #"<<tt<<": ";
				int l=res.size();
				for(int i=0;i<l;i++)
				cout<<res[i]<<" ";
				cout<<endl;
			}	
			return 0;
}
