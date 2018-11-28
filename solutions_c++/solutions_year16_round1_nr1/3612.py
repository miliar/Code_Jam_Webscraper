#include <map>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{

    int t;
    int i;
    cin>>t;
    i=1;


    while(t--)
    { string a;
        cin>>a;
        list<int>b;
         list<int>::iterator p=b.begin();

        b.push_back((int)a[0]);

        for(int h=1;h<a.size();h++)
        {   p=b.begin();
            if((int)(*p)>(int)a[h])
            {
                b.push_back((int)a[h]);
            }

            else
                b.push_front((int)a[h]);


        }

list<int>::iterator k=b.begin();

        cout<<"Case #"<<i<<":"<<" ";
        for(int h=0;h<b.size();h++,k++)
            cout<<(char)(*k);
        cout<<endl;
       i++;
       b.clear();



    }


}
