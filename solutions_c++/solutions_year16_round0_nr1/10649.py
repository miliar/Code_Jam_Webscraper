#include <bits/stdc++.h>
#define ull unsigned long long
#define ll long long
#define ff first
#define ss second
#define pb push_back
#define ins insert
#define mp make_pair
#include <fstream>
#define iOS ios::sync_with_stdio(false)
using namespace std;

struct sort_pred {
    bool operator()(const std::pair<int,int> &left, const std::pair<int,int> &right) {
        return left.second < right.second;
    }
};

int main()
{
		ofstream fout ("test.out");
    ifstream fin ("A-large.in");
		int n;
		fin>>n;
		ll int a[n];
		

    
		for(int i=0;i<n;i++)
		fin>>a[i];
		
		for(int i=0;i<n;i++)
		{
			if(a[i]!=0)
			{
				int arr[10];
				for(int j=0;j<10;j++)
				arr[j]=0;
				
				int sum=0;
				ll int s=a[i];						
				while(sum<10)
				{
					ll int t=a[i];
					while(t!=0)
					{
						int u=t%10;
						if(arr[u]==0)
						{
						arr[u]=1;
						sum++;}
						t/=10;
						//cout<<u;
					}
					if(sum==10)
					break;	
					a[i]+=s;	
							
				}				
			}
			else
			{
				a[i]=-1;
			}
		}
		for(int i=0;i<n;i++)
		{
			if(a[i]==-1)
			fout<<"Case #"<<i+1<<':'<<' '<<"INSOMNIA"<<endl;
			else
				fout<<"Case #"<<i+1<<':'<<' '<<a[i]<<endl;
		}
		
		
	    return 0;
}
