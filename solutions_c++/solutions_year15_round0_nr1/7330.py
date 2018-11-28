using namespace std;
#include<iostream>

int main()
{
	int t,j,num,ans,sum;
	int max;
        char s[1001];
        cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>max;
		cin>>s;
		j=0;
		sum=0;
		ans=0;
                while(s[j]!='\0')
		{
			num=s[j]-48;
			if(sum<j)
			{
				ans+=j-sum;
				sum+=j-sum;	
			}
			sum+=num;			
			j++;	
		}
		cout<<"Case #"<<i+1<<": "<<ans<<"\n";
	}	

}

