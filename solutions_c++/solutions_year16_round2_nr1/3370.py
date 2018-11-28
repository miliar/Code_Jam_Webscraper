#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    cin>>t;
    fstream fout;
    string s;
    fout.open("out1b1.txt",ios::out);
    for(int j=0;j<t;j++)
    {   vector<int>v;
        cin>>s;
        int a[26]={0};
        for(int i=0;i<s.length();i++)
        {
           a[s.at(i)-'A']++;
        }
        while(a[25]&&a[4]&&a[17]&&a[14])
        {
            v.push_back(0);
            a[25]--;a[4]--;a[17]--;a[14]--;
        }
        while(a[5]&&a[14]&&a[20]&&a[17])
        {
            v.push_back(4);
            a[5]--;a[20]--;a[17]--;a[14]--;
        }
        while(a[19]&&a[22]&&a[14])
        {
            v.push_back(2);
            a[19]--;a[14]--;a[22]--;
        }
         while(a[8]&&a[4]&&a[6]&&a[7]&&a[19])
        {
            v.push_back(8);
            a[8]--;a[4]--;a[6]--;a[7]--;a[19]--;
        }
        while(a[18]&&a[8]&&a[23])
        {
            v.push_back(6);
            a[18]--;a[8]--;a[23]--;
        }
        while(a[13]&&a[4]&&a[14])
        {
            v.push_back(1);
            a[13]--;a[4]--;a[14]--;
        }

        while(a[19]&&a[7]&&a[17]&&a[4]>=2)
        {
            v.push_back(3);
            a[19]--;a[4]-=2;a[17]--;a[7]--;
        }

        while(a[5]&&a[8]&&a[21]&&a[4])
        {
            v.push_back(5);
            a[5]--;a[4]--;a[21]--;a[8]--;
        }

        while(a[13]&&a[4]>=2&&a[18]&&a[21])
        {
            v.push_back(7);
            a[13]--;a[4]-=2;a[18]--;a[21]--;
        }

        while(a[13]>=2&&a[8]&&a[4])
        {
            v.push_back(9);
            a[13]-=2;a[4]--;a[8]--;
        }
        fout<<"Case #"<<j+1<<": ";
        sort(v.begin(),v.end());
        for(int i=0;i<v.size();i++)
            fout<<v[i];
        fout<<endl;

    }

}
