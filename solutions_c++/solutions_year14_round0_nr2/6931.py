    #include <iostream>
    #include<cstdio>
    using namespace std;
     
    int main()
    {
    int t;
    int s=1;
    double c,f,x;
    cin>>t;
    while(t--)
    {
    double d=2;
    double count=0;
    cin>>c>>f>>x;
    
    
    while(((c/d)+(x/(d+f)))<(x/d))
    {
    		count=count+(c/d);
		    	d=d+f;
    }
    
    cout<<"Case #"<<s<<": ";
    printf("%.7lf\n",count+(x/d));
    s++;
    
    }
    return 0;
    }