#include<iostream>
#include<math.h>
#include<vector>
#include<algorithm>
#include<string>
#include <fstream>
#define mod 1000000007

using namespace std;

int main()
{
    int t,n;
    ifstream input;
    ofstream output;

    input.open("C:\\Users\\SHUBHAM\\Desktop\\code jam\\A.in.txt");
    output.open ("C:\\Users\\SHUBHAM\\Desktop\\code jam\\A.out.txt");
    input>>t;

    for(int i=1;i<=t;i++){
        input>>n;
        string x;
        input>>x;

        int total_people_standing=0,ans=0;
        for(int j=0;j<x.length();j++){
            int y=j-total_people_standing;
            y=y>0?y:0;

            //cout<<y<<" "<<total_people_standing<<endl;
            ans+=y;
            total_people_standing+=x[j]-48+y;
        }

        output<<"Case #"<<i<<": "<<ans<<endl;
    }

    input.close();
    output.close();
    return 0;
}
