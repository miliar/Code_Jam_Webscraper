#include<bits/stdc++.h>
#define ll long long int
#define F first
#define S second
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define rep(i,in1,n) for(i=in1;i<=n;i++)
#define repd(i,in1,n) for(i=in1;i>=n;i--)

#define pf(n) printf("%d ",n);
#define sf(n) scanf("%d",&n)
#define sl(n) scanf("%I64d",&n)
#define nl printf("\n")
#define mem(arr,init) memset(arr,init,sizeof(arr))
#define vi vector<int>
#define vvi vector<vi>

#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define mp make_pair
#define ep emplace_back//c++11
#define ii pair<int,int>
#define iii pair<ii,i>
//	freopen("input.txt","r",stdin);
  //  freopen("output.txt","w",stdout);
using namespace std;


int arr[27];
map<ii,int> map1;

int main()
{
	int i,j,k,t,n,m,a,b,c,x,y,z,cs;
	freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    for(cs=1;cs<=t;cs++)
    {
    	cin>>n;
    	int tot=0;
    	for(i=1;i<=n;i++)
    	{
    		cin>>x;
    		tot+=x;
    		arr[i]=x;
    		map1[mp(x,i)]++;
		}
		
		printf("Case #%d: ",cs);
		char ch;
		if(tot%2)
		{
			auto it1=map1.end();
			it1--;
			string s1;
			char ch1=(it1->F.S+'A'-1);
			s1+=ch1;
			
			int x1,x2,i1,i2;
				x1=it1->F.F; i1= it1->F.S;
				x1--;
				
				map1.erase(it1);
				//	map1.erase(it2);
				
				if(x1>0)
				{
					map1[mp(x1,i1)]++;
					
				}
				cout<<s1<<" ";
			
			
		}
	
		while(!map1.empty())
		{
			string s1;
		//	cout<<map1.size()<<"<----  ";
		//	nl;
			if(map1.size()>=2)
			{
				auto it1=map1.end();
				auto it2=map1.end();
				it1--;
				it2--;
				it2--;
				
				
				char ch1,ch2;
				ch1=(it1->F.S+'A'-1);
				s1+=ch1;
				
				ch2=(it2->F.S+'A'-1);
				//cout<<ch1<<" # "<<ch2;
				//nl;
				s1+=ch2;
				
			//	cout<<ch1<<" # "<<ch2;
				
				int x1,x2,i1,i2;
				x1=it1->F.F; i1= it1->F.S;
				x1--;
				
				x2=it2->F.F; i2= it2->F.S;
				x2--;
				
				
					map1.erase(it1);
					map1.erase(it2);
				
				if(x1>0)
				{
					map1[mp(x1,i1)]++;
					
				}
				if(x2>0)
				{
					map1[mp(x2,i2)]++;
					
				}
				
				cout<<s1<<" ";
				continue;
			}
			
			
			
		}
		nl;
    	
	}



	return 0;
}



