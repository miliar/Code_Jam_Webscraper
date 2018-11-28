#include<iostream>
using namespace std;
#include<deque>
#include<string>

int main()
{
    int tcase,current;
    int lol=1;
    cin>>tcase;
    string s;
    while(tcase--)
    {
        cin>>s;
        deque<char> a;
        for(int i=0;i<s.length();i++)
        {   if(int(s[i])>=int((a[0])))
              a.push_front(s[i]);
             else
             {a.push_back(s[i]);
      
             }
        }
         cout<<"Case #"<<lol<<": ";
        deque<char>:: iterator i;
       
        for( i=a.begin();i!=a.end();i++)
        cout<<*i;   
        
        cout<<endl;
        lol++;
    }
}


