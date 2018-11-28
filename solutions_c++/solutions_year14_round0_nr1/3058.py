  #include <iostream>
  #include<cstdio>
  #include<algorithm>
    #define getcx getchar_unlocked
    #define ll unsigned long long
    
    using namespace std;
    inline long long int inp()//fast input function
    {
    long long int n=0;
    int ch=getcx();int sign=1;
    while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getcx();}
    while( ch >= '0' && ch <= '9' )
    n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
    return n;
    }
  
  
  
  
  
  
  
    int main()
  {
  	freopen("input.txt","r",stdin);
  	freopen("output.txt","w",stdout);
  	ll t,l,a[4],b[4],c,d,i,j,count,m;
  	t=inp();
  	for(l=1;l<=t;l++)
  	{
  		count=0;
  		c=inp();
  		for(i=1;i<=4;i++)
  		{
  			if(i!=c)for(j=0;j<4;j++)inp();
  			else for(j=0;j<4;j++)a[j]=inp();
  		}
  		
  		d=inp();
  		for(i=1;i<=4;i++)
  		{
  			if(i!=d)for(j=0;j<4;j++)inp();
  			else for(j=0;j<4;j++)b[j]=inp();
  		}
  		sort(a,a+4);
  		sort(b,b+4);
  		for(i=0,j=0;i<4 && j<4;)
  		{
  			if(a[i]>b[j])j++;
  			else if(a[i]<b[j])i++;
  			else {count++;m=i;i++;j++;}
  		}
  		if(!count)cout<<"Case #"<<l<<": Volunteer cheated!\n";
  		else if(count>1)cout<<"Case #"<<l<<": Bad magician!\n";
  		else cout<<"Case #"<<l<<": "<<a[m]<<"\n";
  	}
  		return 0;
  }
