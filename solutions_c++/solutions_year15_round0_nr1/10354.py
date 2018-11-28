#include<iostream>
#include<string>
int min_invites(int smax,std::string s)
{
  if(!smax)
    return 0;
  if(smax==1 && s[0]=='0')
    return 1; 
  int n=s.length(),count=s[0]-48, min_inv=0;
  for(int i=1;i<n;++i)
  {
    if(s[i]!='0')
    {
      int prev_count=count;
      count+=s[i]-48;
      if(i>prev_count)
      {
	min_inv+=i-prev_count;
	count+=min_inv;
      }
    }
  }
  return min_inv;    
}
int main()
{
  int t,i=1;
  std::cin>>t;
  while(t--)
  {
    int smax;
    std::cin>>smax;
    std::string  s;
    std::cin>>s;
    int c=min_invites(smax,s);
    std::cout<<"Case #"<<i++<<": "<<c<<std::endl;
  }
}