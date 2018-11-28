#include <set> 
#include <vector>
#include <algorithm> 
#include <iostream>
#include <iterator>
using namespace std;

void GetAnswer(int caseno)
{
    vector<int> cards(16,0);
    int n, m;
    cin >> n;
    for ( int i = 0; i < 16; ++i)
    {
        cin >> cards[i];
    }
    
    std::set<int> first(cards.begin() + (n-1)*4, cards.begin() + n*4);
   // std::copy(cards.begin(), cards.end(), os);
   // std::copy(first.begin(), first.end(), os);
    cin >> m;

    for ( int i = 0; i < 16; ++i)
    {
        cin >> cards[i];
    }
    
    std::set<int>second(cards.begin() + (m-1)*4, cards.begin() + m*4);
    
    std::vector<int> intersect(4);
    typename std::vector<int>::iterator it = std::set_intersection(first.begin(), first.end(), second.begin(), second.end(), intersect.begin());

    

    std::cout << "Case #" << caseno <<": ";
    if ( it - intersect.begin()  == 0)
    {
        std::cout << "Volunteer cheated!" << std::endl;
    }
    else if ( it - intersect.begin()  > 1 ){
        std::cout << "Bad Magician!" << std::endl;
    }
    else if ( it - intersect.begin() == 1)
    {
        std::cout<<*intersect.begin() << std::endl;
    }
   return; 
}
int main()
{
   int T;
   cin >> T;
   for (int i = 0; i < T; ++i)
   {
       GetAnswer(i+1);
   }
   return 0 ;
}
