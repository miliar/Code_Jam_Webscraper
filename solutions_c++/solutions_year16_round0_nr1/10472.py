#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>


struct myclass {
  bool operator() (int i,int j) { return (i<j);}
} myobject;


using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("OutAnswer.out","w",stdout);

   long int T = 0;
   long int N = 0;
    cin >> T ;
    vector<int> Numbers;
   long int x = 0;
   long int counter = 0;
   long int Result = 0;
    counter = 1;
    for (int i = 1;i <= T; i++)
    {
       // cout << "N= " << N << " x= " << x << " Result= " << Result ;
        cin >> N ;
        if(N == 0){
            cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
                }
                else {

        x = N ;
        Here :
        Result = x;
        while(x> 0)
        {
             Numbers.push_back(x%10);
             x/=10;
        }
        sort(Numbers.begin(), Numbers.end(), myobject);
        x=N*counter;
        counter++ ;

      if(find(Numbers.begin(), Numbers.end(), 0) != Numbers.end()  && find(Numbers.begin(), Numbers.end(), 1) != Numbers.end() && find(Numbers.begin(), Numbers.end(), 2) != Numbers.end() && find(Numbers.begin(), Numbers.end(), 3) != Numbers.end() && find(Numbers.begin(), Numbers.end(), 4) != Numbers.end() && find(Numbers.begin(), Numbers.end(), 5) != Numbers.end() && find(Numbers.begin(), Numbers.end(), 6) != Numbers.end() && find(Numbers.begin(), Numbers.end(), 7) != Numbers.end() && find(Numbers.begin(), Numbers.end(), 8) != Numbers.end() && find(Numbers.begin(), Numbers.end(), 9) != Numbers.end()  )
      {
            cout<<"Case #"<<i<<": "<<Result<<endl;
            Result = 0;
            x = 0;
            counter = 0;
            N = 0;
            Numbers.clear();

      }
      else if(counter == 500000)
        {
            cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
        }
        else
            {
              goto Here;

            }
                }

    }
        return 0;
}
