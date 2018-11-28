#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("q2out.txt","w",stdout);
	long long int t,x=1;
	cin>>t;
	while(t--)
	{
		long long int d;
		cin>>d;
		long long int a[d],i,count[1000]={0},cmp=0,ans=0,cmp1=0,flag=0,max1,max2,max3;
		for(i=0;i<d;i++)
		{
			cin>>a[i];
			count[a[i]]++;
		}
		sort(a,a+d);
		max1 = a[d-1];
		max2 = a[d-2];
		max3= a[d-3];
		if(max1==9 && max2<=3)
		{
			ans = 5;
			flag=1;
		}
		else if(max1==9 && max2==9 && d==2)
		{
			ans = 7;
			flag=1;
			
		}
		else if(max1==9&&d==1)
		{
			ans = 5;
			flag=1;
		}
		else if(max1==9&& max2==6 && d==2)
		{
			ans = 6;
			flag=1;
		}
		else if(max1==9&& max2==6 && a[d-3]<=3)
		{
			ans = 6;
			flag=1;
		}
		else if(max1==6 && max2<=3)
		{
			ans = 4;
			flag=1;
		}
		else if(max1==6 && max2==6 && d==2)
		{
			ans = 5;
			flag=1;
			
		}
		else if(max1==6 &&d==1)
		{
			ans = 4;
			flag=1;
		}
		else if(max1==7 && max2<=4)
		{
			ans = 5;
			flag=1;
		}
		else if(max1==7 && max2==7 && d==2)
		{
			ans = 6;
			flag=1;
			
		}
		else if(max1==7 &&d==1)
		{
			ans = 5;
			flag=1;
		}
		else if(max1==8 && max2<=4)
		{
			ans = 5;
			flag=1;
		}
		else if(max1==8 && max2==8 && d==2)
		{
			ans = 6;
			flag=1;
			
		}
		else if(max1==8 &&d==1)
		{
			ans = 5;
			flag=1;
		}
		else if(max1==4 &&d==1)
		{
			ans = 3;
			flag=1;
		}
		else if(max1==4 && max2==4&&d==2)
		{
			ans = 4;
			flag=1;
		}
		else if(max1==4 &&max2==4&&max3<=2)
		{
			ans = 4;
			flag=1;
		}
		else
		{
		
		
		for(i=d-1;i>=0;i--)
		{
			//cout<<a[i-1]<<endl;
			if(cmp>=a[i])
			{
				//cout<<"hf"<<endl;
			ans = ans + cmp;
			flag=1;
			break;
		}
			
			
		if((count[a[i]]+cmp) < a[i])
		{
			ans = ans + count[a[i]] ;
			if(a[i]%2==0)
			{
				cmp1 = a[i]/2;
				if(cmp1>cmp)
				{
					cmp = cmp1;
				}
			}
			else
			{
			cmp1 = a[i]/2 + 1;
			if(cmp1>cmp)
			{
				cmp = cmp1;
			}
		}
		}
		else
		{
		
		ans = ans + a[i];
		flag=1;
		break;
	}
	//cout<<i<<endl;
	//cout<<count[a[i]]<<endl;
		i = i - count[a[i]]+1;
		if(i==0)
		{
			ans = ans + cmp;
			flag =1;
			break;
		}
		//cout<<i<<endl;
		//cout<<ans<<endl;
		//cout<<cmp<<endl;
		//cout<<i<<endl;
	}}
	if(flag!=1)
	{
		if(a[0]%2==0)
		ans = ans + a[0]/2 +1; 
		else
		ans = ans + a[0]/2 +2;
	}
	if(ans>max1)
	ans = max1;
	cout<<"Case"<<" "<<"#"<<x<<":"<<" "<<ans<<endl;
		x++;
}}
