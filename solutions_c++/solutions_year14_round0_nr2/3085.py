  #include <iostream>
  #include<cstdio>
  #include<iomanip>
    
    using namespace std;

    int main()
  {
  	freopen("input.txt","r",stdin);
  	freopen("output.txt","w",stdout);
  	double c,f,x,r,l,t1,t2,temp,wait;
  	long long t;
  	cin>>t;
  	for(l=1;l<=t;l++)
  	{
  		r=2;
  		cin>>c>>f>>x;
  		t1=x/r;
  		temp=c/r;
  		wait=x/(r+f);
  		t2=temp+wait;
  		while(t2<t1)
  		{
  			t1=t2;
  			r+=f;
  			temp+=c/r;
  			wait=x/(r+f);
  			t2=temp+wait;
  		}
  		
  		if(t1!=int(t1))cout<<"Case #"<<l<<": "<<setprecision(9)<<t1<<"\n";
  		else cout<<"Case #"<<l<<": "<<setprecision(9)<<t1<<".0000000\n";
  	}
  		return 0;
  }
