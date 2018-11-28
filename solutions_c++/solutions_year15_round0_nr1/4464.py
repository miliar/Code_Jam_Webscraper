/*
ID:thtfive
LANG:C++
*/
#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");

    int T;
    fin>>T;
    for (int Test=1;Test<=T;Test++)
    {
        int Smax;
        string str;
        fin>>Smax>>str;
        int len=str.length();
        int people[Smax];
        for (int i=0;i<len;i++)
            people[i]=str[i]-'0';
//        for (int i=0;i<=Smax;i++)
//            cout<<people[i];

        int NumOfFriend=0;
        for (int i=1;i<=Smax;i++)
        {
            if(people[i-1]<i)
            {
                int tmp=i-people[i-1];
                people[i-1]+=tmp;
                NumOfFriend+=tmp;
            }
            people[i]+=people[i-1];
        }
        fout<<"Case #"<<Test<<": "<<NumOfFriend<<"\n";

    }



    return 0;
}
