#include<iostream>
#include<vector>
#include<cstring>
#include<stdlib.h>
#include<sstream>
#include<iterator>
#include<algorithm>
#include<set>
#include <utility>
using namespace std;

int main()
{

    int T,first,second,result;
    int arr[16];
    cin>>T;
    for(int i=0;i<T;i++)
    {
        cin>>first;

        for(int j=0;j<16;j++)
        {
            cin>>arr[j];

        }
        set<int> s(arr+((first-1)*4), arr +(first*4) );


        vector<int> v(s.begin(),s.end());

        cin>>second;

        for(int j=0;j<16;j++)
        {
            cin>>arr[j];

        }


        set<int> s1(arr+((second-1)*4), arr +(second*4) );

        vector<int>v1(s1.begin(),s1.end());
        v.insert(v.end(),v1.begin(),v1.end());
        sort(v.begin(),v.end());
       vector<int>::iterator it= adjacent_find(v.begin(),v.end());


       s.insert(s1.begin(),s1.end());

        result=s.size();
        int m=8-result;

        if(m==1)
        {
            cout<<"Case #"<<i+1<<": "<<*it<<endl;
        }
        else if(m==0)
        {
            cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;

        }

        else
        {
            cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
        }





    }



    return 0;
}
