#include<iostream>
#include<string>
using namespace std;
int a[10005];
int p[5][5] = {
               {0,0,0,0,0},
               {0,1,2,3,4},
               {0,2,-1,4,-3},
               {0,3,-4,-1,2},
               {0,4,3,-2,-1},
               };

int prod(int a,int b)
{
  //   cout<<a<<" "<<b<<"\n"; 
     int s = 1;
     if(a*b<0)  
	s = -1;
     return s*p[a<0?0-a:a][b<0?0-b:b];
  
}
int div(int x, int z)
{
    return -1* prod(x,z);
}
void print(int x[],int n)
{
  for(int i =0;i<n;i++) cout<<x[i]<<" ";
  cout<<"\n";
}
int main()
{
  int t,c=1;
  cin>>t;
  while(c<=t)
  {
    int ans = 0;
    string s;
    int l,x;
    cin>>l>>x;
    cin>>s;
    a[0] = 1;
    for(int i = 0;i<l*x;i++)   
    {
      char ch  = s[i%(l)]-'g';
      a[i+1] = prod(a[i],ch);
    //  cout<<a[i+1]<<"\n";
    }
 // print(a,l*x+1);
    for(int i = 1;i<=l*x;i++)
    {
      for(int j = i+1;j<=l*x;j++)
      {
         int s1 = a[i];
         int s2 = div(s1,a[j]);
         int s3 = div(a[j],a[l*x]);
//         cout<<i<<" "<<j<<" "<<s1<<" "<<s2<<" "<<s3<<"\n";
         if(s1 == 2 && s2==3 && s3== 4) 
	 {
           ans =1; break;
         }
         
      }
    }
    if(ans)
       cout<<"Case #"<<c<<": "<<"YES\n";
    else
      cout<<"Case #"<<c<<": "<<"NO\n";
    c++;
  }
}
