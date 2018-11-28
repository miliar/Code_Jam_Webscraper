# include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("BIGA.out", "w", stdout);
	int t,k,i,j,n,x;
	char str[2005];
	cin>>t;
	for(k=1;k<=t;k++)
	{
		x=0;
		cin>>str;
		sort(str,str+strlen(str));
		int arr[26]={0},b[10]={0};
		for(i=0;i<strlen(str);i++)
		{
			arr[str[i]-'A']++;
		}
		x=arr[25];
		b[0]=x;
		arr[25]-=x;
		arr[4]-=x;
		arr[17]-=x;
		arr[14]-=x;
		
		x=arr[22];
		b[2]=x;
		arr[19]-=x;
		arr[22]-=x;
		arr[14]-=x;
		
		x=arr[20];
		b[4]=x;
		arr[5]-=x;
		arr[14]-=x;
		arr[20]-=x;
		arr[17]-=x;
		
		x=arr[14];
		b[1]=x;
		arr[14]-=x;
		arr[13]-=x;
		arr[4]-=x;
		
		x=arr[6];
		b[8]=x;
		arr[4]-=x;
		arr[8]-=x;
		arr[6]-=x;
		arr[7]-=x;
		arr[19]-=x;
		
		x=arr[23];
		b[6]=x;
		arr[18]-=x;
		arr[8]-=x;
		arr[23]-=x;
		
		x=arr[17];
		b[3]=x;
		arr[19]-=x;
		arr[7]-=x;
		arr[17]-=x;
		arr[4]-=x;
		arr[4]-=x;
		
		x=arr[5];
		b[5]=x;
		arr[5]-=x;
		arr[8]-=x;
		arr[21]-=x;
		arr[4]-=x;
		
		x=arr[18];
		b[7]=x;
		arr[18]-=x;
		arr[4]-=x;
		arr[21]-=x;
		arr[4]-=x;
		arr[13]-=x;
		
		x=arr[8];
		b[9]=x;
		arr[13]-=x;
		arr[8]-=x;
		arr[13]-=x;
		arr[4]-=x;
		
		cout<<"Case #"<<k<<": ";
		for(i=0;i<10;i++)
		{
			while(b[i]>0)
			{
				cout<<i;
				b[i]--;
			}
			
		}
		cout<<endl;
	}
	return 0;
}
