#include<bits/stdc++.h>

using namespace std ;

int main()
{

     freopen("poke.in","r",stdin);
     freopen("poke.out","w",stdout);
 int t;
 cin>>t;

 for(int kk=1;kk<=t;kk++)
 {

       long long int n,i,j,maxi,m1,summ=0;
        cin>>n;
		int marray[n];

		for(j=0;j<n;j++) cin>>marray[j];

        maxi=marray[0];
		j=1;

		while(j<n) { if(marray[j]>maxi)maxi=marray[j]; j++; }

 m1=maxi,summ;

		for(i=1;i<maxi+1;i++)
		{
			summ=i;
			for(j=0;j<n;j++)
			{
				if(marray[j]>i)
				{
					if(marray[j]%i==0)
						summ+=((marray[j]/i)-1);
					else
						summ+=marray[j]/i;
				}

			}
			m1=min(m1,summ);
		}

		cout<<"Case #"<<kk<<": "<<m1<<endl;
	}

	return 0;
}
