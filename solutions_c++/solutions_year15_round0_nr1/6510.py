#include <iostream>
#include <fstream>
using namespace std;
//parsetoint(int ch)
/*{
    switch(ch)
    {
      case
    }
}
*/
int main()
{
    //cout << "Hello world!" << endl;
    int T , Sm ;
    cin>>T ;
    char ch[1001];
    for(int j =0 ;j<T;j++)
    {
      cin>> Sm ;
      cin>>ch ;
      int f=0 ;
      int sum = (int)(ch[0]) - 48 ;
    // cout<<"sum"<<sum ;
      for(int i = 1 ; i<= Sm ; i++)
      {
        if((sum<i)&&((int)ch[i]!=48))
        {
          f += (i-sum) ;
          sum = i ;
        }
        sum = sum + ((int)ch[i]-48) ;
      }
      cout<<"Case #"<<j+1<<": "<<f<<endl;
    }

    return 0;
}