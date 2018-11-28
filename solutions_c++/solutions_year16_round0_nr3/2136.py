#include<bits/stdc++.h>
using namespace std;
set<string> set1;
string getStr(int i,int n)
{

  string answer ="";
  int limit = (n-4)/2;
  for(int j=1;j<=limit;j++)
  {
    int last = i%2;
    if(last==1)
      answer+="11";
    else
      answer+="00";
    i/=2;
  }
  answer+="11";
  answer="11"+answer;
  set1.insert(answer);
  return answer;
}
int main()
{
  int t;
  scanf("%d\n",&t);
  for(int gh=1;gh<=t;gh++)
  {
    int n,k;
    cin>>n>>k;
    printf("Case #%d:\n",gh);
    for(int i=1;i<=k;i++)
    {
      string str = getStr(i,n);
      cout<<str<<" ";
      for(int j=2;j<=10;j++)
        cout<<j+1<<" ";
      cout<<endl;
    }
    //cout<<set1.size()<<endl;

  }
  return 0;
}
