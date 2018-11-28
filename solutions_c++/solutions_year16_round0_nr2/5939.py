#include <iostream>
#include <queue>
#include <stack>

using namespace std;

int main()
{
  int t;
  cin>>t;
  for( int c = 0 ; c < t ; ++c )
  {
    int n=0;
    char temp;
    string in;
    cin>>in;
    for( int i = 0; i < in.size() ; ++i  )
    {
      if( i == 0 )
      {
        temp = in[i];
        n++;
      }
      else if( temp != in[i] )
      {
        temp=in[i];
        n++;
      }
    }
    if(temp == '+')
      n--;
    cout<<"Case #"<<c+1<<": "<<n<<endl;
  }
  return 0;
}
