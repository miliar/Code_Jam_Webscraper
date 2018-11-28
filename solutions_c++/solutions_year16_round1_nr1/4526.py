#include <iostream>

using namespace std;


string rec(string &word,int pos,string temp)
{
  if(pos==word.size())
    return temp;
  string a=rec(word,pos+1,temp+word[pos]);
  string b=rec(word,pos+1,word[pos]+temp);
  return a>b?a:b;
}
int main()
{
  int n;
  cin>>n;
  for( int i = 0 ; i < n ; ++i )
  {
    string word,temp="";
    cin>>word;
    cout<<"Case #"<<i+1<<": "<<rec(word,0,temp)<<endl;
  }

  return 0;
}
