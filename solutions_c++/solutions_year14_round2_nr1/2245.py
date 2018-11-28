# include <iostream>
# include <string.h>
# include <vector>
# include <utility>
# include <algorithm>
# include <sstream>
using namespace std;
pair<vector<int>,string> convert(string str)
{   vector<int>ans;int arr[111];memset(arr,0,sizeof(int)*111);
	for(int i=0;i<str.size();i++)
	    arr[i]=1;
	string rem="";
	for(int i=1;i<str.size();i++)
	{   if(str[i]==str[i-1])
	    {   arr[i]+=arr[i-1];
	        arr[i-1]=0;
		}
	}
	for(int i=0;i<111;i++)
	{    if(arr[i]!=0)
	    {   ans.push_back(arr[i]);
	        rem+=str[i];
		}
	}
	return make_pair(ans,rem);
}

int main()
{   freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n_cases;cin>>n_cases;
	for(int id=0;id<n_cases;id++)
	{   int n_str;cin>>n_str;
	    vector<vector<int> >arr;
	    string a[2];
	    for(int take=0;take<n_str;take++)
	    {   string str;cin>>str;
			arr.push_back(convert(str).first);
			a[take]=convert(str).second;
		}
		if(arr[0].size()!=arr[1].size() || a[0]!=a[1])
		{   cout <<"Case #"<<id+1<<": Fegla Won\n";
		    continue;
		}
		int count=0;
		for(int i=0;i<arr[0].size();i++)
		    count+=abs(arr[0][i]-arr[1][i]);

        cout <<"Case #"<<id+1<<": "<<count<<endl;
	}
}
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	        
	    

