#include<bits/stdc++.h>
using namespace std;
int main()
{
 int t;
 cin>>t;
 int m=1;
 while(t--)
   {
     string s;
     cin>>s;
     deque<char>avi;
     ofstream myfile;
     myfile.open("output4.txt");
     deque<char>::iterator it = avi.begin();
     int l=s.length(),k=0;
     string s1;
     avi.push_front(s[0]);
     for(int i=1;i<l;i++)
     {
      if(avi.front()<=s[i])
     {
        avi.push_front(s[i]);
     }
     else
     avi.push_back(s[i]);

     }
             //myfile<<"Case #"<<k<<": ";
                      cout<<"Case #"<<m<<": ";
       for (it = avi.begin(); it!=avi.end(); ++it)
       {

       // myfile<<*it;
         cout<< *it;
       }
       m++;
       //myfile<<"\n";
      cout<<"\n";

   }
}
