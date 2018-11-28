#include<iostream>
using namespace std;
main()
{
int T;
cin>>T;
for(int i=0;i<T;i++)
{
    int Smax;
    cin>>Smax;
    string people;
    cin>>people;
    int ExtraFriends=0,Sum=people[0]-'0';
   // cout<<Sum;
    for(int j=1;j<Smax+1;j++)
    {

        if(j>Sum)
        {

            ExtraFriends+=j-Sum;
            Sum+=j-Sum;


        }
        Sum+=people[j]-'0';
    }
cout<<"Case #"<<i+1<<": "<<ExtraFriends<<endl;
}
}
