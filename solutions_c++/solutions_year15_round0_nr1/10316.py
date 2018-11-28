#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int num(char x)
{

    return ((int)x-(int)'0');
}
int main()
{

    int cases;
    cin>>cases;
    for(int j=1;j<=cases;j++)
    {

        int N;
        cin>>N;
string X;
cin>>X;

long long count=0;
long long  friends=0;

for(int i=0;i<=N;i++)
{
  if(i>count && X.at(i)!='0' )
    {
    friends+=(i-count);
    count+=(num(X.at(i))+(i-count) );
    }
  else
  count+=num(X.at(i));
}

      cout<<"Case #"<<j<<": "<<friends<<endl;
    }
    return 0;
}
