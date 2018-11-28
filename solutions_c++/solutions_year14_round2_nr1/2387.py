#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main()
{
    fstream file;
    ofstream output;
    file.open("A-small-attempt5.in");
    output.open("answer.txt");

    int n=0;

    file>>n;

    for(int i=0;i<n;i++)
    {
        //cout<<i<<endl;
        int p;
        file>>p;

        string first,second;

        file>>first;
        file>>second;

        int ans=0;

        int s1=first.size();
        int s2=second.size();

        int a=1,b=1;

        if(first[0]!=second[0])
        {
            output<<"Case #"<<i+1<<": "<<"Fegla Won"<<endl;
            //cout<<"Case #"<<i+1<<": "<<"Fegla Won"<<endl;
            continue;
        }
        bool flag=false;
        while(a!=s1||b!=s2)
        {
            if(a!=s1&&b!=s2&&first[a]==second[b])
            {
                a++;
                b++;
            }
            else if(a!=s1&&first[a]==second[b-1])
            {
                a++;
                ans++;
            }
            else if(b!=s2&&first[a-1]==second[b])
            {
                b++;
                ans++;
            }
            else
            {
                flag=true;
                break;

            }
        }

        if(!flag)
        {
            //cout<<"Case #"<<i+1<<": "<<ans<<endl;
            output<<"Case #"<<i+1<<": "<<ans<<endl;
        }
        else
        {
            //cout<<"Case #"<<i+1<<": "<<"Fegla Won"<<endl;
            output<<"Case #"<<i+1<<": "<<"Fegla Won"<<endl;

        }
        //cout<<i<<endl;

    }

}
