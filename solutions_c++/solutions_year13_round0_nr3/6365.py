  #include<iostream>
  #include<cstdio>
  #include<cmath>
  #include<cstdlib>
  #include<cstring>
  #include<algorithm>
  #include<vector>
  #include<stack>
  #include<deque>
  #include<queue>
  #include<utility>
  # define U unsigned long long int
  # define L long long int
  # define INF 2147483648
  using namespace std;
  
  int palin(int n)
  {
      int x=n;
      int s=0;
      while(n>0)
      {
         s=s*10+n%10;
         n/=10;          
      }
      if(x==s)return 1;
      else return 0;    
  }
  
  int main()
  {
       int t;
       cin>>t;
       for(int tc=1;tc<=t;tc++)
       {
          int a,b,n=0;
          cin>>a>>b;
          int c=ceil(sqrt(a)),d=floor(sqrt(b));
          for(int i=c;i<=d;i++)
          {
              if(palin(i))
              {
                 int j=i*i;
                 if(palin(j))
                 {
                    n++;            
                 }               
              }       
          }
          cout<<"Case #"<<tc<<": "<<n<<endl;         
       }
  }
