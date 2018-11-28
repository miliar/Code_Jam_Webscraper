#include<iostream>
#include<iomanip>
#include<string.h>
#include<vector>
#include <algorithm>
using namespace std;
int main()
{
    short unsigned int T = 0,c = 1;

    unsigned int N = 1,Nn = 1,winO = 0,winD = 0;
    unsigned int i = 0 , j = 0;

    double Ken[10],Nam[10];

    std::vector<int>::iterator it;


    cin>>T;
    while(T--)
    {
        cin>>N;
        winO = 0,winD = 0;
        for(i = 0;i<N;i++)
        {
            cin>>Nam[i];
        }
        for(i = 0;i<N;i++)
        {
            cin>>Ken[i];
        }
        sort(Ken,Ken+N);
        sort(Nam,Nam+N);
        vector<double> Kenny(Ken,Ken+N);

        Nn = N;
        i = 0;
        while(Nn > 0)
        {
            for(j = 0;j<Nn;j++)
            {
                if(Kenny[j]>Nam[i])
                {
                    Kenny.erase(Kenny.begin()+j);
                    break;
                }
            }
            if(j==Nn)
            {
                Kenny.erase(Kenny.begin());
                winO++;
            }
            i++;
            Nn--;
        }
        Kenny.clear();
        Nn = N;
        for(i = 0;i<Nn;i++)
            Kenny.push_back(Ken[i]);
        vector<double> Naomi(Nam,Nam+N);
        while(Nn > 0)
        {
            for(i = 0;i<Nn;i++)
            {
                if(Naomi[i]<Kenny[0])
                    continue;
                else
                    break;
            }
            Naomi.erase(Naomi.begin(),Naomi.begin()+i);
            Kenny.erase(Kenny.end()-i,Kenny.end());
            Nn = Nn-i;
            i = 0;
            while(i<Nn && Naomi[i]>Kenny[i])
            {
                i++;
                winD++;
            }
            Kenny.erase(Kenny.begin(),Kenny.begin()+i);
            Naomi.erase(Naomi.begin(),Naomi.begin()+i);
            Nn = Nn - i;
        }
        cout<<"Case #"<<c<<": "<<winD<<" "<<winO<<endl;
        c = c + 1;
    }
}
