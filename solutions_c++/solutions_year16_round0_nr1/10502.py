#include <bits/stdc++.h>
using namespace std;

int main() {

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t,j;
    cin >> t;
    long long int n,z;
    for(int i=1;i<=t;i++) 
	{
        cin >> n;
        int x=0,flag=0;
        if(n==0)
        {
        	cout << "Case #" <<i<<": INSOMNIA" << endl;
		}
		else
		{
			long long int m=n;
			int a[10];
			for(j=0;j<=9;j++)
			{
				a[j]=0;
			}
			while(1)
			{
				x++;
				m=n*x;
				z=m;
				flag=0;
				while(z>0)
				{
					int p=z%10;
					a[p]=1;
					z=z/10;
				}
					
				
				for(j=0;j<=9;j++)
				{
					if(a[j]==0)
					{
						flag=1;	
					}	
				}
				
				if(flag==0)
					break;
			}
			cout << "Case #" << i <<": "<<m << endl;
		}
        
    }
    return 0;
}

