#include<iostream>
#include<cstdio>
#include<climits>
#include<vector>
#include<algorithm>
#include<utility>
#include<cmath>
#include<queue>
#include<map>
#define read(x) scanf("%d",&x)
#define write(x) printf("%d\n",x)
typedef long long int ull;
using namespace std;

map <string,map<string,string> > mp;

int main()
{
	int l,x,i,j,k,t,tc;
	mp["1"]["1"]="1";mp["1"]["i"]="i";mp["1"]["j"]="j";mp["1"]["k"]="k";
	mp["i"]["1"]="i";mp["i"]["i"]="-1";mp["i"]["j"]="k";mp["i"]["k"]="-j";
	mp["j"]["1"]="j";mp["j"]["i"]="-k";mp["j"]["j"]="-1";mp["j"]["k"]="i";
	mp["k"]["1"]="k";mp["k"]["i"]="j";mp["k"]["j"]="-i";mp["k"]["k"]="-1";
	read(t);
	for(tc=1;tc<=t;tc++)
	{
		cin>>l>>x;
		string s,ans[10001],base;
		cin>>base;
		
		for(i=0;i<x;i++)
			s+=base;
		//cout<<s<<endl;
	    string temp;
		temp+=s[0];
		ans[0]=temp;
		//cout<<ans[0]<<endl;
		for(i=1;i<l*x;i++)
		{
			temp.clear();
			temp+=s[i];
			string a,b;
			int mc=0;
			if(ans[i-1][0]=='-')
				{
					a=ans[i-1].substr(1);
					mc++;
				}
				else a=ans[i-1];
		    if(temp[0]=='-')
				{
					b=temp.substr(1);
					mc++;
				}
				else b=temp;		

        
        ans[i]=mp[a][b];
        if(mc&1)
        	{
        		if(ans[i][0]=='-')
        		ans[i]=ans[i].substr(1);
        	else ans[i]='-'+ans[i];
        	}
       // cout<<ans[i]<<endl;
        }

        
        int flag=0;
        if(ans[l*x-1]=="-1")
        {
        for(i=0;i<l*x-2 && !flag;i++)
        if(ans[i]=="i")
        for(j=i+1;j<l*x-1;j++)
        {
        	if(ans[j]=="k")
        		{
        			flag=1;
        			//cout<<"ans "<<i<<" "<<j<<endl;
        			break;
        		}
        }
       }
        
        printf("Case #%d: %s\n",tc,(flag==1)? "YES":"NO");
    }


}