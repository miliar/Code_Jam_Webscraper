#include<iostream>
using namespace std;

int main()
{
  int n;
  cin>>n;
  for(int k=0;k<n;k++)
  {
    bool imp = 0;
    string input;
    int pan;
    cin>>input>>pan;
    int takes = 0;
    int len = input.length();
    for(int i=0;i<=len-pan;i++)
    {
      if(input[i] == '-')
      {
        takes++;
        for(int z=0;z<pan;z++)
        {
          if(input[i+z] == '+')
            input[i+z] = '-';
          else
            input[i+z] = '+';
        }
      }
    }
    for(int i = len-pan+1;i<len;i++)
    {
      if(input[i] == '-')
      {
        imp = true;
        break;
      }
    }
    cout<<"case "<<"#"<<k+1<<": ";
    if(!imp)
      cout<<takes<<endl;
    else
      cout<<"IMPOSSIBLE"<<endl;
  }
  return 0;
}
