#include<bits/stdc++.h>
using namespace std;
int main()
{
  int x=0,tc;
  cin>>tc;
  vector<string > cas;
  while(x!=tc)
  {
    long long int y;
    cin>>y;
    if(y==0)
    cas.push_back("INSOMNIA");
    else
    {
     	long long int temp=y;
    	string str;
    	vector<char > v{'0','1','2','3','4','5','6','7','8','9'};
    	int j=1;
    while(!(v.empty()))
    {
      str=to_string(temp);
      int i=0;
      while(str[i]!='\0')
      {
        if(find(v.begin(), v.end(), str[i])!= v.end())
        v.erase(remove(v.begin(), v.end(), str[i]), v.end());
        i++;
      }
      j++;
      temp=j*y;
    }
  cas.push_back(str);
  }
    x++;
  }
  for (int m=0; m!=cas.size(); ++m)
{

     cout<<"\nCase #"<<m+1<<":"<<" "<<cas[m];
}
cout<<"\n";
return(0);
}
