#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#define INT_MAX 2147483647
#define INT_MIN -2147483648
#define pi acos(-1.0)
#define N 1000000
#define LL long long
#include<fstream>
using namespace std;
int main()
{
    int tcase,ncase,num1[5][5],num2[5][5];
    cin>>ncase;
    ofstream myfile;
    myfile.open ("output.txt");


    for(tcase=1; tcase<=ncase; tcase++)
    {
        int r1,r2,i,j,k;
        int fis[5],sce[5];
        memset(num1,0,sizeof(num1));
        memset(num2,0,sizeof(num2));
        cin>>r1;

        for(i=1; i<=4; i++)
            for(j=1; j<=4; j++)
            {
                cin>>num1[i][j];
                if(r1==i)
                {
                    fis[j]=num1[i][j];
                }

            }
        cin>>r2;

        for(i=1; i<=4; i++)
            for(j=1; j<=4; j++)
            {
                cin>>num2[i][j];
                if(r2==i)
                {
                    sce[j]=num2[i][j];
                }

            }
        int fg=0,c=0,ans=0;

        for(i=1; i<=4; i++)
            for(j=1; j<=4; j++)
            {
                if(fis[i]==sce[j])
                {
                    c++;
                    ans=fis[i];
                }
            }

        cout<<"Case #"<<tcase<<": ";
        myfile <<"Case #"<<tcase<<": ";
        if(c>1)

        {
            cout<<"Bad magician!\n";
            myfile<<"Bad magician!\n";

        }
        else if(!c)
        {
            cout<<"Volunteer cheated!\n";
            myfile<<"Volunteer cheated!\n";
        }
        else if(c==1)
        {

            cout<<ans<<endl;
            myfile<<ans<<endl;


        }


    }
    myfile.close();

    return 0;
}

