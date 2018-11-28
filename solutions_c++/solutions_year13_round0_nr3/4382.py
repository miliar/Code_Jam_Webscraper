#include<iostream>
#include<math.h>
#include<stdio.h>
#include<string.h>
using namespace std;
int main()
{
	long long int t,a,b,num = 1,i,j,k,ans;
	int smaller,beg,end,len;
	char buffer[15];
	bool palindrome;
	long long int fairandsquare[]={1,4,9,121,484,676,10201,12321,14641,40804,44944,69696,94249,698896,1002001,1234321,4008004,5221225,6948496,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,522808225,617323716,942060249,10000200001,10221412201,12102420121,12345654321,40000800004,637832238736,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1086078706801,1210024200121,1212225222121,1214428244121,1230127210321,1232346432321,1234567654321,1615108015161,4000008000004,4004009004004,4051154511504,5265533355625,9420645460249};
	cin>>t;
	while(num<=t)
	{
		cin>>a>>b;
		ans=0;
		palindrome = false;
		if(a>9420645460249)
			cout<<"Case #"<<num<<": 0"<<endl;
		else
		{
			i=0;
			while(a>fairandsquare[i])
				i++;
			if(b<9420645460249)
			{
				j=0;
				while(b>=fairandsquare[j])
					{
						//cout<<fairandsquare[j]<<endl;
						j++;
						//cout<<"j is "<<j<<endl;
					}
			}
			else
			j=55;
			//cout<<"THE LIMITS ARE i and j :: "<<i<<" "<<j<<endl;
			for(k=i;k<j;k++)
			{
				//cout<<"CHECKING FAIR AND SQUARE FOR ::"<<fairandsquare[k]<<endl;
				smaller=sqrtl((long double)fairandsquare[k]);
				sprintf(buffer,"%d",smaller);
				len=strlen(buffer);
				beg=0;
				end=len-1;
				while(beg<=end && buffer[beg] == buffer[end])
				{				
					beg++;
					end--;
				}
				if(beg<end)
				{
					palindrome = false;
				}
				else
				{
					palindrome = true;
					ans++;
				}
			}
			cout<<"Case #"<<num<<": "<<ans<<endl;
		}
		num++;
	}
	return 0;
}
