#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int k=0;k<t;k++)
	{
		int n;
		cin>>n;
		double naomi[10],ken[10];
		for(int i=0;i<n;i++)
			cin>>naomi[i];
		for(int i=0;i<n;i++)
			cin>>ken[i];
		sort(naomi,naomi+n);
		sort(ken,ken+n);
		int i=0,j=0,count=0;
		while((j<n)&&(i<n))
		{	
			if(naomi[i]<ken[j])
			{	i++;
				j++;
				count++;
			}
			else if(naomi[i]>ken[j])
			{	j++;	}
		}
		//cout<<i<<"  " <<j<<endl;
		i=0;j=0;
		int count1=0;
		while((j<n)&&(i<n))
                {
                        if(naomi[i]<ken[j])
                        {      
				 i++;
                        }
                        else if(naomi[i]>ken[j])
                        {      i++,j++,count1++;    }
                }

		cout<<"Case #"<<k+1<<": "<<count1<<" "<<n-count<<endl;
	}
}

