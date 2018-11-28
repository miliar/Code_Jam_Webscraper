#include<iostream>
#include<string>
using namespace std;
int chartoint(char c)
{
  return (int)c-(int)'0';
}
int main()
{
  int t,size;
  string s;
  int testcase,i;
  int cumulative,additional,totalextra;
  cin>>t;
  for(testcase = 1 ;testcase <=t; testcase++)
  {
    cin>>size;
    cin>>s;
    cumulative = additional = totalextra = 0;
    for(i=0;i<=size;i++)
    {
      additional = 0;
      if(s[i]!='0' && cumulative < i)
      {
        additional = i - cumulative;
      }
      cumulative +=  (chartoint(s[i]) + additional);
      totalextra += additional;

    }
    cout<<"Case #"<<testcase<<": "<<totalextra<<"\n";
  }
  return 0;

}
