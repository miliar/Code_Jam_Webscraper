#include <iostream>

using namespace std;

int main()
{
    int z;
    cin>>z;
    long long int new1,old,me,temp,count;
    for(int i=1;i<=z;i++)
    {
            cin>>new1>>old>>me;
              count=0;
            for(int x=0;x<new1;x++)
            {
                for(int y=0;y<old;y++)
                {



                    if((x&y)<me)
                    {
                      count++;
                    }

                }
            }

        cout<<"Case #"<<i<<": "<<count<<endl;


    }
    return 0;
}
