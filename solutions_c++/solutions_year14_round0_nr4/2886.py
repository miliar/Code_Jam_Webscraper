  #include <iostream>
  #include<cstdio>
  #include<algorithm>
    
    using namespace std;

    int main()
  {
  	freopen("input.txt","r",stdin);
  	freopen("output.txt","w",stdout);
  	double n[1000],k[1000];
  	long long t,m,two,one,i,j,l;
  	cin>>t;
  	for(l=1;l<=t;l++)
  	{
  		cin>>m;
  		for(i=0;i<m;i++)cin>>n[i];
  		for(i=0;i<m;i++)cin>>k[i];
  		sort(n,n+m);
  		sort(k,k+m);
  		two=0;
  		for(i=0,j=0;i<m && j<m;)
  		{
  			if(n[i]<k[j]){i++;two++;j++;}
  			else j++;	
  		}
  		two=m-two;
  		one=0;
  		for(i=m-1,j=m-1;i>=0 && j>=0;)
  		{
  			if(n[i]>k[j])
  			{
  				one++;
  				i--;j--;
  			}
  			else j--;
  		}
  			cout<<"Case #"<<l<<": "<<one<<" "<<two<<"\n";
  	}
  		return 0;
  }
