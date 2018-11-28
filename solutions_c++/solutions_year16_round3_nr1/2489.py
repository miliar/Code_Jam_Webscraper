#include <iostream>
#include <bits/stdc++.h>
#include <algorithm>
#include <fstream>
using namespace std;
bool placment( pair<int, int> p1, pair<int, int> p2){

        return (p1.first > p2.first);
}
int main()
{
   // cout << "Hello world!" << endl;

    int t,n,i,a,x;
    fstream f2,f1;
    f2.open("input.txt",ios::in);
    f1.open("output.txt",ios::out);
     pair <int,int> p[26];
cin>>t;
    //f2>>t;
    a=1;
    while(a<=t)
    {
    //
      cin>>n;
      //f2>>n;
        int sm=0;
        for(i=0;i<n;i++)
        {
            cin>>x;
         //   f2>>x;
            p[i]=make_pair(x,i+65);
            //a[i][1]=i+65;
            sm+=x;
        }
        sort(p,p+n,placment);
       cout<<"Case #"<<a<<": ";
       // f1<<"Case #"<<a<<": ";
        while(p[0].first>0)
{

                if(p[1].first<=(sm-1)/2)
                {
               cout<<(char)p[0].second;
            //   f1<<(char)p[0].second;
               p[0].first--;
                sm--;
                }
                else
                {
             cout<<(char)p[0].second<<(char)p[1].second;
                  //  f1<<(char)p[0].second<<(char)p[1].second;
                    sm-=2;
                    p[0].first--;
                    p[1].first--;
                }
           sort(p,p+n,placment);
           cout<<" ";
        //   f1<<" ";
        }
        cout<<"\n";
    //f1<<"\n";
        a++;
    }
    return 0;
}
