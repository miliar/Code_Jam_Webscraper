#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <list>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <set>
using namespace std;
int main()
{
    freopen("output.txt","w",stdout);
    freopen ("input.txt","r",stdin);
    int tc;
    cin>>tc;
    set<char> vowels;
    vowels.insert('a');
    vowels.insert('e');
    vowels.insert('i');
    vowels.insert('o');
    vowels.insert('u');

    for(int t=1;t<=tc;t++)
    {
        string name;
        int n;
        cin>>name>>n;
        int count=0,flag=0;
        vector<int> position;
        int len=name.length();
        for(int j=0;name[j];j++)
        {
            if(vowels.find(name[j])==vowels.end())
            {
                count=1;
                if(n==1)
                {
                    position.push_back(j+1);
                    continue;
                }
                for(int k=j+1;name[k];k++)
                {

                    if(vowels.find(name[k])==vowels.end())
                    {
                        count++;
                        if(count==n)
                        {
                            position.push_back(j+1);
                            break;
                        }
                    }
                    else
                        break;
                }
            }
        }
        int sum=position.size();
        for(int i=0;i<position.size();i++)
        {
            int pos=position[i];
            int leftpos,rightpos;
            if(i==0)
            {
                leftpos=1;
            }
            else
            {
                leftpos=position[i-1]+1;
            }
            int leftcount,rightcount;
            leftcount=pos-leftpos;

            rightcount=len-(position[i]+n-1);
            sum+=(rightcount+leftcount+(rightcount*leftcount));

        }
        cout<<"Case #"<<t<<": "<<sum<<endl;

    }

    return 0;
}
