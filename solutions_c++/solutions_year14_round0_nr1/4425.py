#include<iostream>
#include <iomanip>
#include<vector>
#include<set>
#include<map>



using namespace std;

typedef set<int> IntSet;


int main()
{
    int T;
    cin >> T;
   
    for(int n =0; n<T; ++n)
    {
       IntSet row1;     
       int ans1,ans2;
       cin>>ans1;
       int num;
       for(int i=0; i< (ans1-1)*4; ++i)
       {
           cin >>num; 
       }
       for(int i=0; i< 4; ++i)
       {
          cin >> num;
          row1.insert(num);
       }
       for(int i=0; i< (4-ans1)*4; ++i)
       {
           cin >>num; 
       }
       
       cin>>ans2;
       for(int i=0; i< (ans2-1)*4; ++i)
       {
           cin >>num; 
       }
       int common=0;
       int savenum;
       for(int i=0; i< 4; ++i)
       {
        cin >> num;
        if(row1.find(num)!=row1.end())
        {
             savenum = num;
             ++common; 
        }
       }
       for(int i=0; i< (4-ans2)*4; ++i)
       {
           cin >>num; 
       }
       cout << "Case #" <<n+1<<": ";
       if(common == 0)
       cout<<"Volunteer cheated!\n";   
       else if(common > 1)
         cout<<"Bad magician!\n"; 
       else
         cout<<savenum<<"\n";
    }
    
}
