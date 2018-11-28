#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <map>
#include <cmath>
#include <climits>
#include <queue>
#include <iomanip>
#include <cstdio>
#define lli long long int
#include<fstream>
using namespace std;

int main()
{
    ifstream cin("A-large.in");
	ofstream cout("output.txt");
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++){
        string st;
       cin>>st;
        int k,n,done=1,flips=0;
        cin>>k;
        n=st.length();

        for(int i=0;i<n&&done;i++){
            if(st[i]=='+')
                continue;

            int j=i+k-1;
            if(j>=n){
                done=0;
                break;
            }
            for(j=0;j<k;j++)
            {
                if(st[i+j]=='+')
                    st[i+j]='-';
                else st[i+j]='+';
            }
            flips++;
        }
        if(done)
        cout<<"Case #"<<tt<<": "<<flips<<endl;
        else  cout<<"Case #"<<tt<<": IMPOSSIBLE\n";
    }
}


