#include<iostream>

using namespace std;

int main()
{
  int t;
  cin>>t;
  for(long long i=1; i<=t; i++)
  {
    string S;
    int Arr, compArr;
    cin>>S;
    if(S.size() == 0)
    {
      cout<<"Case #"<<i<<": 0"<<endl;
      continue;
    }

    if(S[0] == '-')
    {
      Arr = 1;
      compArr = 0;
    }
    else
    {
      Arr = 0;
      compArr = 1;
    }
    //cout<<"0 "<<Arr<<" "<<compArr<<endl;
    for(int j=1; j<S.size(); j++)
    {
      if(S[j] == '-')
        Arr = 1 + compArr;
      else
        compArr = 1 + Arr;
      //cout<<j<<" "<<Arr<<" "<<compArr<<endl;
    }
    cout<<"Case #"<<i<<": "<<Arr<<endl;
  }
  return 0;
}
