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
#include <math.h>
using namespace std;

int main(int argc, const char * argv[])
{

    // insert code here...
    ifstream fin;
    ofstream fout;
    int case_count;
    fin.open("data.in",std::ofstream::in);
    fout.open("data.out",std::ofstream::out);
    fin>>case_count;


    for (int step=0;step<case_count;step++)
    {
        int n,r,p,s;

        fin>>n;
        fin>>r;
        fin>>p;
        fin>>s;
       // cout<<n<<" "<<r<<" "<<p<<" "<<s<<endl;
        int a[14][8000] = {0};
        bool ans=false;
        for (int i=0;i<3;i++)
        {

            a[0][0]=i;
            for (int j=1;j<=n;j++)
                for (int k=0;k<pow(2,j);k++)
                {
                    if (a[j-1][k] == 0)
                    {
                        a[j][2*k] = 0;
                        a[j][2*k+1] = 2;

                    }
                    if (a[j-1][k] == 1)
                    {
                        a[j][2*k] = 1;
                        a[j][2*k+1] = 0;

                    }

                    if (a[j-1][k] == 2)
                    {
                        a[j][2*k] = 1;
                        a[j][2*k+1] = 2;

                    }

                }
            //cout<<"Case #"<<step+1<<": ";
            int countr=0;
            int countp=0;
            int counts=0;
            for (int j=0;j<pow(2,n);j++)
            {

                if (a[n][j]==0) {countr++;}
                if (a[n][j]==1) {countp++;}
                if (a[n][j]==2) {counts++;}
            }
          //  cout<<endl;
           // cout<<countr<<" "<<counts<<" "<<countp<<endl;

            if ((countr==r) &&(counts == s) &&(countp == p))
            {
                ans = true;
                fout<<"Case #"<<step+1<<": ";
                for (int j=n-1;j>0;j--)
                {

                    for (int k=0;k<pow(2,j);k+=2)
                    {
                      string s1="";
                      string s2="";
                     // cout<<n-j<<endl;
                     // cout<<(int)pow(2,n-j)* k <<" "<<(int)pow(2,n-j)* (k+1) <<endl;
                      for (int l=0;l<pow(2,n-j);l++)
                      {

                              if (a[n][(int)pow(2,n-j)* k + l]==0) s1+="R";
                              if (a[n][(int)pow(2,n-j)* k + l]==1) s1+="P";
                              if (a[n][(int)pow(2,n-j)* k + l]==2) s1+="S";
                              if (a[n][(int)pow(2,n-j)* (k+1) + l]==0) s2+="R";
                              if (a[n][(int)pow(2,n-j)* (k+1) + l]==1) s2+="P";
                              if (a[n][(int)pow(2,n-j)* (k+1) + l]==2) s2+="S";

                      }
                      //cout<<"cmp:"<<s1<<" "<<s2<<endl;
                      if (s1>s2) {
                       for (int l=0;l<pow(2,n-j);l++)
                       {
                            swap(a[n][(int)pow(2,n-j)* k + l],a[n][(int)pow(2,n-j)* (k+1) + l]);
                       }
                      }
                    }
                }
                for (int j=0;j<pow(2,n);j++)
                {
                    if (a[n][j]==0) fout<<"R";
                    if (a[n][j]==1) fout<<"P";
                    if (a[n][j]==2) fout<<"S";
                }
                fout<<endl;
                break;

            }
        }
        if (!ans) fout<<"Case #"<<step+1<<": IMPOSSIBLE"<<endl;

    }

    fin.close();
    fout.close();
    return 0;
}

