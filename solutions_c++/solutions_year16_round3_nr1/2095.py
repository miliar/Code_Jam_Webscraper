#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<set>
#include<map>
#include<climits>
#include<cstring>
#include<list>
#include<fstream>
#include<queue>
#include<sstream>
#include<stack>
#include<iomanip>


using namespace std;


typedef long long LL;
typedef unsigned int UI;

int n;
LL arr[27];

int main()
{

    ios_base::sync_with_stdio(false);
    //cin.tie(0);

    ifstream cin("A-large.in");
    ofstream cout("file2.txt");

    int T;
    cin>>T;

    for(int I=0; I<T; I++)
    {

        cin>>n;
        int tot=0;
        string ret;
        for(int i=1; i<=n; i++)
        {
            cin>>arr[i];
            tot+= arr[i];
        }

        while(tot>0)
        {
            string temp;
            int maxi=0;
            int ctr=0;

            for(int i=1; i<=n; i++)
            {
                if(arr[i]>maxi)
                {
                    ctr=1;
                    maxi=arr[i];
                }
                else if(arr[i]==maxi&&arr[i]>0)
                {
                    ctr++;
                }
            }

            for(int i=1; i<=n; i++)
            {
                if(arr[i]==maxi)
                {
                    if( (ctr==3&&temp.length()==1)||(temp.length()==2) )
                        continue;
                    else
                    {
                        temp+=(char)('A'+i-1);
                    }
                }

            }
            for(int i=0; i<temp.length(); i++)
                arr[temp[i]-'A'+1]--;

            tot-=temp.length();
            ret+=(temp+" ");
        }

        cout<<"Case #"<<I+1<<": "<<ret<<'\n';


    }


}



