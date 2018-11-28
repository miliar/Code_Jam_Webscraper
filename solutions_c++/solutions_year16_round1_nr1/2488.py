#include <iostream> 
#include <bits/stdc++.h>
    // std::cout, std::endl
#include <iomanip> 
#include <math.h>

using namespace std;
int main()
{
	int t,p=0;
	cin>>t;
	int i,j,in,de,l;
    char a[10000],b[10000];


	while(t--)
	{	p++;
		 in=1010;
        de=1009;
        cin>>a;
        l=strlen(a);
        b[de]=a[0];
        for(i=1;i<l;i++)
        {
            if(b[de]>a[i])
            b[in++]=a[i];
            else
            b[--de]=a[i];
        }
		cout<<"Case #"<<p<<": ";
		  for(i=de;i<in;i++)
        {
            cout<<b[i];
        }
        cout<<"\n";


	}

	return 0;
}


