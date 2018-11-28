#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;

int main()
{
    ifstream fin("/home/ankit/Desktop/input.in");
    ofstream fout("/home/ankit/Desktop/output.txt");
    int t,t1;
    fin>>t;
    t1=t;
    vector<int> v;
    while(t--)
    {
        int arr[27]={0};
        int res;
        string s;
        fin>>s;
        int l=s.length();
        for(int i=0;i<l;i++)
        {
            int j=int(s[i])-64;
            arr[j]++;
        }
          while(arr[26]>0)//0
        {
            v.push_back(0);
            arr[26]--;
            arr[5]--;
            arr[15]--;
            arr[18]--;
        }
        while(arr[24]>0)//6
        {
            v.push_back(6);
            arr[19]--;
            arr[9]--;
            arr[24]--;
        }
        while(arr[23]>0)//2
        {
            v.push_back(2);
            arr[23]--;
            arr[20]--;
            arr[15]--;
        }
        while(arr[21]>0)//4
        {
            v.push_back(4);
            arr[6]--;
            arr[15]--;
            arr[21]--;
            arr[18]--;
        }
        while(arr[7]>0)//8
        {
            v.push_back(8);
            arr[7]--;
            arr[5]--;
            arr[9]--;
            arr[8]--;
            arr[20]--;
        }
        while(arr[20]>0)//3
        {
            v.push_back(3);
            arr[20]--;
            arr[8]--;
            arr[18]--;
            arr[5]--;
            arr[5]--;
        }
        while(arr[6]>0)//5
        {
            v.push_back(5);
            arr[6]--;
            arr[9]--;
            arr[22]--;
            arr[5]--;
        }
        while(arr[15]>0)//1
        {
            v.push_back(1);
            arr[15]--;
            arr[14]--;
            arr[5]--;
        }
        while(arr[19]>0)//7
        {
            v.push_back(7);
            arr[19]--;
            arr[5]--;
            arr[5]--;
            arr[22]--;
            arr[14]--;
        }
        while(arr[14]>0)//9
        {
            v.push_back(9);
            arr[14]--;
            arr[9]--;
            arr[14]--;
            arr[5]--;
        }
        sort(v.begin(),v.end());
        fout << "Case #" << t1-t << ": ";
        for(auto i=v.begin();i!=v.end();i++)
        {
            fout<<*i;
        }
        fout<<endl;
        v.clear();
    }
    return 0;
}


