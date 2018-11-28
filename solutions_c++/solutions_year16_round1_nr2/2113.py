#include<cstdio>
#include<iostream>
#include<algorithm>
#include <fstream>
#include<cstring>
#include<algorithm>
#include<string>
#include<vector>

using namespace std;

int main()
{
    ifstream in; //Creating object for input stream
    ofstream out; //Creating object for output stream
    in.open("large.in");    //open a file to read input
    out.open("outlarge.txt"); //open a file to write output
    int test,loop,n,i,il,j,num;
    int hgt[2501];
    vector<int> ans;
    in>>test;
    for(loop=1;loop<=test;loop++)
    {

        ans.clear();
        memset(hgt,0,sizeof hgt);
        in>>n;
        il=(2*n)-1;
        for(i=1;i<=il;i++)
        {
            for(j=1;j<=n;j++)
            {
                in>>num;
                hgt[num]++;
            }
        }
        for(i=1;i<=2500;i++)
        {
            if(hgt[i]%2==1)
                ans.push_back(i);
        }
        sort(ans.begin(),ans.end());
        out<<"Case #"<<loop<<":";
        for(i=0;i<ans.size();i++)
            out<<" "<<ans[i];
        out<<endl;
    }
    in.close();             //closing the input file
    out.close();            //closing the output file
return 0;
}
