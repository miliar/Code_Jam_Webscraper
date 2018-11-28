//
//  main.cpp
//  MagicTrick
//
//  Created by L on 14-4-12.
//  Copyright (c) 2014ๅนด L. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <sstream>
using namespace std;
int a[5][5],n,ans ;
void dfs(int k,int s,int amount)
{
    if (k==n)
    {
        vector<string> b;
        int c[5] = {0};
        for (int i=0;i<n;i++)
        {
            string s="";
            for (int j=0;j<n;j++)
            {
                s+='0'+a[i][j];
                if (a[i][j]==1) c[i]++;
            }

            b.push_back(s);
        }
  //  cout<<"-----"<<endl;
    //  for (int i=0;i<n;i++)
     //   cout<<b[i]<<endl;
        for (int i=0;i<n;i++)
        {
            vector<int> check;
            for (int j=0;j<n;j++)
                if (a[j][i]==1) check.push_back(j);
            if (check.size()==0) return;
            int mod = check[0];
            if (c[mod]!=check.size()) return;
            bool iffind = true;
            for (int j=1;j<check.size();j++)
                if (b[check[j]]!=b[mod])
                    return;
        }
     //   for (int i=0;i<n;i++)
      //      cout<<b[i]<<endl;
        if (amount<ans)  ans = amount;
       // cout<<"ans="<<amount<<endl;

        return;

    }
    if (a[k][s]==1)
    {
        if (s+1<n) dfs(k,s+1,amount);
        else dfs(k+1,0,amount);
    }
    else
    {
        if (s+1<n)
        {
            dfs(k,s+1,amount);
            a[k][s] = 1;
            dfs(k,s+1,amount+1);
            a[k][s] =0;
        }
        else
        {
            dfs(k+1,0,amount);
            a[k][s] = 1;
            dfs(k+1,0,amount+1);
            a[k][s] =0;
        }
    }
}
int main(int argc, const char * argv[])
{

    // insert code here...
    ifstream fin;
    ofstream fout;
    int case_count;
    fin.open("data.in",std::ofstream::in);
    fout.open("data.out",std::ofstream::out);
    fin>>case_count;

    cout<<case_count<<endl;
    for (int step=0;step<case_count;step++)
    {
        fin>>n;
        string str;
        cout<<n<<endl;
        getline(fin,str);

        for (int i=0;i<n;i++)
        {

            getline(fin,str);
            for (int j=0;j<n;j++)
            {
                a[i][j]=str[j]-'0';

            }

        }
        ans = 25;
        dfs(0,0,0);
         fout<<"Case #"<<step+1<<": "<<ans<<endl;

    }

    fin.close();
    fout.close();
    return 0;
}

