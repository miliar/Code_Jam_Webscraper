#include<bits/stdc++.h>
typedef long long ll;
using namespace std;



void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}


void swapc(char *xp, char *yp)
{
    char temp = *xp;
    *xp = *yp;
    *yp = temp;
}
 
// A function to implement bubble sort
void bubbleSort(int arr[],char arrs[], int n)
{
   int i, j;
   for (i = 0; i < n-1; i++)      
 
       // Last i elements are already in place   
       for (j = 0; j < n-i-1; j++) 
           if (arr[j] > arr[j+1])
              {
              	swap(&arr[j], &arr[j+1]);
              	swapc(&arrs[j], &arrs[j+1]);
              	
              }
}




int main()
{
	
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	ll t;
	cin>>t;
	for(ll i=0;i<t;i++)
	{
		
		int n;
		cin>>n;
		ll sum=0;
		int p[n];
		char ps[n];
		
		for(int i=0;i<n;i++)
		{
			ps[i]=i+'A';
		}
		for(int i=0;i<n;i++)
		{
			
			cin>>p[i];
			sum+=p[i];
			
		}
		
		int ctr=0;
		if(sum%2==0)
		ctr=sum/2;
		
		else
		ctr=(sum/2)-1;
		
		
		cout<<"Case #"<<(i+1)<<": ";
		while(ctr--)
		{
			bubbleSort(p,ps,n);
			if(p[n-1]==p[n-2])
			{
				p[n-1]--;
				p[n-2]--;
				cout<<ps[n-1]<<""<<ps[n-2]<<" ";
				
			}
			
			else{
				p[n-1]-=2;
				cout<<ps[n-1]<<""<<ps[n-1]<<" ";
			}
		}
		
		
		
		if(sum%2!=0)
		{
			p[0]--;
			cout<<ps[0]<<" ";
			
			for(int i=1;i<n;i=i+2)
			{
				p[i]--;
				p[i+1]--;
				cout<<ps[i]<<""<<ps[i+1]<<" ";
			}
		}
		
		cout<<endl;	
		
		
	}
	
	return 0;
}
	

