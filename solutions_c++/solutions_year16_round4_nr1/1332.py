#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
int n,p,r,s,tot;
int status=0;


int main()
{
    ofstream coutt("output.txt");
    ifstream cinn("input.txt");
    int T;
    cinn>>T;
    for(int ii=0;ii<T;ii++)
    {
        coutt<<"Case #"<<ii+1<<": ";

        int cnt0=0;
        cinn>>n>>r>>p>>s;
        tot=s+r+p;
        if(p==0)cnt0++;
        if(r==0)cnt0++;
        if(s==0)cnt0++;
        if(cnt0>=2)
        {
            coutt<<"IMPOSSIBLE"<<endl;
            continue;
        }
        if(r==0||(p==0||s==0))
        {
            if(n==1)
            {
                for(int i=0;i<p;i++)coutt<<"P";
                for(int i=0;i<r;i++)coutt<<"R";
                for(int i=0;i<s;i++)coutt<<"S";

                coutt<<endl;
                continue;
            }
            else
            {
                coutt<<"IMPOSSIBLE"<<endl;
                continue;
            }
        }
        int aa=p-s,bb=p-r,cc=r-s;
        if(aa*aa>1||(bb*bb>1||cc*cc>1))
        {
            coutt<<"IMPOSSIBLE"<<endl;
                continue;
        }
        if(p>s&&p>r)status=0;
        else if(s>p&&s>r)status=1;
        else if(r>s&&r>p)status=2;
        else if(p==s)status=0;
        else if(p==r)status=2;
        else if(r==s)status=1;
        vector <string> arr;
        while(tot!=0)
        {
            if(status==0)
            {
                arr.push_back("P");
                status=1;
                tot--;
            }
            else if(status==2)
            {
                arr.push_back("R");
                status=0;tot--;

            }
            else{arr.push_back("S");
                status=2;tot--;

            }
        }
        while(arr.size()!=1)
        {
            vector <string> arr2;
            for(int i=0;i<arr.size()/2;i++)
            {
                if(arr[i*2].compare(arr[i*2+1])<=0)
                {
                    arr2.push_back(arr[i*2]);
                    arr2[i].append(arr[i*2+1]);
                }
                else
                {
                    arr2.push_back(arr[i*2+1]);
                    arr2[i].append(arr[i*2]);
                }
            }
            arr=arr2;
        }

        coutt<<arr[0]<<endl;

    }
}
