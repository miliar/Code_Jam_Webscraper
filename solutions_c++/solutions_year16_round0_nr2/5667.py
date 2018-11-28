#include<iostream>
#include<string>
using namespace std;

void swap(string& word)
{
  for(int i=0;i<word.size();i++)
  {
    if(word[i]=='+')
    {
      word[i]='-';
    }else{
      word[i]='+';
    }
  }
}

int revengePancakes(string &word)
{
  int times=0;
  for(int i=word.size()-1;i>=0;i--)
  {
    if(word[i]=='+')
    {
     continue;
    }
    swap(word);
    times++;
  }
  return times;
}

int main()
{
  string word;
  int test_input;
  int test_case=1;
  cin>>test_input;
  for(int i=0;i<test_input;i++){
     cin>>word;
     cout<<"Case #"<<test_case<<": "<<revengePancakes(word)<<endl;
     test_case++;
   }

}
