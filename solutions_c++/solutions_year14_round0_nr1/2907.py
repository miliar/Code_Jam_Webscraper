#include<iostream>
#include<iomanip>
#include<vector>
#include<string>
#include<fstream>
#include<list>
#include<cctype>
#include<algorithm>
#include<queue>
#include<stack>
#include<cmath>
#include<sstream>
#include<map>
#define long long LL

using namespace std;

int main ()
{
    ifstream cin("A-small-attempt0.in");
    ofstream cout("trick.out");
    int cas;
    cin>>cas;
    for(int i=0;i<cas;i++)
    {
        int row;
        vector<string>grid(4,"");
        vector<int>card(4);
        for(int k=0;k<2;k++)
        {
            cin>>row;
            cin.ignore();
            for(int j=0;j<4;j++)
            {
                getline(cin,grid[j]);
            }
            istringstream input(grid[row-1]);
            if(!k)
            {
                for(int j=0;j<4;j++)
                    input>>card[j];
            }
            else
            {
                int x;
                int counter=0;
                int temp=0;
                for(int l=0;l<4;l++)
                {
                    input>>x;
                    for(int s=0;s<4;s++)
                    {
                        if(card[s]==x)
                        {
                            counter++;
                            temp=x;
                        }

                    }
                }
                switch(counter)
                {
                case 0:
                    cout<<"Case #"<<i+1<<": Volunteer cheated!\n";
                    break;
                case 1:
                    cout<<"Case #"<<i+1<<": "<<temp<<"\n";
                    break;
                default:
                    cout<<"Case #"<<i+1<<": Bad magician!\n";
                    break;
                }

            }
        }

    }


    return 0;
}

